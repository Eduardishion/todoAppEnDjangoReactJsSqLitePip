from django.urls import path
from .views import listarTodasLasTareasyCrearTarea,ActualizarEliminarTareas

urlpatterns = [

    path('<int:pk>/',ActualizarEliminarTareas.as_view(),name="ActualizarEliminarTareas"),
    path('',listarTodasLasTareasyCrearTarea.as_view(),name="listarTodasLasTareas"),        #Ruta para mostrar todos los registros metodo get y crear tarea son metodo post

]