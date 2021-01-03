from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from account.models import CompanyProfile, DriverProfile, License, DrivingLicense


from django import forms

PROFILE_TYPE_CHOICES = [
    ('company', 'Yük Sahibi'),
    ('driver', 'Sürücü'),
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
        #fields = ['age', 'phone_number', 'gender', 'nationality', 'experience','websiteUrl','facebookUrl','licenses','driving_licenses','languages']
        exclude = ['user']

    licenses = forms.ModelMultipleChoiceField(queryset=License.objects.all(), widget=forms.CheckboxSelectMultiple)
    driving_licenses = forms.ModelMultipleChoiceField(queryset=DrivingLicense.objects.all(), widget=forms.CheckboxSelectMultiple)

class CompanyProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        #fields = '__all__'
        fields = ['phone_number', 'address','websiteUrl', 'facebookUrl','explain',"vd_no",]
        exclude = ['user']