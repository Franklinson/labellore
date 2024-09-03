from django.urls import path
from . import views
# from .views import FoodDocumentView

urlpatterns = [
    path('', views.home, name='home'),
    path('foods/', views.foods, name='foods'),
    path('foods/<int:pk>/', views.food_detail, name='food-detail'),
    path('api/search/', views.search_food, name='search_food'),
]
