from advertisement.models import Advertisement

from django import forms


class AdvertisementForm(forms.ModelForm):

    class Meta:
        model = Advertisement
        fields = '__all__'
        #fields = ['ad_explain', 'from_city', 'to_city', 'publish_date','last_date','product_total_weight','product_total_volume','product_type','licenses','product_risk']
        exclude = ['user']

        publish_date = forms.DateField(input_formats='%Y,%m,%d',widget=forms.SelectDateWidget())
        last_date = forms.DateField(input_formats='%Y,%m,%d',widget=forms.SelectDateWidget())


class AdFormUpdate(forms.ModelForm):

    class Meta:
        model = Advertisement
        fields = '__all__'
        #fields = ['ad_explain', 'from_city', 'to_city', 'publish_date','last_date','product_total_weight','product_total_volume','product_type','licenses','product_risk','user']
        # exclude = ['user']

        publish_date = forms.DateField(input_formats='%Y,%m,%d',widget=forms.SelectDateWidget())
        last_date = forms.DateField(input_formats='%Y,%m,%d',widget=forms.SelectDateWidget())