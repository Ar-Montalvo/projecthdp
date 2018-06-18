from django.conf.urls import url,include
#esto es para que tenga que estar logeado 
from django.contrib.auth.decorators import login_required
from sccc.views import Index,Cultivov,Investigacion,Usuario,Cosechav,RegistroUsuario
app_name="sccc"
urlpatterns = [
	url(r'index',login_required(Index.as_view()), name='inicio'),
	url(r'cultivo',login_required(Cultivov.as_view()), name='pagina_cultivo'),
	url(r'cosecha',login_required(Cosechav.as_view()), name='pagina_cosecha'),
	url(r'investigacion',login_required(Investigacion.as_view()), name='pagina_investigacion'),
	url(r'usuario',login_required(Usuario.as_view()), name='pagina_usuario'),
	url(r'registrar',RegistroUsuario.as_view(), name='usuario_registrar'),
	
]