from django.http import request
from django.urls import path
from . import views


app_name = 'marine'

urlpatterns = [
    path('', views.home, name=''),
]