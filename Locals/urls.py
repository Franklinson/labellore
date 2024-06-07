from django.urls import path
from . import views


urlpatterns = [
    path('locals/<int:pk>/', views.Locals, name='local-food'),
    path('locals/', views.foods, name='foods'),
]