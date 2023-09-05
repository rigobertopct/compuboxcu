import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q
from .models import *


class TipoEventoType(DjangoObjectType):
    class Meta:
        model = TipoEvento
        fields = '__all__'


class PaisType(DjangoObjectType):
    class Meta:
        model = Pais
        fields = '__all__'
        
class ReglamentoType(DjangoObjectType):
    class Meta:
        model = Reglamento
        fields = '__all__'

class EventoType(DjangoObjectType):
    class Meta:
        model = Evento
        fields = '__all__'

class CategoriaType(DjangoObjectType):
    class Meta:
        model = Categoria
        fields = '__all__'

class PugilType(DjangoObjectType):
    class Meta:
        model = Pugil
        fields = '__all__'
        
class HistoricoPesoType(DjangoObjectType):
    class Meta:
        model = HistoricoPeso
        fields = '__all__'
        
class CombateType(DjangoObjectType):
    class Meta:
        model = Combate
        fields = '__all__'
        
class CodifResultadoType(DjangoObjectType):
    class Meta:
        model = CodifResultado
        fields = '__all__'
        
class ResultadoType(DjangoObjectType):
    class Meta:
        model = Resultado
        fields = '__all__'
        
class GolpeType(DjangoObjectType):
    class Meta:
        model = Golpe
        fields = '__all__'

class ContadorGolpesType(DjangoObjectType):
    class Meta:
        model = ContadorGolpes
        fields = '__all__'
        
class ConfigGolpeType(DjangoObjectType):
    class Meta:
        model = ConfigGolpe
        fields = '__all__'
        
class Query(graphene.ObjectType):
    tiposE = graphene.List(TipoEventoType, name=graphene.String())
    paises = graphene.List(PaisType, name=graphene.String())
    reglamentos = graphene.List(ReglamentoType, name=graphene.String())
    eventos = graphene.List(EventoType, name=graphene.String())
    categorias = graphene.List(CategoriaType, name=graphene.String())
    pugiles = graphene.List(PugilType, name=graphene.String())
    pesosh = graphene.List(HistoricoPesoType, name=graphene.String())
    combates = graphene.List(CombateType, name=graphene.String())
    codifResult = graphene.List(CodifResultadoType, name=graphene.String())
    resultados = graphene.List(ResultadoType, name=graphene.String())
    golpes = graphene.List(GolpeType, name=graphene.String())
    contGolpes = graphene.List(ContadorGolpesType, name=graphene.String())
    configGolpes = graphene.List(ConfigGolpeType, name=graphene.String())

    def resolve_paises(self, info, name):
        if name == "":
            return Pais.objects.all()
        else:
            return Pais.objects.filter(
                Q(pais__icontains=name)|Q(siglas__icontains=name)
                
                                                  )

    def resolve_tiposE(self, info, name):
        if name == "":
            return TipoEvento.objects.all()
        else:
            return TipoEvento.objects.filter(tipo__icontains=name)

    def resolve_reglamento(self, info, name):
        if name == "":
            return Reglamento.objects.all()
        else:
            return Reglamento.objects.filter(
                Q(tipo__icontains=name)|Q(cant_r__icontains=name)|Q(duracion__icontains=name)
                
                                                  )
        
    def resolve_eventos(self, info, name):
        if name == "":
            return Evento.objects.all()
        else:
            return Evento.objects.filter(
                Q(nombre__icontains=name)|Q(pais__pais__icontains=name)|Q(reglamento__reglamento__icontains=name)|Q(tipoevento__tipo__icontains=name)
                
                                                  )
    
    def resolve_categorias(self, info, name):
        if name == "":
            return Categoria.objects.all()
        else:
            return Categoria.objects.filter(
                Q(categoria__icontains=name)|Q(peso_min__icontains=name)|Q(peso_max__icontains=name)
                
                                                  )
        
    def resolve_pugiles(self, info, name):
        if name == "":
            return Pugil.objects.all()
        else:
            return Pugil.objects.filter(
                Q(nombre__icontains=name)|Q(edad__icontains=name)|Q(peso__icontains=name)|Q(categoria__categoria__icontains=name)|Q(pais__pais__icontains=name)
                
                                                  )
        
    def resolve_pesosh(self, info, name):
        if name == "":
            return HistoricoPeso.objects.all()
        else:
            return HistoricoPeso.objects.filter(tipo__icontains=name)
        
    def resolve_combate(self, info, name):
        if name == "":
            return Combate.objects.all()
        else:
           return Pugil.objects.filter(
                Q(fecha__icontains=name)|Q(esquinaA__nombre__icontains=name)|Q(esquinaR__nombre__icontains=name)|Q(evento__nombre__icontains=name)
                
                                                  )
        
    def resolve_codifResult(self, info, name):
        if name == "":
            return CodifResultado.objects.all()
        else:
           return CodifResultado.objects.filter(
                Q(resul__icontains=name)|Q(descripcion__icontains=name)
                
                                                  )
        
    def resolve_resultados(self, info, name):
        if name == "":
            return Resultado.objects.all()
        else:
             return Resultado.objects.filter(
                Q(combate__fecha__icontains=name)|Q(pugil__pugil__icontains=name)|Q(resultado__resultado__icontains=name)
                
                                                  )
        
    def resolve_golpes(self, info, name):
        if name == "":
            return Golpe.objects.all()
        else:
           return Golpe.objects.filter(
                Q(golpe__icontains=name)|Q(siglas__icontains=name)
                
                                                  )
        
    def resolve_contGolpes(self, info, name):
        if name == "":
            return ContadorGolpes.objects.all()
        else:
            return ContadorGolpes.objects.filter(
                Q(golpe__icontains=name)|Q(siglas__icontains=name)
                
                                                  )
        
    def resolve_configGolpes(self, info, name):
        if name == "":
            return ConfigGolpe.objects.all()
        else:
            return ConfigGolpe.objects.filter(
                Q(tecla__icontains=name)|Q(golpe__golpe__icontains=name)|Q(user__username__icontains=name)
                
                                                  )