from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('cafe/', views.cafe, name='cafe'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('docad/', views.docad, name='docad'),
    path('dologin/', views.dologin, name='dologin'),
    path('perfil/', views.profile, name='perfil'),
    path('doupdate/', views.do_update, name='doupdate'),
    path('comentario/', views.comentario, name='comentario'),
    path('comentario/<int:id>/editar/',views.edit_coment, name='edit_coment'),
]