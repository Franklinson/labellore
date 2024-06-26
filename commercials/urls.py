from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('foods/', views.foods, name='foods'),
    path('foods/<int:pk>/', views.food_detail, name='food-detail'),
]