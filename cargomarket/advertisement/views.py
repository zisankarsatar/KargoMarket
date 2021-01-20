from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from advertisement.models import Advertisement, Application
#from account.models import License
from advertisement.forms import AdvertisementForm, AdvertisementEditForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.timezone import localdate

# Create your views here.

@login_required
def ad_list(request):
    user = request.user
    search_post = request.GET.get('search')
    if search_post :
        advertisement = Advertisement.objects.filter(ad_title__contains=search_post, ad_state=1)
    else :
        advertisement = Advertisement.objects.filter(ad_state=1).order_by("-last_date").all()

    return render(request, template_name="adList.html", context={'user' : user, 'advertisement':advertisement})

@login_required
def create_ad(request):
    user = request.user
    #all_l = License.objects.all()
    if user.first_name :
        form = AdvertisementForm()    
        if request.method == 'POST':
            form = AdvertisementForm(request.POST)
            if form.is_valid():
                new_ad = form.save(commit=False)
                new_ad.user = user
                new_ad.save()
                messages.success(request, ('Kayıt Başarılı'))
                return redirect('my_ad')
            else :
                messages.error(request, ('Lütfen alanları eksiksiz doldurun.'))
        
        return render(request, template_name="createAd.html", context={'user':user, 'form':form}) #, 'all_l': all_l})

    else : 
        messages.error(request,('Önce Profil bilgilerinizi doldurunuz!'))
        return redirect('myprofile')
    

@login_required
def update_ad(request, ad_id):
    user = request.user
    adp = Advertisement.objects.get(id=ad_id)

    if request.method == 'POST':
        form = AdvertisementEditForm(request.POST, instance=adp)

        if form.is_valid():
            form.save()
            messages.success(request,('İlan Güncelleme Tamamlandı!'))
            return redirect('detail_ad', ad_id=ad_id)
    else:
        form = AdvertisementEditForm(instance=adp)


    return render(request, template_name='updateAd.html', context={'user':user, 'form':form, 'dltId':ad_id, 'last_date': str(adp.last_date) })

@login_required
def my_ad(request):
    user = request.user
    search_post = request.GET.get('search')
    if search_post :
        my_ad = Advertisement.objects.filter(ad_title__contains=search_post)
    else : 
        my_ad = Advertisement.objects.filter(user_id=request.user.id)

    return render(request, template_name="myAd.html", context={'user' : user, 'my_ad':my_ad})


@login_required
def detail_ad(request, ad_id):
    user = User.objects.get(id=request.user.id)
    form = Advertisement.objects.get(id=ad_id)
    own = Advertisement.objects.get(id=ad_id).user_id
        
    showApp = 0
    
    if Application.objects.filter(add_id=ad_id , user_id=request.user.id):
        showApp = 1    

    if request.user.id != own:
        show = Advertisement.objects.get(id=ad_id).ad_show
        show = show + 1  
        Advertisement.objects.filter(id=ad_id).update(ad_show = show)

    return render(request, template_name="detailAd.html", context={'user' : user, 'form':form, 'showApp':showApp})

@login_required
def delete_ad(request, ad_id):
    user = User.objects.get(id=request.user.id)
   
    Advertisement.objects.filter(id=ad_id).update(ad_state='0')

    messages.success(request,('İlan Silindi!'))
    return redirect('my_ad')
    
@login_required
def all_ad(request):
    search_post = request.GET.get('search')
    if search_post :
        ads = Advertisement.objects.filter(ad_title__contains=search_post)
    else : 
        ads = Advertisement.objects.all()

    return render(request, template_name="allAd.html", context={'ads':ads})

@login_required
def recourse(request, ad_id):
    user= User.objects.get(id=request.user.id)

    if user.first_name :
        app = Application()
        app.add_id = ad_id
        app.user_id = user.id
        app.app_state = 0
        app.app_date = localdate()
        app.save()       

        messages.success(request,('Başvurunuz iletildi!'))
        return redirect('detail_ad', ad_id=ad_id)
    else :        
        messages.error(request,('Önce Profil bilgilerinizi doldurunuz!'))
        return redirect('myprofile')

        

@login_required
def my_recourse(request):
    user = request.user
    search_post = request.GET.get('search')
    if search_post :
        adlist = Advertisement.objects.filter(ad_title__contains=search_post,ad_state=1)
    else : 
        adlist = Advertisement.objects.filter(ad_state=1).all() #ilan bilgilerini yazdırmak için tüm ilanlar çekilir, bu kod değişmeli

    applist = Application.objects.filter(user_id=user.id) #kullanıcın tüm başvuruları çekilir
    
    return render(request, template_name="myRecourse.html", context={"applist":applist, 'adlist':adlist})

@login_required
def applicants_list(request, ad_id):
    appList = Application.objects.filter(add_id=ad_id)#ilan numarasına ait başvurular çekilir
    ad = Advertisement.objects.get(id=ad_id)
    users = User.objects.all()

    return render (request, template_name="applicantsList.html", context={"appList":appList, "ad":ad, "users":users})

@login_required
def state_set(request, app_id ,state):
    Application.objects.filter(id=app_id).update(app_state=state)
    ad_id = Application.objects.get(id=app_id)
    print(ad_id)
    messages.success(request,('Durum değiştirildi'))
    return redirect('app_list', ad_id=ad_id.add_id)