from django.shortcuts import render
from datosMedicos.models import DatosP

def formulario02(request):
    return render(request, 'formularioHospital.html')

def login(request):
    return render(request, 'login.html')

def formulario(request):
    return render(request, 'formulario.html')

def procesado(request):
    #Variables que se usaran
    pre = request.POST['prevision']
    gen = request.POST['genero']
    eda = int(request.POST['edad'])
    der = request.POST['derivacion']
    eva = request.POST['evaluacion']
    ale = request.POST['Alergia']
    mot = request.POST['MotivoConsulta']
    fre = request.POST['frecuenciaC']
    tem = request.POST['temperatura']
    # Falta hacer Diabetes, tratamientos cronicos, signos vitales, licemia (azucar en sangre), precion arterial, temperatura rectar o axilar
    #
    # Se elimino la comorbilidad por que no se sabra si tiene otra enfermedad
    # Cuando es translado de arta complejidad va con un prefecional acargo
    # El hospital usa el sistema fonendo
    
    
    dp = DatosP(
        prevision = pre,
        genero = gen,
        edad = eda,
        derivacion = der,
        evaluacion = eva
    )
    
    dp.save()
    
    datos = {'r':'Datos Enviados Correctamente'}
    return render(request, 'procesado.html', datos)



# Explicaciones:
# Despues de enviar el formulario dirigir a la pagina de menu
#

# Por hacer (General): 
# Boton para imprimir y descargar en formato excel
# Que se pueda ver la hora de envio del formulario y que la persona vio la ficha
# Crear 3 lineas para aparecer y esconder Inicio y Formulario
# Crear Historial de Formularios
# Crear Historial de Loggin
# Notificacion de Nuevos Formularios
# Hacer Pagina del Menu
# Tic de Formulario Visto
# Pagina para el Listado del formulario o para ver el formulario