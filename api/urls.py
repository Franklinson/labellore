from django.urls import path
from . import views


urlpatterns = [
    path('getfood', views.getfood, name='getfood'),
    
]