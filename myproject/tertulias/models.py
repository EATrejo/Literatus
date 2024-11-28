from django.db import models

# Create your models here.

class Tertulia(models.Model):
    tertulia_name = models.CharField(max_length=100)
    tertulia_banner = models.ImageField(default='fallback.png', blank=True)
    tertulia_description = models.TextField(max_length=250, blank=True)
    tertulia_address = models.CharField(max_length=250, blank=True, null=True)
    tertulia_horario = models.CharField(max_length=100)
    tertulia_fecha_de_inicio = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
    tertulia_sesiones =models.PositiveSmallIntegerField()
    tertulia_encargado_picture = models.ImageField(default='alonso.jpg', blank=True)
    tertulia_encargado = models.CharField(max_length=100)
    tertulia_lugares_disponibles = models.PositiveIntegerField(default=12)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.tertulia_name
