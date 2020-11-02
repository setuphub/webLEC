from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from usuarios.models import Usuario

# Create your models here.

class Comentario(models.Model):
    """Model definition for Comentario."""

    # TODO: Define fields here

    comentario = models.TextField(blank = True, null = True, unique_for_date = "fecha_creado")
    autor = models.OneToOneField(Usuario, verbose_name="autor_comentario", on_delete=models.CASCADE)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField( auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null = True)
    object_id = models.PositiveIntegerField(null = True)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        """Meta definition for Comentario."""

        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        get_latest_by = "-fecha_creado"
        ordering = ['-fecha_creado']

    def __str__(self):
        """Unicode representation of Comentario."""
        pass


class Post(models.Model):
    """Model definition for MODELNAME."""

    # TODO: Define fields here

    Titulo = models.CharField( max_length=50, unique_for_date = "fecha_creado", null = False, blank = False )
    autor = models.OneToOneField(Usuario, verbose_name="autor_post", on_delete=models.PROTECT, null = False)
    cuerpo = models.TextField(null = False, blank = False)
    comentarios = GenericRelation(Comentario)
    permitir_comentarios = models.BooleanField(default = True)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default = True, null = True)

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        get_latest_by = "-fecha_creado"
        ordering = ['-fecha_creado']

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.Titulo


class Subcategoria(models.Model):
    """Model definition for Post."""

    # TODO: Define fields here

    Titulo = models.CharField(max_length=50)
    Posts = models.ForeignKey(Post, verbose_name="Posts", on_delete=models.CASCADE, blank = True, null = True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Subcategoria'
        verbose_name_plural = 'Subcategoria'

    def __str__(self):
        """Unicode representation of Post."""
        return self.Titulo


class Categoria(models.Model):
    """Model definition for Hilo."""

    # TODO: Define fields here

    Titulo = models.CharField(max_length=50, unique = True)
    Subcategoria = models.ForeignKey("Subcategoria", verbose_name="Subcategoria", on_delete=models.CASCADE, blank = True, null= True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Hilo."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        """Unicode representation of Hilo."""
        return self.Titulo