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
            # Mensaje de Usuario no encontrado
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
    # if 'usuario_id' not in request.session:
    #    return redirect('login')
    
    # Verificar que sea paramedico
    # if request.session.get('rol_nombre') != 'admin':
    #    return redirect('menu')
    return render(request, 'menu.html')

def menu_paramedico(request):
    if 'usuario_id' not in request.session:
        return redirect('login')
    
    # Verificar que sea paramedico
    if request.session.get('rol_nombre') != 'paramedico':
        return redirect('login')


def sesion(request):
    # Datos de Sesion
    usuario_rut = request.session.get('usuario_rut')
    usuario_nombre = request.session.get('usuario_nombre')
    
    return render(request, 'login', {'usuario_rut': usuario_rut, 'usuario_nombre': usuario_nombre})

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
    nom = request.POST['nombre']
    gen = request.POST['genero']
    eda = int(request.POST['edad']) # Implementar opciones de Niño, Joven, Adulto, Adulto Mayor
    fre = request.POST['frecuenciaCardiaca']
    vit = request.POST['signosVitales']
    art = request.POST['precionArterial']
    tem = request.POST['temperatura']
    ale = request.POST['Alergia']
    
    # Algunos de los siguientes datos se agregan en el hospital o despues
    com = request.POST['comorbilidades']
    rut = request.POST['rut']
    pre = request.POST['prevision']
    mot = request.POST['motivoConsulta']
    lic = request.POST['azucarEnSangre'] #Azucar En Sangre, solo se vea si es Diabetico
    san = request.POST['tipoDeSangre']
    cro = request.POST['tratamientoCronico']
    tel = request.POST['telefono']
    der = request.POST['derivacion']
    eva = request.POST['evaluacion']
    
    # tratamientos cronicos,temperatura rectar o axilar (opcion)
    # Cuando es translado de arta complejidad va con un profesional acargo
    # El hospital usa el sistema fonendo
    
    
    dp = DatosPaciente(
        prevision = pre,
        genero = gen,
        edad = eda,
        derivacion = der,
        evaluacion = eva
    )
    
    dp.save()
    
    datos = {'r':'Datos Enviados Correctamente'}
    return render(request, 'procesado.html', datos)


#----------------------------------| Pendientes |---------------------------------------

# ----- Explicaciones -----
# Despues de enviar el formulario dirigir a la pagina de menu
#

# ----- Por hacer (General) -----
# Boton para imprimir y descargar en formato excel

# Que se pueda ver la hora de envio del formulario y que la persona vio la ficha
# Crear Boton de 3 lineas para aparecer y esconder Inicio y Formulario
# Crear Pagina Historial de Formularios
# Crear Pagina Historial de Acciones (Login, Envio de Formularios)
# Crear Pagina Menu para el Paramedico 
# Crear Pagina Menu para el Medico
# Notificacion de Nuevos Formularios
# Hacer Pagina del Menu
# Tic de Formulario Visto
# Pagina para el Listado del formulario o para ver el formulario
# Boton Logout
# Boton Ver Perfil y Pagina del perfil de Usuario
# Poner Diabetes y Hypertension como opciones (Comorbilidades mas comunes)
# Funciona para Encriptar Contraseñas
# 
