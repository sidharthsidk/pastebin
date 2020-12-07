from django.urls import path
from .views import *

urlpatterns=[
    path('login/',user_login,name='login'),
    path('register/',register, name='register'),
    path('logout/',staff_logout,name='logout'),

]