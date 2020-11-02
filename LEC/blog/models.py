from django.db import models
from usuarios.models import Usuario

# Create your models here.

CATEGORIAS  = [
    ('GTS', 'Gran Turismo Sport'),
    ('GT7', 'Gran Turismo 7'),
    ('IR', 'iRacing'),
    ('PC2', 'Project Cars 2'),
    ('PC3', 'Project Cars 3'),
    ('RD4', 'Ride 4'),
    ('ATM', 'Automobilista 2'),
    ('RFC2', 'rFactor 2'),
    ('SR', 'SimRacing')
]

class Entrada(models.Model):
    """Model definition for Post."""

    # Define fields here

    titulo = models.CharField( blank=False, max_length=50, unique_for_date="fecha_creacion")
    subtitulo = models.CharField( blank=False, max_length=75)
    imagen = models.ImageField( blank=False, upload_to='%Y/%m/%d/', height_field=None, width_field=None, max_length=None)
    cuerpo = models.TextField( blank=False, )
    categoria = models.CharField( blank=False, max_length=50, choices=CATEGORIAS)
    etiquetas = models.CharField( blank=False, max_length=50)
    fecha_creacion = models.DateTimeField( auto_now_add=True)
    fecha_modificado = models.DateTimeField( auto_now_add=True)
    fecha_eliminado = models.DateTimeField( blank = True, null = True, auto_now_add=False)
    creado_por = models.ForeignKey(Usuario, blank=False, verbose_name="Creado por", on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        get_latest_by = "-fecha_modificado"
        ordering = ['-fecha_modificado']
        indexes = [models.Index(fields=['creado_por'], name="creador_por")]

    def __str__(self):
        """Unicode representation of Post."""
        return self.titulo
