from django.shortcuts import render

# Create your views here.
#vistas basadas en clases 
from django.views.generic import TemplateView
class Index(TemplateView):
    template_name = 'Login/index.html'
class Usuario(TemplateView):
    template_name = 'html/user.html'

