"""cargomarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from account.views import register, myprofile, home, change_password ,myprofile_edit, user_list,show_profile

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    path('accounts/register/', register, name='register'),
    path('accounts/myprofile/', myprofile, name='myprofile'),
    path('accounts/myprofile_edit/', myprofile_edit, name='myprofile_edit'),
    path('accounts/profile/id=<int:user_id>', show_profile, name='show_profile'),
    path('accounts/password/', change_password, name='password'),
    path('accounts/users/', user_list, name='users') 
]
