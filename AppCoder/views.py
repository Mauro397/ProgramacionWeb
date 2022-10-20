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


class ListaEntrenador(ListView):
    model = Entrenadores

class DetalleEntrenador(DetailView):
    
    model = Entrenadores

class CrearEntrenador(CreateView):

    model = Entrenadores
    succes_url = "/AppCoder/entrenador/list"
    fields = ["nombre","apellido","especialidad"]

class ActualizarEntrenador(UpdateView):
    
    model = Entrenadores
    succes_url = "/AppCoder/entrenador/list"
    fields = ["nombre","apellido","especialidad"]

class BorrarEntrenador(DeleteView):

    model = Entrenadores
    succes_url = "/AppCoder/entrenador/list"   


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

class ListaMaquina(ListView):
    model = Maquinas

class DetalleMaquina(DetailView):
    
    model = Maquinas

class CrearMaquina(CreateView):

    model = Maquinas
    succes_url = "/AppCoder/maquina/list"
    fields = ["nombre","zonaDeTrabajo","pesoMax"]

class ActualizarMaquina(UpdateView):
    
    model = Maquinas
    succes_url = "/AppCoder/maquina/list"
    fields = ["nombre","zonaDeTrabajo","pesoMax"]

class BorrarMaquina(DeleteView):

    model = Maquinas
    succes_url = "/AppCoder/maquina/list"

#Seccion Gimnasios

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


class ListaGimnasio(ListView):
    model = Gimnasio

class DetalleGimnasio(DetailView):
    
    model = Gimnasio

class CrearGimnasio(CreateView):

    model = Gimnasio
    succes_url = "/AppCoder/gimnasio/list"
    fields = ["nombre","fechaCreacion","localicacion"]

class ActualizarGimnasio(UpdateView):
    
    model = Gimnasio
    succes_url = "/AppCoder/gimnasio/list"
    fields = ["nombre","fechaCreacion","localicacion"]

class BorrarGimnasio(DeleteView):

    model = Gimnasio
    succes_url = "/AppCoder/gimnasio/list"


