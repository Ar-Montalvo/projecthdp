from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from sccc.models import SimulacionCultivo
from sccc.util	import Mapeo

class RegistroForm(UserCreationForm):
	class Meta:
		model=User
		fields=[
			'username',
			'first_name',
			'last_name',
			'email',
		]
		labels = {
			'username':'Nombre de Usuario',
			'first_name':'Nombre',
			'last_name':'Apellido',
			'email':'Correo Electronico',
		}
		widgets = {



}

class CultivoForm(item) 
	def obtenerSimulacionCultivoForm(item):
		sc = SimulacionCultivo.getiter(self)
		#nombreSimulacionCultivo = models.CharField(max_length=50)
		ns = sc.nombreSimulacionCultivo
		#fechaDeSiembra = models.DateField()
    	fds = sc.fechaDeSiembra
    	#fechaDeSimulacion = models.DateField()
    	fs = sc.fechaDeSimulacion
    	#fc = models.ManyToOneRel(FactorControlable)
    	fc = FactorControlable.getiter(self)	#cambiar la funcion getiter
    	#ca = models.ManyToOneRel(CondicionAnual)
    	ca = CondicionAnual.getiter(self)
    	#dc = models.ManyToOneRel(DensidadCañera)
    	dc = DensidadCañera.getiter(self)
    	#mg = models.ManyToOneRel(MaterialGenetico)
    	mg = MaterialGenetico.getiter(self)
    	#pyenp = models.ManyToManyRel(PlagaYEnfermedadDeLaPlanta)
    	it = sc.pyenp
    	obtenerPyenpS(it)
		return 

	def obtenerPyenpS(it)
		mapeo = Mapeo.__init__() 
		for a in b  
