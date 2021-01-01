from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BaseProfile(models.Model):
    phone_number = models.CharField('Phone number', max_length=11)
    websiteUrl = models.CharField('website', max_length=50 , default="www.website.com")
    facebookUrl = models.CharField('facebook', max_length=50 , default="www.facebook.com")
    #profile_pic = models.CharField('profile_pic', max_length=50)
    
    class Meta:
        abstract = True


class License(models.Model):
    license_name = models.CharField('License Name', max_length=50)
    license_description = models.CharField('License Description', max_length=200)

class DrivingLicense(models.Model):
    driving_name = models.CharField('License Name', max_length=50)
    driving_description = models.CharField('License Description', max_length=200)


class DriverProfile(BaseProfile):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.CharField('Age', max_length=3)
    gender = models.CharField('Gender', max_length=5) 
    nationality = models.CharField('Nationality', max_length=50)
    languages = models.CharField('Languages', max_length=100)
    experience = models.CharField('Experience', max_length=50)
    licenses = models.ManyToManyField(License, blank=True, verbose_name='Licenses')
    driving_licenses = models.ManyToManyField(DrivingLicense, blank=True, verbose_name='Driving Licenses')
    truck_model = models.CharField('Truck Model', max_length=50, default='not specified')
    max_capacity = models.DecimalField('Truck Capacity', max_digits=5, decimal_places=2, default="25.8")
    # review_point = models.DecimalField('Point', max_digits=2, decimal_places=1)
    

class CompanyProfile(BaseProfile):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    explain=models.CharField('Bio Explain', max_length=500)
    address = models.CharField('Address', max_length=200) 
    vd_no = models.CharField('VD. No', max_length=50)
