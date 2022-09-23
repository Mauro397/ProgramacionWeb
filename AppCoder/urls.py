from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("",inicio, name="Inicio"),
    path("gimnasio/",gimnasio,name="Gimnasios"),
    path("maquina/",maquina,name="Maquinas"),
    path("entrenador",entrenador,name="Entrenadores"),
    path("entrenadorFormulario/",entrenadorFormulario, name="FormularioEntrenador"),
    path("buscarEntrenador", busquedaEntrenador, name="BuscarEntrenador"),
    path("resultados/", resultados, name="ResultadosObtenidos"),
    path("maquinaFormulario/",maquinaFormulario, name="FormularioMaquina"),
    path("buscarMaquina/",busquedaMaquina,name="BuscarMaquina"),
    path("resultadosMaquina/",resultadosMaquina,name="ResultadosObtenidosMaquinas"),
    path("gimnasioFormulario/",gimnasioFormulario,name="FormularioGimnasio"),
    path("buscarGimnasio/",busquedaGimnasio,name="BuscarGimnasio"),
    path("resultadosGimnasio/",resultadosGimnasio,name="RestuladosObtenidosGimnasios"),
]