from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from advertisement.models import Advertisement
from advertisement.forms import AdvertisementForm, AdFormUpdate
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def ad_list(request):
    user = User.objects.get(username=request.user.username)
    advertisement = Advertisement.objects.all()
    #form = AdvertisementForm()

    ##return render(request, template_name="advertisement.html", context={'user' : user, 'form':form})
    return render(request, template_name="adList.html", context={'user' : user, 'advertisement':advertisement})

@login_required
def create_ad(request):
    user = User.objects.get(username=request.user.username)
    form = AdvertisementForm()
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            #messages.success(request, ('Kayıt Başarılı'))
            return redirect('my_ad')
        #else :
            #messages.error(request, ('Lütfen alanları düzgün doldurun.'))
    #return render(request, template_name="createAd.html", context={"form": form})
    return render(request, template_name="createAd.html", context={'user':user, 'form':form})


@login_required
def update_ad(request, ad_id):
    user = User.objects.get(username=request.user.username)
    adp = Advertisement.objects.get(id=ad_id)
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, instance=adp)

        if form.is_valid():
            form.save()
            return redirect('home')
            #messages.success(request,('İlan Güncellendi!'))
            #return redirect('my_ad'+ str(user.id))      
                  
    else:
        form = AdvertisementForm(instance=adp)

    return render(request, template_name='updateAd.html', context={'user':user, 'form':form})

@login_required
def my_ad(request, user_id):
    user = User.objects.get(id=user_id)
    my_ad = Advertisement.objects.filter(user_id=user_id)

    return render(request, template_name="myAd.html", context={'user' : user, 'my_ad':my_ad})


@login_required
def detail_ad(request, ad_id):
    user = User.objects.get(id=request.user.id)
    form = Advertisement.objects.get(id=ad_id)

    return render(request, template_name="detailAd.html", context={'user' : user, 'form':form})
       