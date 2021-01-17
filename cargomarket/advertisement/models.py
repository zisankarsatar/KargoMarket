from django.db import models
from django.contrib.auth.models import User
from account.models import License

# Create your models here.

#class ProductType(models.Model):
#    risk_degree = models.IntegerField('Risk Degree')
#    risk_explain = models.CharField('Risk Degree', max_length=50)

class Advertisement(models.Model):
    ad_title = models.CharField('Ad Title', max_length=50)
    ad_explain = models.TextField('Ad Explain', max_length = 500)
    from_city = models.CharField('From City', max_length = 25)
    to_city = models.CharField('To City', max_length = 25)
    publish_date = models.DateField('Publish Date')
    last_date = models.DateField('Last Date')
    total_weight = models.CharField('Product Weigth', max_length=25)
    total_volume = models.CharField('Product Volume', max_length=25)
    #product_type = models.OneToOneField(ProductType, blank=True, verbose_name='Product Type')
    licenses = models.ManyToManyField(License, blank=True, verbose_name='Licenses')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad_state=models.IntegerField('Ad State', default=1)
    ad_show=models.IntegerField('Ad Show', default=0)
    applicants = models.ManyToManyField(User, blank=True, related_name='Applicants', default='')
