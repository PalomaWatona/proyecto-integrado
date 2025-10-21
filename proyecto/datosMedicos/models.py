from django.db import models

# Se puede usar models.TextField() para que el campo sea obligatorio
# blank: Permite que el campo este vacio | null: Pone el campo en NULL en la base de datos
# Si se ponen ambos se puede dejar vacio el campo y en la base de datos queda como NULL
# Se puede usar on_delete=models. para diferentes tipos de borrado en la base de datos como:
# CASCADE:  Borra todo lo relacionado   | PROTECT: No deja borrar si hay relaciones
# SET_NULL: Pone NULL en las relaciones | SET_DEFAULT: Pone valor por defecto

class DatosPaciente(models.Model):
    prevision = models.CharField(max_length=50, blank=True)
    genero = models.CharField(max_length=10)
    edad = models.IntegerField()
    derivacion = models.CharField(max_length=50, blank=True)
    evaluacion = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    
    Alergia = models.CharField(max_length=50, blank=True)
    motivoConsulta = models.CharField(max_length=50, blank=True)
    frecuenciaCardiaca = models.CharField(max_length=50)
    signosVitales = models.CharField(max_length=50)
    temperatura = models.CharField(max_length=50)
    diabetes = models.CharField(max_length=20)
    azucarEnSangre = models.CharField(max_length=10)
    precionArterial = models.CharField(max_length=50)

    
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
    
    
class Roles(models.Model):
    nombre = models.CharField(max_length=50)
    
    
class Usuario(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    contraseña = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    rol = models.ForeignKey(Roles, on_delete=models.PROTECT)











