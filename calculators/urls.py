from django.urls import path
from .views import BMRCalculationView

urlpatterns = [
    path('<str:equation>/', BMRCalculationView.as_view(), name='bmr-calculation'),
]
