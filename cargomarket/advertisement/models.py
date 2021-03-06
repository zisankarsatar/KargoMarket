from django.db import models
from django.contrib.auth.models import User
from account.models import License

# Create your models here.

class Advertisement(models.Model):
    ad_title = models.CharField('Ad Title', max_length=50)
    ad_explain = models.CharField('Ad Explain', max_length = 500)
    from_city = models.CharField('From City', max_length = 25)
    to_city = models.CharField('To City', max_length = 25)
    publish_date = models.DateField('Publish Date', auto_now_add=True)
    last_date = models.DateField('Last Date')
    total_weight = models.CharField('Product Weigth', max_length=25)
    total_volume = models.CharField('Product Volume', max_length=25)
    licenses = models.ManyToManyField(License, blank=True, verbose_name='Licenses')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad_state=models.IntegerField('Ad State', default=1)
    ad_show=models.IntegerField('Ad Show', default=0)
    img = models.CharField('Img Select', max_length=400)


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #user olarak düzelt
    add_id = models.IntegerField('Ad id') #ad_id olarak düzelt
    app_date = models.DateField('Application Date')
    app_state = models.IntegerField('app state', default = 0) #0 görülmemiş, 1 onaylanmış , 2 red
    
