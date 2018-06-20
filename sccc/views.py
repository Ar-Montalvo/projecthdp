from django.shortcuts import render
#importamos el forms para el registro del usuario
from sccc.forms import RegistroForm
#esto es para que django haga todo lo del registro
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import TemplateView, CreateView
from sccc.models import SimulacionCultivo, DensidadCanera
from sccc.models import MaterialGenetico, CondicionAnual
from sccc.models import PlagaYEnfermedadDeLaPlanta,Clima
from sccc.models import FactorControlable, ManejoDelSuelo
from sccc.models import Fertilizante, Suelo, Topografia


class IndexV(TemplateView):
    template_name = 'index.html'


class CultivoV(TemplateView):
    template_name = 'cultivo.html'

    sco = SimulacionCultivo
    dco = DensidadCanera
    mgo = MaterialGenetico
    cao = CondicionAnual
    pyo = PlagaYEnfermedadDeLaPlanta
    clo = Clima
    fco = FactorControlable
    mdo = ManejoDelSuelo
    feo = Fertilizante
    suo = Suelo
    too = Topografia


def init_list(request):
    sue = Suelo.from_db(Suelo)
    mds = ManejoDelSuelo.from_db(ManejoDelSuelo)
    mgs = MaterialGenetico.from_db(MaterialGenetico)
    climas = Clima.from_db(Clima)
    pyenps = PlagaYEnfermedadDeLaPlanta.from_db()
    return render(request, 'sccc/cultivo.html', {'sue': sue, 'mds': mds, 'mgs': mgs, 'climas': climas, 'pyenps': pyenps})


class Investigacion(TemplateView):
    template_name = 'investigacion.html'


class Usuario(TemplateView):
    template_name = 'user.html'


class VistaCosecha(TemplateView):
    template_name = 'cosecha.html'


class RegistroUsuario(CreateView):
    model = User
    template_name = 'registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('login')