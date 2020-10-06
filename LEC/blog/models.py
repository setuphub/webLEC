from django.db import models
#from usuarios.models import Usuario

# Create your models here.

class Post(models.Model):
    """Model definition for Post."""

    # Define fields here

    titulo = models.CharField( blank=False, max_length=50, unique_for_date="fecha_creacion")
    subtitulo = models.CharField( blank=False, max_length=75)
    imagen = models.ImageField( blank=False, upload_to=None, height_field=None, width_field=None, max_length=None)
    cuerpo = models.TextField( blank=False, )
    categoria = models.CharField( blank=False, max_length=50)
    etiquetas = models.CharField( blank=False, max_length=50)
    fecha_creacion = models.DateTimeField( auto_now=True, auto_now_add=True)
    fecha_modificado = models.DateTimeField( auto_now=True, auto_now_add=True)
    fecha_eliminado = models.DateTimeField( auto_now=False, auto_now_add=False)
    #creado_por = models.ForeignKey(Usuario, blank=False, verbose_name=_("Creado por"), on_delete=models.RESTRICT)

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'post'
        get_latest_by = "-fecha_modificado"
        ordering = ['-fecha_modificado']
        indexes = [models.Index(fields=['creado_por'], name="creador_por")]

    def __str__(self):
        """Unicode representation of Post."""
        return self
