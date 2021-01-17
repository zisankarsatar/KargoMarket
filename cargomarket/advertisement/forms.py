from advertisement.models import Advertisement
from account.models import License

from django import forms


class AdvertisementForm(forms.ModelForm):

    class Meta:
        model = Advertisement
        fields = '__all__'
        #fields = ['id','ad_explain', 'from_city', 'to_city', 'publish_date','last_date','total_weight','total_volume','licenses']
        exclude = ['user']

        licenses = forms.ModelMultipleChoiceField(queryset=License.objects.all(), widget=forms.CheckboxSelectMultiple)
        publish_date = forms.DateField(input_formats='%d/%m/%Y',widget=forms.SelectDateWidget())
        last_date = forms.DateField(input_formats='%d/%m/%Y',widget=forms.SelectDateWidget())

class AdvertisementEditForm(forms.ModelForm):

    class Meta:
        model = Advertisement
        fields = ['id','ad_title','ad_explain', 'from_city', 'to_city', 'publish_date','last_date','total_weight','total_volume','licenses']
        exclude = ['user']

        licenses = forms.ModelMultipleChoiceField(queryset=License.objects.all(), widget=forms.CheckboxSelectMultiple)
        publish_date = forms.DateField(input_formats='%d/%m/%Y',widget=forms.SelectDateWidget())
        last_date = forms.DateField(input_formats='%d/%m/%Y',widget=forms.SelectDateWidget())
