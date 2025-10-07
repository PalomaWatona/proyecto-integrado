from django.shortcuts import render

def formulario02(request):
    return render(request, 'formularioHospital.html')

def login(request):
    return render(request, 'login.html')

def formulario(request):
    return render(request, 'formulario.html')

def procesado(request):
    #Variables que se usaran
    pre = request.POST['prevision']
    act = request.POST['actlaboral']
    gen = request.POST['genero']
    eda = int(request.POST['edad'])
    com = request.POST['comorbilidades']
    fun = request.POST['funcionalidad']
    der = request.POST['derivacion']
    eva = request.POST['evaluacion']
    
    return render(request, 'procesado.html')

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
#