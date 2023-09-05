import graphene
from graphene import Mutation

from .models import Pais


class NuevoPais(Mutation):
    class Arguments:
        pais = graphene.String(required=True)
        siglas = graphene.String(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, pais, siglas):
        try:
            Pais.objects.create(pais=pais, siglas=siglas)
            return NuevoPais(success=True, errors=None)
        except Exception as e:
            return NuevoPais(success=False, errors=str(e))


class ActualizarPais(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        pais = graphene.String(required=True)
        siglas = graphene.String(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, pais, siglas, id):
        try:
            paiss = Pais.objects.get(id=id)
            paiss.pais = pais
            paiss.siglas = siglas
            paiss.save()
            return ActualizarPais(success=True, errors=None)
        except Exception as e:
            return ActualizarPais(success=False, errors=str(e))


class Mutation(graphene.ObjectType):
    nuevoPais = NuevoPais.Field()
    actualizarPais = ActualizarPais.Field()
