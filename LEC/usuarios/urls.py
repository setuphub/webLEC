from django.urls import path

from . import views

app_name= 'usuarios'

urlpatterns = [
    path('registro', views.registro, name='registro'),
    path('sent/', views.activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name="activate"),
]