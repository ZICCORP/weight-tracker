from django.urls import path
from main.views import BweightView,SignUpView
from django.contrib.auth import views as auth_views
from main import forms

urlpatterns = [

    path('', BweightView.as_view(),name='bwv'),
    path('login/',auth_views.LoginView.as_view(template_name='main/login.html',form_class=forms.AuthenticationForm,),name="login",),
    path('logout',auth_views.LogoutView.as_view(),name='logout'),
    path('change_password',auth_views.PasswordChangeView.as_view(template_name='main/change_password.html',success_url='done/'),name='change_password'),
    path('done/',auth_views.PasswordChangeDoneView.as_view(template_name='main/done.html'),name='done'),
    path('signup/',SignUpView.as_view(),name='signup'),
]