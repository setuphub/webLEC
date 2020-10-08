from django.urls import path

from . import views
from usuarios.views import registro

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    #path('registro', registro, name='registro')
]