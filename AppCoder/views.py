from this import d
from django.shortcuts import render
from AppCoder.forms import *
from AppCoder.models import *
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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

def leerEntrenadores(request):
    
    entrenador = Entrenadores.objects.all()

    contexto = {"Coach": entrenador}

    return render(request, "AppCoder/leerEntrenadores.html", contexto)

def crearEntrenador(request):

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

def eliminarEntrenadores(request, entrenadorNombre):

    entrenador = Entrenadores.objects.get(nombre=entrenadorNombre)
    entrenador.delete()

    entrenadores = Entrenadores.objects.all()

    contexto = {"Coach":entrenadores}

    return render(request, "AppCoder/leerEntrenadores.html", contexto)

def editarEntrenadores(request, entrenadorNombre):

    entrenador =  Entrenadores.objects.get(nombre=entrenadorNombre)

    if request.method =="POST": #Lo que ocurre si se le da al boton enviar

        formulario1 = EntrenadorFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            entrenador.nombre = info["nombre"]
            entrenador.apellido = info["apellido"]
            entrenador.especialidad = info["especialidad"]             

            entrenador.save()

            return render(request, "AppCoder/inicio.html")
    
    else:

        formulario1 = EntrenadorFormulario(initial={"nombre":entrenador.nombre,"apellido":entrenador.apellido,
        "especialidad":entrenador.especialidad})


    return render(request, "AppCoder/editarEntrenadores.html", {"form1":formulario1,"nombre":entrenadorNombre})    


#Seccion Maquinas


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

def leerMaquinas(request):
    
    maquinas = Maquinas.objects.all()

    contexto = {"Maquinaria": maquinas}

    return render(request, "AppCoder/leerMaquinas.html", contexto)


def crearMaquina(request):

    if request.method =="POST": #Lo que ocurre si se le da al boton enviar

        formulario2 = MaquinasFormulario(request.POST)

        if formulario2.is_valid():

            info = formulario2.cleaned_data

            maquina = Maquinas(nombre=info["nombre"], zonaDeTrabajo=info["zonaDeTrabajo"], pesoMax=info["pesoMax"])

            maquina.save()

            return render(request, "AppCoder/inicio.html")
    
    else:

        formulario2 = MaquinasFormulario()


    return render(request, "AppCoder/maquinasFormulario.html", {"form2":formulario2})


def eliminarMaquinas(request, maquinaNombre):

    maquina = Maquinas.objects.get(nombre=maquinaNombre)
    maquina.delete()

    maquinas = Maquinas.objects.all()

    contexto = {"Maquinaria":maquinas}

    return render(request, "AppCoder/leerMaquinas.html", contexto)


def editarMaquinas(request, maquinaNombre):

    maquina = Maquinas.objects.get(nombre=maquinaNombre)

    if request.method =="POST": #Lo que ocurre si se le da al boton enviar

        formulario2 = MaquinasFormulario(request.POST)

        if formulario2.is_valid():

            info = formulario2.cleaned_data

            maquina.nombre = info["nombre"]
            maquina.zonaDeTrabajo = info["zonaDeTrabajo"]
            maquina.pesoMax = info["pesoMax"]  

            maquina.save()

            return render(request, "AppCoder/inicio.html")
    
    else:

        formulario2 = MaquinasFormulario(initial={"nombre":maquina.nombre, "zonaDeTrabajo":maquina.zonaDeTrabajo,
        "pesoMax":maquina.pesoMax})


    return render(request, "AppCoder/editarMaquinas.html", {"form2":formulario2,"nombre":maquinaNombre})    

 

#Seccion Gimnasios

def crearGimnasios(request):

    if request.method =="POST": #Lo que ocurre si se le da al boton enviar

        formulario3 = GimnasiosFormulario(request.POST)

        if formulario3.is_valid():

            info = formulario3.cleaned_data

            Gimnasios1 = Gimnasio(nombre=info["nombre"], fechaCreacion=info["fechaCreacion"], localicacion=info["Localicacion"])

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

def leerGimnasios(request):
    
    gimnasios = Gimnasio.objects.all()

    contexto = {"Gym": gimnasios}

    return render(request, "AppCoder/leerGimnasios.html", contexto)


def eliminarGimnasios(request, gimnasioNombre):

    gimnasio = Gimnasio.objects.get(nombre=gimnasioNombre)
    gimnasio.delete()

    gimnasios = Gimnasio.objects.all()

    contexto = {"Gym":gimnasios}

    return render(request, "AppCoder/leerGimnasios.html", contexto)

def editarGimnasios(request, gimnasioNombre):

    gimnasio = Gimnasio.objects.get(nombre=gimnasioNombre)

    if request.method =="POST": #Lo que ocurre si se le da al boton enviar

        formulario3 = GimnasiosFormulario(request.POST)

        if formulario3.is_valid():

            info = formulario3.cleaned_data

            gimnasio.nombre = info["nombre"]
            gimnasio.fechaCreacion = info["fechaDeCreacion"]
            gimnasio.localicacion = info["localizacion"]

            gimnasio.save()

            return render(request, "AppCoder/inicio.html")
    
    else:

        formulario3 = GimnasiosFormulario(initial={"nombre":gimnasio.nombre, "fechaDeCreacion":gimnasio.fechaCreacion,
        "localizacion":gimnasio.localicacion})


    return render(request, "AppCoder/editarGimnasios.html", {"form3":formulario3, "nombre":gimnasioNombre})



