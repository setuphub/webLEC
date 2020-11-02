from django.urls import path

from . import views
from usuarios.views import registro, login, logout

urlpatterns = [
    path('', views.index, name='index'),
    path('login', login, name='login'),
    path('logout',logout, name='logout'),
    path('blog/articulo/<str:id>', views.entrada, name='post')
    #path('registro', registro, name='registro')
]