from _ast import mod

from django.db import models

# Create your models here.


class Topografia(models.Model):
    topografia = models.CharField(max_length=30)
    descipcionTopo = models.CharField(max_length=200)
    temperaturaPromedio = models.IntegerField()
    altitud = models.IntegerField()
    lluvias = models.IntegerField()
    radiacion = models.IntegerField()
#Generar lista

class Suelo(models.Model):
    tipoSuelo = models.CharField(max_lenght=30)
    esHomogeneo = models.BooleanField()
    textura = models.IntegerField()
    degradacion = models.IntegerField()
    ventilacion = models.IntegerField()
    genera = models.ManyToOneRel(Topografia)
#Generar lista

class Fertilizante(models.Model):
    nitrogeno = models.IntegerField()
    fosfotoGramP = models.IntegerField()
    potasioGramK = models.IntegerField()
#Generar lista

class ManejoDelSuelo(models.Model):
    muestreo = models.CharField(max_length=10)
    recuperacion = models.BooleanField()
    espaciamiento = models.IntegerField()
    periodoRiego = models.IntegerField()
    utiliza = models.ManyToOneRel(Fertilizante)
#Generar lista


class FactorControlable(models.Model):
    profundidadSiembra = models.IntegerField()
    anteriorUsoDelSuelo = models.IntegerField()
    aplica = models.ForeignKey(ManejoDelSuelo)
    rs14 = models.ManyToOneRel(ManejoDelSuelo)
    requiere = models.ManyToOneRel(Suelo)


class Clima(models.Model):
    fenomenoClimatico = models.CharField(max_length=50)
    indiceSequia = models.IntegerField()
    indiceInundacion = models.IntegerField()
    tempMax = models.IntegerField()
    tempMin = models.IntegerField()
#Generar lista


class PlagaYEnfermedadDeLaPlanta(models.Model):
    nombreEnfermedad = models.CharField(max_lenght=25)
    recomendacion = models.CharField(max_lenght=200)
#Generar lista


class CondicionAnual(models.Model):
    anomaliasEnLaPlantacion = models.CharField(max_lenght=50)
    diasEnEmerger = models.IntegerField()
    tieneMalezas = models.BooleanField()
    fenomenoClimatico = models.ManyToOneRel(Clima)
    

class MaterialGenetico(models.Model):
    nombreMaterial = models.CharField(max_length=30)
    potencialAzucarero = models.IntegerField()
#Generar lista


class DensidadCañera(models.Model):
    calidad = models.IntegerField()
    siembra = models.IntegerField()
    yema = models.IntegerField()


class SimulacionCultivo(models.Model):
    nombreSimulacionCultivo = models.CharField(max_length=50)
    fechaDeSiembra = models.DateField()
    fechaDeSimulacion = models.DateField()
    fc = models.ManyToOneRel(FactorControlable)
    ca = models.ManyToOneRel(CondicionAnual)
    dc = models.ManyToOneRel(DensidadCañera)
    mg = models.ManyToOneRel(MaterialGenetico)
    pyenp = models.ManyToManyRel(PlagaYEnfermedadDeLaPlanta)


class Rendimiento(models.Model):
    pesoPromTalloGram = models.IntegerField()
    numPlantSemb = models.IntegerField()
    numPlantGermi = models.IntegerField()
    rendCaniaIni = models.IntegerField()
    rendCaniaFin = models.IntegerField()
    rendAzuIni = models.IntegerField()
    rendAzuFin = models.IntegerField()


class Cosecha(models.Model):
    nombreSimulacionCosecha = models.CharField(max_length=50)
    edad = models.IntegerField()
    esCorteManual = models.BooleanField()
    esQuemada = models.BooleanField()
    simulacionCultivo = models.ManyToOneRel(SimulacionCultivo)


class CicloProduccion(models.Model):
    ciclosDeProduccion = models.IntegerField()
    fechaDeCorte = models.DateField()
    rendimiento = models.ManyToOneRel(Rendimiento)
    cosecha = models.ManyToOneRel(Cosecha)


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





