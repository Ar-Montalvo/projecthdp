from _ast import mod

from django.db import models

# Create your models here.


class Topografia(models.Model):
    topografia = models.CharField(max_length=30)
    descipcion = models.CharField(max_length=200)
    temperaturaProm = models.DecimalField(max_digits=8, decimal_places=2)
    altitud = models.DecimalField(max_digits=8, decimal_places=2)
    lluvias = models.ForeignKey(Categorizacion)
    radiacion = models.ForeignKey(Categorizacion)


class Suelo(models.Model):
    tipoSuelo = models.CharField(max_lenght=30)
    esHomogeneo = models.BooleanField()
    textura = models.ForeignKey(Categorizacion)
    degradacion = models.ForeignKey(Categorizacion)
    ventilacion = models.ForeignKey(Categorizacion)
    estaEn = models.OneToOneRel(Topografia)


class Fertilizante(models.Model):
    nitrogeno = models.DecimalField(max_digits=8, decimal_places=2)
    fosfotoGramP = models.DecimalField(max_digits=8, decimal_places=2)
    potasioGramK = models.DecimalField(max_digits=8, decimal_places=2)


class ManejoDelSuelo(models.Model):
    muestreo = models.CharField(max_length=200)
    recuperacion = models.BooleanField()
    espaciamiento = models.ForeignKey(Categorizacion)
    fertilizante = models.ManyToManyRel(Fertilizante)


class FactorControlable(models.Model):
    profundidadSiembra = models.DecimalField(max_digits=3, decimal_places=2)
    anteriorUsoDelSuelo = models.IntegerField()


class Clima(models.Model):
    fenomenoClimatico = models.CharField(max_length=50)
    indiceSequia = models.IntegerField()
    indiceInundacion = models.IntegerField()
    tempMax = models.IntegerField()
    tempMin = models.IntegerField()


class PlagaOEnfermedad(models.Model):
    nombrePlagaOEnfermedad = models.CharField(max_lenght=50)
    recomendacion = models.CharField(max_lenght=200)


class CondicionAnual(models.Model):
    anomaliasEnLaPlantacion = models.CharField(max_lenght=50)
    fechaQueEmerge = models.DateField()
    hayMalezas = models.BooleanField()
    fenomenoClima = models.ManyToOneRel(Clima)
    plagasYEnfermedades = models.ManyToOneRel(PlagaOEnfermedad)


class MaterialGenetico(models.Model):
    nombreMaterial = models.CharField(max_length=50)
    potencialAzucarero = models.IntegerField()


class DensidadCañera(models.Model):
    calidad = models.ForeignKey(Categorizacion)
    siembra = models.ForeignKey(Categorizacion)
    yema = models.IntegerField()


class SimulacionCultivo(models.Model):
    nombreSimulacionCultivo = models.CharField(max_length=30)
    fechaSiembra = models.DateField()
    fc = models.ManyToOneRel(FactorControlable)
    ca = models.ManyToOneRel(CondicionAnual)
    dc = models.ManyToOneRel(DensidadCañera)
    mg = models.ManyToManyRel(MaterialGenetico)


class Rendimiento(models.Model):
    pesoPromTalloGram = models.DecimalField(max_digits=8, decimal_places=2)
    numPlantSemb = models.IntegerField()
    numPlantGermi = models.IntegerField()
    rendCaniaIni = models.DecimalField(max_digits=8, decimal_places=2)
    rendCaniaFin = models.DecimalField(max_digits=8, decimal_places=2)
    rendAzuIni = models.DecimalField(max_digits=8, decimal_places=2)
    rendAzuFin = models.DecimalField(max_digits=8, decimal_places=2)


class CicloProduccion(models.Model):
    ciclosDeProduccion = models.IntegerField()
    fechaDeCorta = models.DateField()
    rendimiento = models.OneToOneRel(Rendimiento)


class Cosecha(models.Model):
    nombreSimulacionCosecha = models.CharField(max_length=30)
    edadDeCorta = models.IntegerField()
    esCorteManual = models.BooleanField()
    esQuemada = models.BooleanField()
    simulacionCultivo = models.ManyToOneRel(SimulacionCultivo)
    ciclosDeProduccion = models.ForeignKey(CicloProduccion)




#
# class Caña(models.Model):
#     fotosintesis = models.DecimalField(max_digits=8, decimal_places=2)
#     crecimiento = models.DecimalField(max_digits=8, decimal_places=2)
#     floracion = models.ForeignKey(Categorizacion)
#     respiracion = models.ForeignKey(Categorizacion)
#     absorcionMineral = models.ForeignKey(Categorizacion)
#     elongacion = models.ForeignKey(Categorizacion)
#     factoresExternos = FactoresExternos
#     materialGenetico = MaterialGenetico
#     densidadCañera = DensidadCañera
#
#
#     #simulacion Cultivo





