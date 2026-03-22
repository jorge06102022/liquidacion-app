from django.db import models

# Create your models here.
from django.db import models

class Calculo(models.Model):
    salario = models.FloatField()
    fecha_ingreso = models.DateField()
    fecha_retiro = models.DateField()

    cesantias = models.FloatField(null=True, blank=True)
    intereses = models.FloatField(null=True, blank=True)
    prima = models.FloatField(null=True, blank=True)
    vacaciones = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)

    creado = models.DateTimeField(auto_now_add=True)