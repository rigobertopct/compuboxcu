import graphene
from graphene_django import DjangoObjectType

from .models import *


class TipoEventoType(DjangoObjectType):
    class Meta:
        model = TipoEvento
        fields = '__all__'


class PaisType(DjangoObjectType):
    class Meta:
        model = Pais
        fields = '__all__'


class Query(graphene.ObjectType):
    eventos = graphene.List(TipoEventoType, name=graphene.String())
    paises = graphene.List(PaisType, name=graphene.String())

    def resolve_paises(self, info, name):
        if name == "":
            return Pais.objects.all()
        else:
            return Pais.objects.filter(pais__icontains=name)

    def resolve_eventos(self, info, name):
        if name == "":
            return TipoEvento.objects.all()
        else:
            return TipoEvento.objects.filter(tipo__icontains=name)
