from _ast import mod

from django.db import models
from sccc.util import Mapeo

# Create your models here.


class Topografia(models.Model):
    topografia = models.CharField(max_length=30)
    descipcionTopo = models.CharField(max_length=200)
    temperaturaPromedio = models.IntegerField()
    altitud = models.IntegerField()
    lluvias = models.IntegerField()
    radiacion = models.IntegerField()

    def getiter(self):
        return iter(self.from_db(self))

    def __str__(self):
        return self.topografia

    def __get_FIELD_display(self, field):
        return super()._get_FIELD_display(field)


class Suelo(models.Model):
    tipoSuelo = models.CharField(max_lenght=30)
    esHomogeneo = models.BooleanField()
    textura = models.IntegerField()
    degradacion = models.IntegerField()
    ventilacion = models.IntegerField()
    genera = models.ManyToOneRel(Topografia)

    def getiter(self):
        return iter(self.from_db())

    def __str__(self):
        return self.tipoSuelo

    def __get_FIELD_display(self, field):
        return super()._get_FIELD_display(field)


class Fertilizante(models.Model):
    nitrogeno = models.IntegerField()
    fosfotoGramP = models.IntegerField()
    potasioGramK = models.IntegerField()

    def getiter(self):
        return iter(self.from_db(self))

    def __str__(self):
        tx = "N " + self.nitrogeno.__str__() + ", P "
        tx = tx + self.fosfotoGramP.__str__() + ", K "
        return tx + self.potasioGramK.__str__()

    def __get_FIELD_display(self, field):
        return super()._get_FIELD_display(field)


class ManejoDelSuelo(models.Model):
    muestreo = models.CharField(max_length=10)
    recuperacion = models.BooleanField()
    espaciamiento = models.IntegerField()
    periodoRiego = models.IntegerField()
    utiliza = models.ManyToOneRel(Fertilizante)

    def getiter(self):
        return iter(self.from_db(self))

    def __str__(self):
        return self.muestreo

    def __get_FIELD_display(self, field):
        return super()._get_FIELD_display(field)


class FactorControlable(models.Model):
    profundidadSiembra = models.IntegerField()
    anteriorUsoDelSuelo = models.IntegerField()
    aplica = models.ForeignKey(ManejoDelSuelo)
    rs14 = models.ManyToOneRel(ManejoDelSuelo)
    requiere = models.ManyToOneRel(Suelo)

    def getiter(self):
        return iter(self.from_db(self))

    def __str__(self):
        tx = "Prof: " + self.profundidadSiembra.__str__()
        return tx + "mm, uso: " +self.anteriorUsoDelSuelo.__str__() + " años"

    def __get_FIELD_display(self, field):
        return super()._get_FIELD_display(field)


class Clima(models.Model):
    fenomenoClimatico = models.CharField(max_length=50)
    indiceSequia = models.IntegerField()
    indiceInundacion = models.IntegerField()
    tempMax = models.IntegerField()
    tempMin = models.IntegerField()

    def getiter(self):
        return iter(self.from_db(self))

    def __str__(self):
        return self.fenomenoClimatico

    def __get_FIELD_display(self, field):
        return super()._get_FIELD_display(field)


class PlagaYEnfermedadDeLaPlanta(models.Model):
    nombreEnfermedad = models.CharField(max_lenght=25)
    recomendacion = models.CharField(max_lenght=200)

    def getiter(self):
        return iter(self.from_db(self))

    def __str__(self):
        return self.nombreEnfermedad

    def __get_FIELD_display(self, field):
        return super()._get_FIELD_display(field)


class CondicionAnual(models.Model):
    anomaliasEnLaPlantacion = models.CharField(max_lenght=50)
    diasEnEmerger = models.IntegerField()
    tieneMalezas = models.BooleanField()
    fenomenoClimatico = models.ManyToOneRel(Clima)

    def getiter(self):
        return iter(self.from_db(self))

    def __get_FIELD_display(self, field):
        return super()._get_FIELD_display(field)


class MaterialGenetico(models.Model):
    nombreMaterial = models.CharField(max_length=30)
    potencialAzucarero = models.IntegerField()

    def getiter(self):
        return iter(self.from_db(self))

    def __str__(self):
        return self.nombreMaterial

    def __get_FIELD_display(self, field):
        return super()._get_FIELD_display(field)


class DensidadCañera(models.Model):
    calidad = models.IntegerField()
    siembra = models.IntegerField()
    yema = models.IntegerField()

    def __get_FIELD_display(self, field):
        return super()._get_FIELD_display(field)

    def getiter(self):
        return iter(self.from_db(self))

    def getcalidad(self, calidad):
        return self.calidad

    def getsiembra(self, siembra):
        return self.siembra

    def getyema(self, yema):
        return self.yema


class SimulacionCultivo(models.Model):
    nombreSimulacionCultivo = models.CharField(max_length=50)
    fechaDeSiembra = models.DateField()
    fechaDeSimulacion = models.DateField()
    fc = models.ManyToOneRel(FactorControlable)
    ca = models.ManyToOneRel(CondicionAnual)
    dc = models.ManyToOneRel(DensidadCañera)
    mg = models.ManyToOneRel(MaterialGenetico)
    pyenp = models.ManyToManyRel(PlagaYEnfermedadDeLaPlanta)

    def getiter(self):
        return iter(self.from_db(self))

    def __str__(self):
        return self.nombreSimulacionCultivo

    def __get_FIELD_display(self, field):
        return super()._get_FIELD_display(field)


class Rendimiento(models.Model):
    pesoPromTalloGram = models.IntegerField()
    numPlantSemb = models.IntegerField()
    numPlantGermi = models.IntegerField()
    rendCaniaIni = models.IntegerField()
    rendCaniaFin = models.IntegerField()
    rendAzuIni = models.IntegerField()
    rendAzuFin = models.IntegerField()

    def getiter(self):
        return iter(self.from_db(self))

    def __str__(self):
        tx = "Rend%: " + self.pesoPromTalloGram.__str__() + ", "
        tx = tx + self.numPlantSemb.__str__() + ", "
        tx = tx + self.numPlantGermi.__str__() + ", "
        tx = tx + self.rendCaniaIni.__str__() + ", "
        tx = tx + self.rendCaniaFin.__str__() + ", "
        tx = tx + self.rendCaniaIni.__str__() + ", "
        return tx + self.rendAzuFin.__str__()

    def __get_FIELD_display(self, field):
        return super()._get_FIELD_display(field)


class Cosecha(models.Model):
    nombreSimulacionCosecha = models.CharField(max_length=50)
    edad = models.IntegerField()
    esCorteManual = models.BooleanField()
    esQuemada = models.BooleanField()
    simulacionCultivo = models.ManyToOneRel(SimulacionCultivo)

    def getiter(self):
        return iter(self.from_db(self))

    def __str__(self):
        return self.nombreSimulacionCosecha

    def __get_FIELD_display(self, field):
        return super()._get_FIELD_display(field)


class CicloProduccion(models.Model):
    ciclosDeProduccion = models.IntegerField()
    fechaDeCorte = models.DateField()
    rendimiento = models.ManyToOneRel(Rendimiento)
    cosecha = models.ManyToOneRel(Cosecha)

    def getiter(self):
        return iter(self.from_db(self))

    def __str__(self):
        return "num" + self.ciclosDeProduccion.__str__() + self.fechaDeCorte.__str__()

    def __get_FIELD_display(self, field):
        return super()._get_FIELD_display(field)

#
# class Caña(models.Model):
#     fotosintesis = models.IntegerField()
#     crecimiento = models.IntegerField()
#     floracion = models.IntegerField()
#     respiracion = models.IntegerField()
#     absorcionMineral = models.IntegerField()
#     elongacion = models.IntegerField()
#     factoresExternos = FactoresExternos
#     materialGenetico = MaterialGenetico
#     densidadCañera = DensidadCañera
#
#
#     #simulacion Cultivo