from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BaseProfile(models.Model):
    phone_number = models.CharField('Phone number', max_length=11)
    websiteUrl = models.CharField('website', max_length=50 , default="www.website.com")
    facebookUrl = models.CharField('facebook', max_length=50 , default="www.facebook.com")
    
    class Meta:
        abstract = True


class License(models.Model):
    license_name = models.CharField('License Name', max_length=50)
    license_description = models.CharField('License Description', max_length=200)
    
    def __str__(self):
        return '{} | {}'.format( self.license_name, self.license_description )


class DrivingLicense(models.Model):
    driving_name = models.CharField('License Name', max_length=50)
    driving_description = models.CharField('License Description', max_length=200)

    def __str__(self):
        return '{} | {}'.format( self.driving_name, self.driving_description )


class DriverProfile(BaseProfile):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.CharField('Age', max_length=3)
    nationality = models.CharField('Nationality', max_length=50)
    languages = models.CharField('Languages', max_length=100)
    experience = models.CharField('Experience', max_length=50)
    licenses = models.ManyToManyField(License, blank=True, verbose_name='Licenses')
    driving_licenses = models.ManyToManyField(DrivingLicense, blank=True, verbose_name='Driving Licenses')
    truck_brand = models.CharField('Truck Brand', max_length=25)
    truck_model = models.CharField('Truck Model', max_length=50)
    truck_fuel = models.CharField('Truck Fuel', max_length=25)
    truck_gear = models.CharField('Truck Gear', max_length=25)
    max_capacity = models.DecimalField('Truck Capacity', max_digits=5, decimal_places=2, default='200')
    profile_pic = models.CharField('Profile Pic', max_length=400, default="https://lh3.googleusercontent.com/proxy/QCXzPUrnqqkX-cZFyQ3TBYrpduTFBjg7ifzx_SB4EPnIwpBf6WUDxwrHRgXK2xxO5fZwZSBPWlfVhhoTJdjeZPxGhcQrCqcLT_SRmr9idRZlZ_dRTNqAistv1nfifi25F-V9XkV-5fBpDyk-PzqSGoU3Gg")

    def __str__(self):
        return 'Driver: {}'.format(self.user.username)    

class CompanyProfile(BaseProfile):
    picture  = models.CharField('Profile Pic', max_length=400, default="https://images.unsplash.com/photo-1550136513-548af4445338?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1054&q=80")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    explain=models.CharField('Bio Explain', max_length=500)
    address = models.CharField('Address', max_length=200) 
    vd_no = models.CharField('VD. No', max_length=50, blank=True)

    def __str__(self):
        return 'Company: {}'.format(self.user.username)