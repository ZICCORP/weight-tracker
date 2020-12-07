from django.forms import ModelForm
from django import forms
from main.models import BodyWeight
from django.contrib.auth import authenticate

class BodyWeightForm(ModelForm):
    class Meta:
        model = BodyWeight
        fields = ['weight',]

class AuthenticationForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

    def __init__(self,request=None,*args,**kwargs):
        self.request =request
        self.user = None
        super().__init__(*args,**kwargs)

    def clean(self):
        email =self.cleaned_data.get("email")
        password =self.cleaned_data.get("password")
        if email is not None and password:
            self.user = authenticate(self.request,email=email,password=password)
            if self.user is None:
                raise forms.ValidationError("Invalid Email/Password combination.")
        return self.cleaned_data

    def get_user(self):
        return self.user



