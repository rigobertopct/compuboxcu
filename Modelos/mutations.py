import graphene
from graphene import Mutation

from .models import *


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


class EliminarPais(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            paiss = Pais.objects.get(id=id)
            paiss.delete()
            return EliminarPais(success=True, errors=None)
        except Exception as e:
            return EliminarPais(success=False, errors=str(e))


class NuevoCodifResultado(Mutation):
    class Arguments:
        resultado = graphene.String(required=True)
        descripcion = graphene.String(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, resultado, descripcion):
        try:
            CodifResultado.objects.create(resul=resultado, descripcion=descripcion)
            return NuevoCodifResultado(success=True, errors=None)
        except Exception as e:
            return NuevoCodifResultado(success=False, errors=str(e))


class ActualizarCodifResultado(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        resultado = graphene.String(required=True)
        descripcion = graphene.String(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, resultado, id, descripcion):
        try:
            item = CodifResultado.objects.get(id=id)
            item.resul = resultado
            item.descripcion = descripcion
            item.save()
            return ActualizarCodifResultado(success=True, errors=None)
        except Exception as e:
            return ActualizarCodifResultado(success=False, errors=str(e))


class EliminarCodifResultado(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = CodifResultado.objects.get(id=id)
            item.delete()
            return EliminarCodifResultado(success=True, errors=None)
        except Exception as e:
            return EliminarCodifResultado(success=False, errors=str(e))


class NuevoTipoEvento(Mutation):
    class Arguments:
        nombre = graphene.String(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, nombre):
        try:
            TipoEvento.objects.create(tipo=nombre)
            return NuevoTipoEvento(success=True, errors=None)
        except Exception as e:
            return NuevoTipoEvento(success=False, errors=str(e))


class ActualizarTipoEvento(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        nombre = graphene.String(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, nombre, id):
        try:
            item = TipoEvento.objects.get(id=id)
            item.tipo = nombre
            item.save()
            return ActualizarTipoEvento(success=True, errors=None)
        except Exception as e:
            return ActualizarTipoEvento(success=False, errors=str(e))


class EliminarTipoEvento(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = TipoEvento.objects.get(id=id)
            item.delete()
            return EliminarTipoEvento(success=True, errors=None)
        except Exception as e:
            return EliminarTipoEvento(success=False, errors=str(e))


class NuevoReglamento(Mutation):
    class Arguments:
        tipo = graphene.String(required=True)
        cant_r = graphene.Int(required=True)
        duracion = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, tipo, cant_r, duracion):
        try:
            Reglamento.objects.create(tipo=tipo, cant_r=cant_r, duracion=duracion)
            return NuevoReglamento(success=True, errors=None)
        except Exception as e:
            return NuevoReglamento(success=False, errors=str(e))


class ActualizarReglamento(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        tipo = graphene.String(required=True)
        cant_r = graphene.Int(required=True)
        duracion = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, tipo, cant_r, duracion, id):
        try:
            item = Reglamento.objects.get(id=id)
            item.tipo = tipo
            item.cant_r = cant_r
            item.duracion = duracion
            item.save()
            return ActualizarReglamento(success=True, errors=None)
        except Exception as e:
            return ActualizarReglamento(success=False, errors=str(e))


class EliminarReglamento(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = Reglamento.objects.get(id=id)
            item.delete()
            return EliminarReglamento(success=True, errors=None)
        except Exception as e:
            return EliminarReglamento(success=False, errors=str(e))


class NuevoEvento(Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        pais = graphene.Int(required=True)
        reglamento = graphene.Int(required=True)
        tipoevento = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, nombre, pais, reglamento, tipoevento):
        try:
            item_pais = Pais.objects.get(id=pais)
            item_reglamento = Reglamento.objects.get(id=reglamento)
            item_tipoevento = TipoEvento.objects.get(id=tipoevento)
            Evento.objects.create(nombre=nombre, pais=item_pais, reglamento=item_reglamento,
                                  tipoevento=item_tipoevento)
            return NuevoEvento(success=True, errors=None)
        except Exception as e:
            return NuevoEvento(success=False, errors=str(e))


class ActualizarEvento(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        nombre = graphene.String(required=True)
        pais = graphene.Int(required=True)
        reglamento = graphene.Int(required=True)
        tipoevento = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, nombre, pais, reglamento, tipoevento, id):
        try:
            item = Evento.objects.get(id=id)
            item_pais = Pais.objects.get(id=pais)
            item_reglamento = Reglamento.objects.get(id=reglamento)
            item_tipoevento = TipoEvento.objects.get(id=tipoevento)
            item.nombre = nombre
            item.pais = item_pais
            item.reglamento = item_reglamento
            item.tipoevento = item_tipoevento
            item.save()
            return ActualizarEvento(success=True, errors=None)
        except Exception as e:
            return ActualizarEvento(success=False, errors=str(e))


class EliminarEvento(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = Evento.objects.get(id=id)
            item.delete()
            return EliminarEvento(success=True, errors=None)
        except Exception as e:
            return EliminarEvento(success=False, errors=str(e))

class NuevaCategoria(Mutation):
    class Arguments:
        categoria = graphene.String(required=True)
        peso_min = graphene.Int(required=False)
        peso_max = graphene.Int(required=False)
    
    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, categoria, peso_min, peso_max):
        try:
            item_categoria = categoria
            pesoMin = peso_min
            pesoMax = peso_max
            Categoria.objects.create(categoria=item_categoria, peso_min=pesoMin, peso_max=pesoMax)
            return NuevaCategoria(success=True, errors=None)
        except Exception as e:
            return NuevaCategoria(success=False, errors=str(e))


class ActualizarCategoria(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        categoria = graphene.String(required=False)
        peso_min = graphene.Decimal(required=False)
        peso_max = graphene.Decimal(required=False)
       

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, categoria, peso_min, peso_max,id):
        try:
            item = Categoria.objects.get(id=id)
            item.categoria = categoria
            item.peso_min = peso_min
            item.peso_max = peso_max
            item.save()
            return ActualizarCategoria(success=True, errors=None)
        except Exception as e:
            return ActualizarCategoria(success=False, errors=str(e))


class EliminarCategoria(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = Categoria.objects.get(id=id)
            item.delete()
            return EliminarCategoria(success=True, errors=None)
        except Exception as e:
            return EliminarCategoria(success=False, errors=str(e))


class Mutation(graphene.ObjectType):
    nuevoPais = NuevoPais.Field()
    actualizarPais = ActualizarPais.Field()
    eliminarPais = EliminarPais.Field()
    nuevoCodResultado = NuevoCodifResultado.Field()
    actualizarCodResultado = ActualizarCodifResultado.Field()
    eliminarCodResultado = EliminarCodifResultado.Field()
    nuevoTipoEvento = NuevoTipoEvento.Field()
    actualizarTipoEvento = ActualizarTipoEvento.Field()
    eliminarTipoEvento = EliminarTipoEvento.Field()
    nuevoReglamento = NuevoReglamento.Field()
    actualizarReglamento = ActualizarReglamento.Field()
    eliminarReglamento = EliminarReglamento.Field()
    nuevoEvento = NuevoEvento.Field()
    actualizarEvento = ActualizarEvento.Field()
    eliminarEvento = EliminarEvento.Field()
    nuevaCategoria = NuevaCategoria.Field()
    actualizarCategoria = ActualizarCategoria.Field()
    eliminarCategoria = EliminarCategoria.Field()
