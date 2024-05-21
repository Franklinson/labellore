from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('labels/', views.labels, name='labels'),
    path('labels/<int:pk>/', views.label, name='label'),
    # path('nutrients/', views.nutrients, name='nutrients'),
    # path('nutrients/<int:pk>/', views.nutrient, name='nutrient'),
]