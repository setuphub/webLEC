from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):

    user = models.OneToOneField(User, verbose_name="user", on_delete=models.CASCADE)
    equipo = models.CharField( max_length=50)
    status = models.CharField( max_length=50)#si es piloto,jefe de  equipo,representante,etc.
    imagen_perfil = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)
    activo = models.BooleanField()
    registrado = models.DateTimeField( auto_now=False, auto_now_add=False)
    baja = models.DateTimeField( auto_now=False, auto_now_add=False)



    def __str__(self):
        return self.user.username

    class Meta:
        db_table ='usuario'
        managed = True
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

