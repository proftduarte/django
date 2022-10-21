from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('cafe/', views.cafe, name='cafe'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('docad/', views.docad, name='docad'),
    path('dologin/', views.dologin, name='dologin'),
]