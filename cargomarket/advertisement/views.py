from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from advertisement.models import Advertisement
from advertisement.forms import AdvertisementForm, AdvertisementEditForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def ad_list(request):
    user = User.objects.get(username=request.user.username)
    advertisement = Advertisement.objects.filter(ad_state=1).all()

    return render(request, template_name="adList.html", context={'user' : user, 'advertisement':advertisement})

@login_required
def create_ad(request):
    user = User.objects.get(username=request.user.username)
    form = AdvertisementEditForm()
    if request.method == 'POST':
        form = AdvertisementEditForm(request.POST, instance=user)
        form.user_id = user.id
        if form.is_valid():
            form.save()

            messages.success(request, ('Kayıt Başarılı'))
            return redirect('detail_ad', ad_id=ad_id)
        else :
            messages.error(request, ('Lütfen alanları eksiksiz doldurun.'))

    return render(request, template_name="createAd.html", context={'user':user, 'form':form})


@login_required
def update_ad(request, ad_id):
    user = User.objects.get(username=request.user.username)
    adp = Advertisement.objects.get(id=ad_id)
    dltId=ad_id
    if request.method == 'POST':
        form = AdvertisementEditForm(request.POST, instance=adp)

        if form.is_valid():
            form.save()
            messages.success(request,('İlan Güncelleme Tamamlandı!'))
            return redirect('detail_ad', ad_id=ad_id)
    else:
        form = AdvertisementForm(instance=adp)

    return render(request, template_name='updateAd.html', context={'user':user, 'form':form, 'dltId':dltId})

@login_required
def my_ad(request):
    user = User.objects.get(id=request.user.id)
    my_ad = Advertisement.objects.filter(user_id=request.user.id)

    return render(request, template_name="myAd.html", context={'user' : user, 'my_ad':my_ad})


@login_required
def detail_ad(request, ad_id):
    user = User.objects.get(id=request.user.id)
    form = Advertisement.objects.get(id=ad_id)
    own = Advertisement.objects.get(id=ad_id).user_id

    if request.user.id != own:
        show = Advertisement.objects.get(id=ad_id).ad_show
        show = show + 1  
        Advertisement.objects.filter(id=ad_id).update(ad_show = show)

    return render(request, template_name="detailAd.html", context={'user' : user, 'form':form})

@login_required
def delete_ad(request, ad_id):
    user = User.objects.get(id=request.user.id)
   
    Advertisement.objects.filter(id=ad_id).update(ad_state='0')

    messages.success(request,('İlan Silindi!'))
    return redirect('my_ad')
    
@login_required
def all_ad(request):
    ads = Advertisement.objects.all()

    return render(request, template_name="allAd.html", context={'ads':ads})

#@login_required
def recourse(request, ad_id):
    user= User.objects.get(id=request.user.id)

    if user.first_name == ' ' :
        messages.error(request,('Önce Profil bilgilerinizi doldurunuz!'))
        return redirect('my_profile')
    else :
        Advertisement.objects.filter(id=ad_id).set(applicants=request.user.id)
        #form = Advertisement.objects.get(id=ad_id)
        #form.applicants.set(str(request.user.id))
        #form.save()
        messages.success(request,('Başvurunuz iletildi!'))
        return redirect('detail_ad', ad_id=ad_id)


@login_required
def my_recourse(request):

    return render(request, template_name="myRecourse.html", context={})