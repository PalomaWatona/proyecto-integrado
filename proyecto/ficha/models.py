from django.db import models

    
class Fichas(models.Model):
    prevision = models.CharField(max_length=50)
    genero = models.CharField(max_length=10)
    edad = models.IntegerField()
    derivacion = models.CharField(max_length=50)
    evaluacion = models.CharField(max_length=50)
    Alergia = models.CharField(max_length=50)
    motivoConsulta = models.CharField(max_length=50)
    frecuenciaCardiaca = models.CharField(max_length=50)
    signosVitales = models.CharField(max_length=50)
    temperatura = models.CharField(max_length=50)
    diabetes = models.CharField(max_length=50)
    azucarEnSangre = models.CharField(max_length=50)
    precionArterial = models.CharField(max_length=50)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    
    
    
    
class Usuario(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    contraseña = models.CharField(max_length=100)
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    rol = models.CharField(max_length=20)