from django.urls import path
from .views import *
urlpatterns = [
    path('supervisorsignup/',SupervisorRegister.as_view(),name='superreg'),
    path('normalsignup/',NormalRegister.as_view(),name = "normalreg"),
    path('login_user/',LoginUser.as_view(),name='login'),
]
