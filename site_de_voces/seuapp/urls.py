from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cafe/', views.cafe, name='cafe'),
    path('nova_pagina/', views.cafe, name='cafe'),
]