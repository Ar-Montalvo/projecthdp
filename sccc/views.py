from django.shortcuts import render


# Create your views here.
from django.views.generic import TemplateView
from django.http import request, response
from .models import Topografia
from .models import Suelo, Fertilizante, ManejoDelSuelo
from .models import FactorControlable, Clima, CondicionAnual
from .models import PlagaYEnfermedadDeLaPlanta, MaterialGenetico
from .models import DensidadCañera, SimulacionCultivo




class Index(TemplateView):
    template_name = 'cultivo.html'
    listaobjeto =



    def cultivo_init(self):
        topografia = Topografia.__new__(Topografia)

        """output = ', '[topografia]"""
        return response.HttpResponse()

    def obtenerlistaobjeto(self):

        return 

class Cultivo(TemplateView):
    template_name = 'cultivoh.html'



