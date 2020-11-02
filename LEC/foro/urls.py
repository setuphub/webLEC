from django.urls import path

from . import views

urlpatterns = [
    path('', views.foro, name='categorias'),
    path('foro/<str:Titulo>/', views.subcategoria, name='post')
    #path('registro', registro, name='registro')
]