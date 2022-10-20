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
    path("maquina/list/", ListaMaquina.as_view(),name="MaquinasLeer"),
    path("maquina/<int:pk>",DetalleMaquina.as_view(), name="MaquinasDetalle"),
    path("maquina/crear/",CrearMaquina.as_view(),name="MaquinasCrear"),
    path("maquina/editar/<int:pk>",ActualizarMaquina.as_view(),name="MaquinasEditar"),
    path("maquina/borrar/<int:pk>",BorrarMaquina.as_view(),name="MaquinasBorrar"),


    #CRUD de entrenadores
    path("entrenador/list/", ListaEntrenador.as_view(),name="EntrenadoresLeer"),
    path("entrenador/<int:pk>",DetalleEntrenador.as_view(), name="EntrenadoresDetalle"),
    path("entrenador/crear/",CrearEntrenador.as_view(),name="EntrenadoresCrear"),
    path("entrenador/editar/<int:pk>",ActualizarEntrenador.as_view(),name="EntrenadoresEditar"),
    path("entrenador/borrar/<int:pk>",BorrarEntrenador.as_view(),name="EntrenadoresBorrar"),
]