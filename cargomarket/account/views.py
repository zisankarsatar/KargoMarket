from django.shortcuts import render, redirect
from django.urls import reverse
from account.forms import UserCreateForm, CompanyProfileForm, DriverProfileForm, DriverProfileUpdateForm, CompanyProfileUpdateForm, UserUpdateForm
from account.models import CompanyProfile, DriverProfile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('myprofile'))

    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    return render(request, template_name="account/register.html", context={"form": form})


def base(request):
    return render(request, template_name="base/base.html", context={'user' : request.user})


@login_required
def home(request):
    return render(request, template_name="account/home.html", context={'user' : request.user})


@login_required
def myprofile(request):
    user = User.objects.get(username=request.user.username)
    try:
        if user.driverprofile:
            role = 'driver'
            dp = DriverProfile.objects.get(user=user)
            form = DriverProfileForm(instance=dp)
            profile = DriverProfile.objects.get(user=user)
        
        return render(request, template_name='account/myprofileD.html', context={'role': role, 'user': user,  'profile':profile})
    except:
        role = 'company'
        cp = CompanyProfile.objects.get(user=user)
        form = CompanyProfileForm(instance=cp)
        profile = CompanyProfile.objects.get(user=user)
        
    return render(request, template_name='account/myprofileC.html', context={'role': role, 'user': user,  'profile':profile})


@login_required
def myprofile_edit(request):
    user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        try:
            if user.driverprofile:
                role = 'driver'
                dp = DriverProfile.objects.get(user=user)
                p_form = DriverProfileUpdateForm(request.POST, instance=dp)
        except:
            role = 'company'
            cp = CompanyProfile.objects.get(user=user)
            p_form = CompanyProfileUpdateForm(request.POST, instance=cp)          

        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Your Profile has been updated!')
            
            return redirect('myprofile')
    else:
        u_form = UserUpdateForm(instance=request.user)            
        try:
            if user.companyprofile:
                role = 'company'
                cp = CompanyProfile.objects.get(user=user)
                p_form = CompanyProfileUpdateForm(instance=cp)

            return render(request, 'account/myprofileC_edit.html',context={'p_form': p_form, 'u_form': u_form} )
        except: 
            role = 'driver'
            dp = DriverProfile.objects.get(user=user)
            p_form = DriverProfileUpdateForm(instance=dp)
    
    return render(request, 'account/myprofileD_edit.html',context={'p_form': p_form, 'u_form': u_form} )
   
@login_required
def user_list(request):
    users = User.objects.all()

    return render(request, template_name="account/users.html", context={'users' : users})

@login_required
def show_profile(request, user_id):
    user = User.objects.get(id=user_id)
    try:
        if user.driverprofile:
            role = 'driver'
            dp = DriverProfile.objects.get(user=user)
            form = DriverProfileForm(instance=dp)
            profile = DriverProfile.objects.get(user=user)

        return render(request, template_name='account/myprofileD.html', context={'role': role, 'user': user,  'profile':profile})
    except:
        role = 'company'
        cp = CompanyProfile.objects.get(user=user)
        form = CompanyProfileForm(instance=cp)
        profile = CompanyProfile.objects.get(user=user)
        
    return render(request, template_name='account/myprofileC.html', context={'role': role, 'user': user,  'profile':profile})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')

            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'account/password.html', {'form': form})