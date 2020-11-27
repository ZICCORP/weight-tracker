from django.urls import path
from main.views import BweightView


urlpatterns = [
    path('', BweightView.as_view(),name='bwv'),
]