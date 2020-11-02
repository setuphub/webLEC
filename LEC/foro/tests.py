from django.test import TestCase

# Create your tests here.

class Hilo(models.Model):
    """Model definition for Hilo."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Hilo."""

        verbose_name = 'Hilo'
        verbose_name_plural = 'Hilos'

    def __str__(self):
        """Unicode representation of Hilo."""
        pass

class POST(models.Model):
    """Model definition for POST."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for POST."""

        verbose_name = 'POST'
        verbose_name_plural = 'POSTs'

    def __str__(self):
        """Unicode representation of POST."""
        pass

