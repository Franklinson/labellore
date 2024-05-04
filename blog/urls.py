from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('<int:pk>/', views.blog, name='blog'),
    path('categories', views.categories, name='categories'),
    path('categories/<int:pk>/', views.category, name='category'),
]
