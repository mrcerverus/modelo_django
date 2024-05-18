from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True)
    marca = models.CharField(max_length=20, null=False, blank=False)
    modelo = models.CharField(max_length=20, null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)
    activo = models.BooleanField(default=False)

class Chofer(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    vehiculo_id = models.ForeignKey("Vehiculo", null=False, blank=False,on_delete=models.CASCADE)

class RegistroContabilidad(models.Model):
    fecha_compra = models.DateField(null=False)
    valor = models.FloatField(null=False)
    vechiculo_id = models.ForeignKey("Vehiculo", null=False, blank=False,on_delete=models.CASCADE)