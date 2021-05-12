from django.shortcuts import render
from rest_framework import generics
from tareas.models import Tarea
from .serializers import TareaSerializer

# Create your views here.

class TareaAPIView(generics.ListAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
