from django.urls import path
from main.views import BweightView,SignUpView
from django.contrib.auth import views as auth_views
from main import forms

app_name='main'
urlpatterns = [

    path('', BweightView.as_view(),name='home'),
    path('login/',auth_views.LoginView.as_view(template_name='main/login.html',form_class=forms.AuthenticationForm,),name="login",),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/',SignUpView.as_view(),name='signup'),
]