from django.urls import path
from main.views import BweightView,SignUpView


urlpatterns = [

    path('', BweightView.as_view(),name='bwv'),
    path('signup/',SignUpView.as_view(),name='signup'),
]