from django.shortcuts import render
from ficha.models import Usuario
import hashlib

def index(request):
    return render(request, 'index.html')

def menu(request):
    try:
        estado = request.session['estadoSesion']
        nombre =  request.session['nomUsuario']
        
        if estado is True:
            datos = {'nomUsuario':nombre}
            if nombre == 'OPERADOR':
                return render(request, 'menuA.html', datos)
            elif nombre == 'ADMIN':
                return render(request, 'menuB.html', datos)
            else:
                datos = {'r':'Error en el usuario'}
                return render(request, 'index.html', datos)
        else:
            datos = {'r':'Debe iniciar sesion para ingresar al menu!'}
            return render(request, 'index.html', datos)
    except:
        datos = {'r':'Debe iniciar sesion para ingresar al menu!'}
        return render(request, 'index.html', datos)        

def iniciarSesion(request):
    if request.method == 'POST':
        nom = request.POST['nombre']
        con = request.POST['contraseña']
        has = hashlib.md5(con.encode('utf-8')).hexdigest()
        comprobar = Usuario.objects.filter(nombre = nom, contraseña = has)

        if comprobar:
            request.session['estadoSesion'] = True
            request.session['nomUsuario'] = nom.upper()
            datos = {'nomUsuario':nom.upper()}
            if nom.upper() == 'OPERADOR':
                return render(request, 'menuA.html', datos)
            elif nom.upper() == 'ADMIN':
                return render(request, 'menuB.html', datos)
            else:
                datos = {'r':'Error en el usuario'}
                return render(request, 'index.html', datos)
        else:
            datos = {'r':'Error en el usuario y/o contraseña'}
            return render(request, 'index.html', datos)
    else:
        datos = {'r':'Error en el envio de los datos'}
        return render(request, 'index.html', datos)

def cerrarSesion(request):
    try:
        del request.session['estadoSesion']
        del request.session['nomUsuario']
        
        datos = {'r':'Sesion cerrada correctamente!'}
        return render(request, 'index.html', datos)
    except:
        datos = {'r':'La sesion está cerrada!'}
        return render(request, 'index.html', datos)