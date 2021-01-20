from advertisement.models import Advertisement, Application
from account.models import License

from django import forms
IMG_CHOICES= [
    ('#','Seçiniz'),
    ('https://images.unsplash.com/photo-1452948491233-ad8a1ed01085?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1053&q=80', 'Meyve ve Sebze'),
    ('https://images.unsplash.com/photo-1472141521881-95d0e87e2e39?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1052&q=80', 'Bakliyat'),
    ('https://images.unsplash.com/photo-1516199423456-1f1e91b06f25?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1032&q=80', 'Pertol'),
    ('https://images.unsplash.com/photo-1543389776-543c767cd200?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1050&q=80', 'Ev Eşyaları'),
    ('https://images.unsplash.com/photo-1549127024-5f213d45604a?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1053&q=80', 'Cam vs Kırılıcak'),
    ('https://images.unsplash.com/photo-1471174466996-0aa69dbda661?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=924&q=80', 'Elektornik'),
    ('https://images.unsplash.com/photo-1547447379-7e2485fa95f8?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80', 'Demir ve Çelik'),
    ('https://images.unsplash.com/photo-1582282577230-2f59c636e60b?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1052&q=80', 'Odun Kereste'),
    ('https://images.unsplash.com/photo-1566125882500-87e10f726cdc?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=967&q=80', 'Zarf, Döküman'),
    ('https://images.unsplash.com/photo-1597074753149-53c386367bdf?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80', 'Diğer'),
]
class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        #fields = '__all__'
        fields = ['ad_title','ad_explain', 'from_city', 'to_city', 'last_date', 'total_weight','total_volume','licenses', 'img']
        exclude = ['user']

    img = forms.CharField(widget=forms.Select(choices=IMG_CHOICES))
    licenses = forms.ModelMultipleChoiceField(queryset=License.objects.all(), widget=forms.CheckboxSelectMultiple)
    last_date = forms.CharField()

    # def save(self, *args, **kwargs):
    #     self.kwargs = 


class AdvertisementEditForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['ad_title','ad_explain', 'from_city', 'to_city', 'last_date', 'total_weight','total_volume','licenses']
        exclude = ['user']

    licenses = forms.ModelMultipleChoiceField(queryset=License.objects.all(), widget=forms.CheckboxSelectMultiple)
    last_date = forms.CharField()


class ApplicationForm(forms.ModelForm):
    class Meta:
        model: Application
        fields = ['app_state']
        exclude = ['user']
