from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Equipo(models.Model):
    """Model definition for Equipo."""

    # TODO: Define fields here

    nombre_equipo = models.CharField( max_length=50)
    abreviatura = models.CharField(max_length=50)
    email_equipo = models.EmailField(max_length=254)
    pilotos = models.ManyToManyField(User, through='Usuario') #foreign key con usuarios
    activo = models.BooleanField(default = False)
    fecha_creacion = models.DateTimeField( auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now_add=True)
    fecha_baja = models.DateTimeField(auto_now_add=False)

    class Meta:
        """Meta definition for Equipo."""
        db_table ='equipo'
        managed = True
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'

    def __str__(self):
        """Unicode representation of Equipo."""
        return self.nombre_equipo

class Usuario(models.Model):

    user = models.OneToOneField(User, verbose_name="usuario", on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    rol = models.CharField( max_length=50) #si es piloto,jefe de  equipo,representante,etc.
    imagen_perfil = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)
    registrado = models.DateTimeField( auto_now=False, auto_now_add=False)
    baja = models.DateTimeField( auto_now=False, auto_now_add=False)



    def __str__(self):
        return self.user.username

    class Meta:
        db_table ='usuario'
        managed = True
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class codigos_activacio_usuarios(models.Model):
    """Model definition for codigos_activacio_usuarios."""

    # TODO: Define fields here

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) 
    codigo = models.CharField( max_length=5)
    class Meta:
        """Meta definition for codigos_activacio_usuarios."""

        verbose_name = 'Codigo activacion'
        verbose_name_plural = 'Codigos de activacion'

    def __str__(self):
        """Unicode representation of codigos_activacio_usuarios."""
        return self.usuario.id, self.codigo
