from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login 

urlpatterns = [
    path('', login, name='login'), 
]
