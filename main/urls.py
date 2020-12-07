from django.urls import path
from main.views import BweightView,SignUpView,SignInView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from main import forms

app_name='main'
urlpatterns = [

    path('', TemplateView.as_view(template_name='main/home.html'),name='home'),
    path('weight/',BweightView.as_view(),name='weight'),
    path('login/',SignInView.as_view(),name="login",),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/',SignUpView.as_view(),name='signup'),
]