from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import redirect
from ficha.models import Usuario
from ficha.models import Fichas
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
        return redirect('login')

    usuario = get_object_or_404(Usuario, pk=userid)
    datos = {'usuario': usuario}

    rol = (usuario.rol or '').lower()
    if rol == 'admin':
        return render(request, 'menu_Admin.html', datos)
    elif rol == 'coordinador':
        return render(request, 'menu_Coordinador.html', datos)
    elif rol == 'paramedico':
        return render(request, 'menu_Paramedico.html', datos)
    else:
        datos = {'r': 'Rol no autorizado'}
        return render(request, 'login.html', datos)


def iniciarSesion(request):
    if request.method == 'POST':
        rut = request.POST['rut']
        con = request.POST['password']
        has = hashlib.md5(con.encode('utf-8')).hexdigest()
        try:
            usuario = Usuario.objects.get(rut=rut, contraseña=has)
        except Usuario.DoesNotExist:
            datos = {'r': 'Error en el usuario y/o contraseña'}
            return render(request, 'login.html', datos)

        request.session['estadoSesion'] = True
        request.session['username'] = usuario.nombre.upper()
        request.session['userid'] = usuario.id
        request.session['rol'] = (usuario.rol or '').upper()

        return redirect('menu')
    else:
        return render(request, 'login.html')


def cerrarSesion(request):
    request.session.pop('estadoSesion', None)
    request.session.pop('username', None)
    request.session.pop('userid', None)
    request.session.pop('rol', None)
    request.session.flush()
    return redirect('login')


def formulario(request):
    userid = request.session.get('userid')
    if not userid:
        datos = {'r': 'Debe iniciar sesión para ingresar al formulario'}
        return redirect('login')

    usuario = get_object_or_404(Usuario, pk=userid)
    datos = {'usuario': usuario}

    return render(request, 'formulario.html', datos)

def listado(request):
    userid = request.session.get('userid')
    if not userid:
        datos = {'r': 'Debe iniciar sesión para ingresar al listado'}
        return redirect('login')

    usuario = get_object_or_404(Usuario, pk=userid)
    datos = {'usuario': usuario}

    return render(request, 'Listado.html', datos)

def insertar(request):
    userid = request.session.get('userid')
    if not userid:
        datos = {'r': 'login requerido'}
        return redirect('login')
    
    usuario = get_object_or_404(Usuario, pk=userid)
    
    nompa = request.POST['txtnompa']
    apepa = request.POST['txtapepa']
    rutpa = request.POST['txtrutpa']
    rutme = usuario.rut
    eda = request.POST['txteda']
    tel = request.POST['txttel']
    gen = request.POST['cbogen']
    pre = request.POST['cbopre']
    mot = request.POST['txtmot']
    com = request.POST['txtcom']
    ale = request.POST['txtale']
    fre = request.POST['txtfre']
    tem = request.POST['txttem']
    pre = request.POST['txtpre']
    san = request.POST['cbosan']
    obs = request.POST['txtobs']


    ficha = Fichas(
        nombrepaciente=nompa,
        apellidopaciente=apepa,
        rutpaciente=rutpa,
        rutparamedico=rutme,
        edad=eda,
        telefono=tel,
        genero=gen,
        prevision=pre,
        motivoconsulta=mot,
        comorbilidades=com,
        alergias=ale,
        frecuenciacardiaca=fre,
        temperatura=tem,
        presionarterial=pre,
        tiposangre=san,
        observaciones=obs
    )
    ficha.save()

    return redirect('/menu/')

def listado(request):
    userid = request.session.get('userid')
    if not userid:
        datos = {'r': 'Debe iniciar sesión para ingresar al listado'}
        return redirect('login')

    usuario = get_object_or_404(Usuario, pk=userid)
    fichas = Fichas.objects.all()
    datos = {'usuario': usuario, 'fichas': fichas}

    return render(request, 'Listado.html', datos)

def eliminarficha(request, id):
    userid = request.session.get('userid')
    if not userid:
        datos = {'r': 'Debe iniciar sesión para eliminar una ficha'}
        return redirect('login')

    ficha = get_object_or_404(Fichas, pk=id)
    ficha.delete()

    return redirect('listado')

def verficha(request, id):
    userid = request.session.get('userid')
    if not userid:
        datos = {'r': 'Debe iniciar sesión para ver una ficha'}
        return redirect('login')

    usuario = get_object_or_404(Usuario, pk=userid)
    ficha = get_object_or_404(Fichas, pk=id)
    datos = {'usuario': usuario, 'ficha': ficha}

    return render(request, 'Ficha.html', datos)
    
    
    
    
    
    
    
    
    
    