from django.db import models

class TertuliaForm(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField(max_length=100, unique=True)
    numero_telefono = models.CharField(max_length=12, blank=True)
    nombre_tertulia = models.CharField(max_length=150)
    tertulia_folio_id =models.IntegerField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
