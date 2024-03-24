from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('viewnutrient', views.label_list, name='viewnutrient'),
]