from django.db import models

class DatosP(models.Model):
    prevision = models.CharField(max_length=50)
    accidentelaboral = models.CharField(max_length=3)
    genero = models.CharField(max_length=10)
    edad = models.IntegerField()
    comorbilidades = models.CharField(max_length=50)
    funcionalidad = models.CharField(max_length=50)
    derivacion = models.CharField(max_length=50)
    evaluacion = models.CharField(max_length=50)
    Alergia = models.CharField(max_length=50)
    MotivoConsulta = models.CharField(max_length=50)
    frecuenciaC = models.CharField(max_length=50)
    temperatura = models.CharField(max_length=50)

class Fichas(models.Model):
    prevision = models.CharField(max_length=50)
    accidentelaboral = models.CharField(max_length=3)
    genero = models.CharField(max_length=10)
    edad = models.IntegerField()
    comorbilidades = models.CharField(max_length=50)
    funcionalidad = models.CharField(max_length=50)
    derivacion = models.CharField(max_length=50)
    evaluacion = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)
    Alergia = models.CharField(max_length=50)
    MotivoConsulta = models.CharField(max_length=50)
    frecuenciaC = models.CharField(max_length=50)
    temperatura = models.CharField(max_length=50)
    