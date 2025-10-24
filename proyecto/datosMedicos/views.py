from django.shortcuts import render, redirect
from datosMedicos.models import DatosPaciente, Usuario

#----------------------------------| Zona Login |---------------------------------------

def login(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        con = request.POST.get('contraseña')
        
        try:
            usuario = Usuario.objects.get(rut=rut, contraseña=con)
            request.session['usuario_rut'] = usuario.rut
            request.session['usuario_nombre'] = usuario.nombre
            request.session['rol_nombre'] = usuario.rol.nombre
            
            if usuario.rol.nombre == 'cordinador':
                return redirect('menu_cordinador')
            elif usuario.rol.nombre == 'medico':
                return redirect('menu_medico')
            elif usuario.rol.nombre == 'paramedico':
                return redirect('formulario')
            else:
                return redirect('menu_default')

        except Usuario.DoesNotExist:
            return render(request, 'login.html', {'error': 'RUT o contraseña incorrectos'})
    
    return render(request, 'login.html')

def menu_cordinador(request):
    if 'usuario_id' not in request.session:
        return redirect('login')
    
    # Verificar que sea supervisor
    if request.session.get('rol_nombre') != 'cordinador':
        return redirect('menu')
    
    return render(request, 'menu_cordinador.html')

def menu_default(request):
    #if 'usuario_id' not in request.session:
    #    return redirect('login')
    
    # Verificar que sea paramedico
    #if request.session.get('rol_nombre') != 'admin':
    #    return redirect('menu')
    return render(request, 'menu.html')

def menu_paramedico(request):
    if 'usuario_id' not in request.session:
        return redirect('login')
    
    # Verificar que sea paramedico
    if request.session.get('rol_nombre') != 'paramedico':
        return redirect('login')


def sesion(request):
    usuario_rut = request.session.get('usuario_rut')
    usuario_nombre = request.session.get('usuario_nombre')
    
    return render(request, 'login', {
        'usuario_rut': usuario_rut,
        'usuario_nombre': usuario_nombre
    })

def logout_view(request):
    # Eliminar los datos de sesion
    request.session.flush()
    return redirect('login')

#----------------------------------| Formulario y Procesado |---------------------------------------

def formulario(request):
    # Si el Usuario no esta login entonces lo redirige a la pagina de login
    # if 'usuario_rut' not in request.session:
    #     return redirect('login')
    
    # try:
    #     usuario = Usuario.objects.get(rut=request.session['usuario_rut'])
    # except Usuario.DoesNotExist:
    #     request.session.flush()
    #     return redirect('login')
    
    return render(request, 'formularioHospital.html')


def procesado(request):
    if 'usuario_rut' not in request.session:
        return redirect('login')
    
    #Variables que se usaran
    pre = request.POST['prevision']
    gen = request.POST['genero']
    eda = int(request.POST['edad'])
    der = request.POST['derivacion']
    ale = request.POST['Alergia']
    fre = request.POST['frecuenciaCardiaca']
    art = request.POST['precionArterial']
    
    # Algunos de los siguientes datos se agregan en el hospital o despues
    rut = request.POST['rut']
    nom = request.POST['nombre']
    tem = request.POST['temperatura']
    san = request.POST['tipoDeSangre']
    cro = request.POST['tratamientoCronico']
    tel = request.POST['telefono']
    
    dp = DatosPaciente(
        prevision = pre,
        genero = gen,
        edad = eda,
        derivacion = der,
    )
    
    dp.save()
    
    datos = {'r':'Datos Enviados Correctamente'}
    return render(request, 'procesado.html', datos)
