from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.mail import send_mail


class CustomUserCreationForm(UserCreationForm):

    class Meta:

        model = get_user_model()
        fields = ('first_name','last_name','email','birth_date','gender',)
        widgets = {
            'birth_date':forms.SelectDateWidget
            }
    def send_mail(self):
        message = "Welcome {}".format(self.cleaned_data["email"])
        send_mail("Welcome to WeightTrack",message,"site@weighttrack.domain",[self.cleaned_data["email"]],fail_silently=True,)
            
