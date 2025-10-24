from django.contrib import admin
from ficha.models import Usuario

class usuarioAdmin(admin.ModelAdmin):
    list_display = ['id','rut','nombre', 'contraseña','correo','rol']

admin.site.register(Usuario, usuarioAdmin)