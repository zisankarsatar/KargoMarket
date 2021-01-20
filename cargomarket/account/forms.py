from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from account.models import CompanyProfile, DriverProfile, License, DrivingLicense


from django import forms

PROFILE_TYPE_CHOICES = [
    ('company', 'Yük Sahibi'),
    ('driver', 'Sürücü'),
    ]

PICTURE_CHOICES= [
    ('#','Seçiniz'),
    ('https://images.unsplash.com/photo-1601455763557-db1bea8a9a5a?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1086&q=80', 'Erkek'),
    ('https://images.unsplash.com/photo-1544725176-7c40e5a71c5e?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1047&q=80', 'Kadın'),
]

class UserCreateForm(UserCreationForm):
    profile_type = forms.CharField(label='What is your role?', widget=forms.RadioSelect(choices=PROFILE_TYPE_CHOICES))

    class Meta:
        model = User
        fields = ("username", "email",)

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(UserCreateForm, self).save(commit=True)

        if self.cleaned_data['profile_type'] == 'driver':
            dp = DriverProfile(user=user)
            dp.save()
            return user
        
        cp = CompanyProfile(user=user)
        cp.save()
        return user


class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = '__all__'
        exclude = ['user']


class DriverProfileForm(forms.ModelForm):
    # licences = forms.MultipleChoiceField
    class Meta:
        model= DriverProfile
        fields= '__all__'
        exclude=['user'] #user haric

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]
        #fields = '__all__'

class DriverProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = DriverProfile
        fields = '__all__'
        #fields = ['age', 'phone_number', 'nationality', 'experience','websiteUrl','facebookUrl','licenses','driving_licenses','languages','profile_pic',]
        exclude = ['user']

    profile_pic = forms.CharField(widget=forms.Select(choices=PICTURE_CHOICES))
    licenses = forms.ModelMultipleChoiceField(queryset=License.objects.all(), widget=forms.CheckboxSelectMultiple)
    driving_licenses = forms.ModelMultipleChoiceField(queryset=DrivingLicense.objects.all(), widget=forms.CheckboxSelectMultiple)

class CompanyProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        #fields = '__all__'
        fields = ['phone_number', 'address','websiteUrl', 'facebookUrl','explain',"vd_no",]
        exclude = ['user']