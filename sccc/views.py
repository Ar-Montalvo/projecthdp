from django.shortcuts import render
#importamos el forms para el registro del usuario
from sccc.forms import RegistroForm
#esto es para que django haga todo lo del registro
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import TemplateView, CreateView

class Index(TemplateView):
    template_name = 'indexBase (2).html'

class VistaCultivo(TemplateView):
    template_name = 'cultivoh (2).html'

class Investigacion(TemplateView):
    template_name = 'investigacion.html'

class Usuario(TemplateView):
    template_name = 'user.html'

class VistaCosecha(TemplateView):
    template_name = 'cosecha.html'

class RegistroUsuario(CreateView):
	model=User
	template_name='registrar.html'
	form_class=RegistroForm
	success_url=reverse_lazy('login')