from django.urls import path

from . import views
from usuarios.views import registro, login

urlpatterns = [
    path('', views.index, name='index'),
    path('login', login, name='login')
    #path('registro', registro, name='registro')
]