from django.shortcuts import render
from AppCoder.forms import *
from AppCoder.models import *
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request,"AppCoder/inicio.html")

def gimnasio(request):
    return render(request,"AppCoder/gimnasio.html")

def maquina(request):
    return render(request,"AppCoder/maquina.html")

def entrenador(request):
    return render(request,"AppCoder/entrenador.html")

#Seccion Entrenadores

def entrenadorFormulario(request):

    if request.method =="POST": #Lo que ocurre si se le da al boton enviar

        formulario1 = EntrenadorFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            entrenador = Entrenadores(nombre=info["nombre"], apellido=info["apellido"], especialidad=info["especialidad"])

            entrenador.save()

            return render(request, "AppCoder/inicio.html")
    
    else:

        formulario1 = EntrenadorFormulario()


    return render(request, "AppCoder/entrenadorFormulario.html", {"form1":formulario1})


def busquedaEntrenador(request):

    return render(request, "AppCoder/inicio.html")

def resultados(request):

    if request.GET["entrenador"]:

        entrenador=request.GET["entrenador"]
        entrenadores=Entrenadores.objects.filter(nombre__icontains=entrenador)

        return render(request, "AppCoder/inicio.html", {"entrenadores":entrenadores,"entrenador":entrenador})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)


#Seccion Maquinas

def maquinaFormulario(request):

    if request.method =="POST": #Lo que ocurre si se le da al boton enviar

        formulario2 = MaquinasFormulario(request.POST)

        if formulario2.is_valid():

            info = formulario2.cleaned_data

            Maquina = Maquinas(nombre=info["nombre"], zonaDeTrabajo=info["zonaDeTrabajo"], pesoMax=info["pesoMax"])

            Maquina.save()

            return render(request, "AppCoder/inicio.html")
    
    else:

        formulario2 = MaquinasFormulario()


    return render(request, "AppCoder/maquinasFormulario.html", {"form2":formulario2})

def busquedaMaquina(request):

    return render(request, "AppCoder/inicio.html")

def resultadosMaquina(request):

    if request.GET["maquina"]:

        maquina=request.GET["maquina"]
        maquinas=Maquinas.objects.filter(nombre__icontains=maquina)

        return render(request, "AppCoder/inicio.html", {"maquinas":maquinas,"maquina":maquina})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)


def busquedaEntrenador(request):

    return render(request, "AppCoder/inicio.html")

def resultados(request):

    if request.GET["entrenador"]:

        entrenador=request.GET["entrenador"]
        entrenadores=Entrenadores.objects.filter(nombre__icontains=entrenador)

        return render(request, "AppCoder/inicio.html", {"entrenadores":entrenadores,"entrenador":entrenador})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)


#Seccion Maquinas

def gimnasioFormulario(request):

    if request.method =="POST": #Lo que ocurre si se le da al boton enviar

        formulario3 = GimnasiosFormulario(request.POST)

        if formulario3.is_valid():

            info = formulario3.cleaned_data

            Gimnasios1 = Gimnasio(nombre=info["nombre"], fechaCreacion=info["fechaCreacion"], Localicacion=info["Localicacion"])

            Gimnasios1.save()

            return render(request, "AppCoder/inicio.html")
    
    else:

        formulario3 = GimnasiosFormulario()


    return render(request, "AppCoder/gimnasiosFormulario.html", {"form3":formulario3})

def busquedaGimnasio(request):

    return render(request, "AppCoder/inicio.html")

def resultadosGimnasio(request):

    if request.GET["gimnasio"]:

        gimnasio=request.GET["gimnasio"]
        gimnasios=Gimnasio.objects.filter(nombre__icontains=gimnasio)

        return render(request, "AppCoder/inicio.html", {"gimnasios":gimnasios,"gimnasio":gimnasio})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)