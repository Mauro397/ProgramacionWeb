from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("",inicio, name="Inicio"),
    path("gimnasio/",gimnasio,name="Gimnasios"),
    path("maquina/",maquina,name="Maquinas"),
    path("entrenador",entrenador,name="Entrenadores"),
    path("buscarEntrenador", busquedaEntrenador, name="BuscarEntrenador"),
    path("resultados/", resultados, name="ResultadosObtenidos"),
    path("buscarMaquina/",busquedaMaquina,name="BuscarMaquina"),
    path("resultadosMaquina/",resultadosMaquina,name="ResultadosObtenidosMaquinas"),
    path("buscarGimnasio/",busquedaGimnasio,name="BuscarGimnasio"),
    path("resultadosGimnasio/",resultadosGimnasio,name="RestuladosObtenidosGimnasios"),

    #CRUD de gimnasios
    path("gimnasio/list/", ListaGimnasio.as_view(),name="GimnasiosLeer"),
    path("gimnasio/<int:pk>",DetalleGimnasio.as_view(),name="GimnasiosDetalle"),
    path("gimnasio/crear/",CrearGimnasio.as_view(),name="GimnasiosCrear"),
    path("gimnasio/editar/<int:pk>",ActualizarGimnasio.as_view(),name="GimnasiosEditar"),
    path("gimnasio/borrar/<int:pk>",BorrarGimnasio.as_view(),name="GimnasiosBorrar"),

    #CRUD de maquinas
    path("leerMaquinas/", leerMaquinas,name="MaquinasLeer"),
    path("crearMaquinas/",crearMaquina, name="MaquinasCrear"),
    path("eliminarMaquinas/<maquinaNombre>/",eliminarMaquinas,name="MaquinasEliminar"),
    path("editarMaquinas/<maquinaNombre>/",editarMaquinas,name="MaquinasEditar"),

    #CRUD de entrenadores
    path("leerEntrenadores/", leerEntrenadores,name="EntrenadoresLeer"),
    path("crearEntrenadores/",crearEntrenador, name="EntrenadoresCrear"),
    path("eliminarEntrenadores/<entrenadorNombre>/",eliminarEntrenadores,name="EntrenadoresEliminar"),
    path("editarEntrenadores/<entrenadorNombre>/",editarEntrenadores,name="EntrenadoresEditar"),
]