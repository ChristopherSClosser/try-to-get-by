"""Intell urls."""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mtx', views.front_input, name='finput')
]
