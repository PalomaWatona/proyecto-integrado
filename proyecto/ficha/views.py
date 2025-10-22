from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import redirect
from ficha.models import Usuario
import hashlib



def redir(request):
    if request.session.get('userid'):
        return redirect('menu')
    else:
        return redirect('login')

def menu(request):
    userid = request.session.get('userid')
    if not userid:
        datos = {'r': 'Debe iniciar sesión para ingresar al menú'}
        return redirect('login')  # login view will show datos if needed

    usuario = get_object_or_404(Usuario, pk=userid)
    datos = {'usuario': usuario}

    rol = (usuario.rol or '').lower()
    if rol == 'admin':
        return render(request, 'menuA.html', datos)
    elif rol == 'operador':
        return render(request, 'menuB.html', datos)
    else:
        datos = {'r': 'Rol no autorizado'}
        return render(request, 'index.html', datos)


def iniciarSesion(request):
    if request.method == 'POST':
        nom = request.POST['nombre']
        con = request.POST['contraseña']
        has = hashlib.md5(con.encode('utf-8')).hexdigest()
        try:
            usuario = Usuario.objects.get(nombre=nom, contraseña=has)
        except Usuario.DoesNotExist:
            datos = {'r': 'Error en el usuario y/o contraseña'}
            return render(request, 'index.html', datos)

        request.session['estadoSesion'] = True
        request.session['username'] = usuario.nombre.upper()
        request.session['userid'] = usuario.id
        request.session['rol'] = (usuario.rol or '').upper()

        # Redirect to menu (URL named 'menu'); menu() will fetch the usuario and render proper template
        return redirect('menu')
    else:
        datos = {'r': 'Error en el envio de los datos'}
        return render(request, 'index.html', datos)


def cerrarSesion(request):
    request.session.pop('estadoSesion', None)
    request.session.pop('username', None)
    request.session.pop('userid', None)
    request.session.pop('rol', None)
    request.session.flush()

    datos = {'r': 'Sesion cerrada correctamente!'}
    return render(request, 'index.html', datos)