from django.shortcuts import render

from django.views.generic import ListView
# Create your views here.

from .models import Tarea

class TareaListView(ListView):
    model = Tarea

    template_name = "tarea_list.html"
