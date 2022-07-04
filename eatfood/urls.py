from django.urls import path
from .views import login, register, index

app_name='login'

urlpatterns = [
    path('login/',login, name='login'),
    path('login/register/',register, name="register"),
    path('',index, name="index"),
]
