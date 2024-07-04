from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('password-reset/', password_reset_request_view, name='password-reset'),
    path('password-reset-confirm/<int:uidb64>/<str:token>/', password_reset_confirm_view, name='password-reset-confirm'),
]