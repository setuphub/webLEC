from django.db import models
from django.contrib.auth.models import User

# Create your models here.

ROL_CHOICES = [
    ('JE', 'Jefe de Equipo'),
    ('RP', 'Representante'),
    ('PV', 'Portavoz'),
    ('PI', 'Piloto') 
]

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
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, null = True)
    rol = models.CharField( max_length=25, choices=ROL_CHOICES, default = 'JE') #si es piloto,jefe de  equipo,representante,etc.
    imagen_perfil = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None, blank= True, null = True)
    confirmacion_activacion = models.BooleanField(default = False)
    baja = models.DateTimeField( auto_now=False, auto_now_add=False, null = True, blank = True)



    def __str__(self):
        return self.user.username

    class Meta:
        db_table ='usuario'
        managed = True
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


