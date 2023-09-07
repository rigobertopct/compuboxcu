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
        peso_min = graphene.Decimal(required=False)
        peso_max = graphene.Decimal(required=False)

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

    def mutate(self, info, categoria, peso_min, peso_max, id):
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


class NuevoPugil(Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        edad = graphene.Int(required=False)
        peso = graphene.Decimal(required=False)
        categoria = graphene.Int(required=True)
        pais = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, nombre, edad, peso, categoria, pais):
        try:
            item_nombre = nombre
            item_edad = edad
            item_peso = peso
            item_categoria = Categoria.objects.get(id=categoria)
            item_pais = Pais.objects.get(id=pais)
            Pugil.objects.create(nombre=item_nombre, edad=item_edad, peso=item_peso, categoria=item_categoria,
                                 pais=item_pais)
            return NuevoPugil(success=True, errors=None)
        except Exception as e:
            return NuevoPugil(success=False, errors=str(e))


class ActualizarPugil(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        nombre = graphene.String(required=False)
        edad = graphene.Int(required=False)
        peso = graphene.Decimal(required=False)
        categoria = graphene.Int(required=True)
        pais = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, nombre, edad, peso, categoria, pais, id):
        try:
            item = Pugil.objects.get(id=id)
            item_categoria = Categoria.objects.get(id=categoria)
            item_pais = Pais.objects.get(id=pais)
            item.nombre = nombre
            item.edad = edad
            item.peso = peso
            item.categoria = item_categoria
            item.pais = item_pais
            item.save()
            return ActualizarPugil(success=True, errors=None)
        except Exception as e:
            return ActualizarPugil(success=False, errors=str(e))


class EliminarPugil(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = Pugil.objects.get(id=id)
            item.delete()
            return EliminarPugil(success=True, errors=None)
        except Exception as e:
            return EliminarPugil(success=False, errors=str(e))


class NuevoCombate(Mutation):
    class Arguments:
        fecha = graphene.Date(required=True)
        esquinaA = graphene.Int(required=False)
        esquinaR = graphene.Decimal(required=False)
        evento = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, fecha, esquinaA, esquinaR, evento):
        try:
            item_fecha = fecha
            item_esquinaA = esquinaA
            item_esquinaR = esquinaR
            item_evento = Evento.objects.get(id=evento)
            Combate.objects.create(fecha=item_fecha, esquinaA=item_esquinaA, esquinaR=item_esquinaR, evento=item_evento)
            return NuevoCombate(success=True, errors=None)
        except Exception as e:
            return NuevoCombate(success=False, errors=str(e))


class ActualizarCombate(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        fecha = graphene.Date(required=False)
        esquinaA = graphene.Int(required=False)
        esquinaR = graphene.Decimal(required=False)
        evento = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, fecha, esquinaA, esquinaR, evento, id):
        try:
            item = Combate.objects.get(id=id)
            item_roja = Pugil.objects.get(id=esquinaR)
            item_azul = Pugil.objects.get(id=esquinaA)
            item_evento = Evento.objects.get(id=evento)
            item.fecha = fecha
            item.esquinaA = item_azul
            item.esquinaR = item_roja
            item.evento = item_evento
            item.save()
            return ActualizarCombate(success=True, errors=None)
        except Exception as e:
            return ActualizarCombate(success=False, errors=str(e))


class EliminarCombate(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = Combate.objects.get(id=id)
            item.delete()
            return EliminarCombate(success=True, errors=None)
        except Exception as e:
            return EliminarCombate(success=False, errors=str(e))


class NuevoHistorico(Mutation):
    class Arguments:
        peso = graphene.Decimal(required=True)
        fecha = graphene.Date(required=False)
        pugil = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, peso, fecha, pugil):
        try:
            item_peso = peso
            item_fecha = fecha
            item_pugil = Pugil.objects.get(id=pugil)
            HistoricoPeso.objects.create(fecha=item_fecha, peso=item_peso, pugil=item_pugil)
            return NuevoHistorico(success=True, errors=None)
        except Exception as e:
            return NuevoHistorico(success=False, errors=str(e))


class ActualizarHistorico(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        fecha = graphene.Date(required=False)
        peso = graphene.Decimal(required=False)
        pugil = graphene.Int(required=False)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, fecha, peso, pugil, id):
        try:
            item = HistoricoPeso.objects.get(id=id)
            item_pugil = Pugil.objects.get(id=pugil)
            item.fecha = fecha
            item.peso = peso
            item.save()
            return ActualizarHistorico(success=True, errors=None)
        except Exception as e:
            return ActualizarHistorico(success=False, errors=str(e))


class EliminarHistorico(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = HistoricoPeso.objects.get(id=id)
            item.delete()
            return EliminarHistorico(success=True, errors=None)
        except Exception as e:
            return EliminarHistorico(success=False, errors=str(e))


class NuevoResultado(Mutation):
    class Arguments:
        combate = graphene.Int(required=True)
        resultado = graphene.Int(required=False)
        pugil = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, combate, resultado, pugil):
        try:
            item_combate = Combate.objects.get(id=combate)
            item_resultado = CodifResultado.objects.get(id=resultado)
            item_pugil = Pugil.objects.get(id=pugil)
            Resultado.objects.create(combate=item_combate, resultado=item_resultado, pugil=item_pugil)
            return NuevoResultado(success=True, errors=None)
        except Exception as e:
            return NuevoResultado(success=False, errors=str(e))


class ActualizarResultado(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        combate = graphene.Int(required=False)
        resultado = graphene.Int(required=False)
        pugil = graphene.Int(required=False)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, combate, resultado, pugil, id):
        try:
            item = Resultado.objects.get(id=id)
            item_pugil = Pugil.objects.get(id=pugil)
            item_combate = Combate.objects.get(id=combate)
            item_resultado = CodifResultado.objects.get(id=resultado)
            item.resultado = item_resultado
            item.combate = item_combate
            item.pugil = item_pugil
            item.save()
            return ActualizarResultado(success=True, errors=None)
        except Exception as e:
            return ActualizarResultado(success=False, errors=str(e))


class EliminarResultado(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = Resultado.objects.get(id=id)
            item.delete()
            return EliminarResultado(success=True, errors=None)
        except Exception as e:
            return EliminarResultado(success=False, errors=str(e))


class NuevoGolpe(Mutation):
    class Arguments:
        golpe = graphene.String(required=True)
        siglas = graphene.String(required=False)
        efectivo = graphene.Boolean(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, golpe, siglas, efectivo):
        try:
            item_golpe = golpe
            item_siglas = siglas
            item_efectivo = efectivo
            Golpe.objects.create(golpe=item_golpe, siglas=item_siglas, efectivo=item_efectivo)
            return NuevoGolpe(success=True, errors=None)
        except Exception as e:
            return NuevoGolpe(success=False, errors=str(e))


class ActualizarGolpe(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        siglas = graphene.String(required=False)
        golpe = graphene.String(required=False)
        efectivo = graphene.Boolean(required=False)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, golpe, siglas, efectivo, id):
        try:
            item = Golpe.objects.get(id=id)
            item.golpe = golpe
            item.siglas = siglas
            item.efectivo = efectivo
            item.save()
            return ActualizarGolpe(success=True, errors=None)
        except Exception as e:
            return ActualizarGolpe(success=False, errors=str(e))


class EliminarGolpe(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = Golpe.objects.get(id=id)
            item.delete()
            return EliminarGolpe(success=True, errors=None)
        except Exception as e:
            return EliminarGolpe(success=False, errors=str(e))


class CrearUsuario(Mutation):
    class Arguments:
        nombre = graphene.String()
        apellidos = graphene.String()
        usuario = graphene.String()
        email = graphene.String()
        password = graphene.String()

    error = graphene.String()
    success = graphene.Boolean()

    def mutate(self, info, nombre, apellidos, usuario, email, password):
        try:
            usuario = User.objects.create(email=email, first_name=nombre, last_name=apellidos, username=usuario)
            usuario.set_password(password)
            usuario.save()
            return CrearUsuario(error=None, success=True)
        except Exception as e:
            return CrearUsuario(error=str(e), success=False)


class NuevaTecla(Mutation):
    class Arguments:
        tecla = graphene.String()
        golpe = graphene.Int()
        usuario = graphene.Int()

    error = graphene.String()
    success = graphene.Boolean()

    def mutate(self, info, tecla, usuario, golpe):
        try:
            item_golpe = Golpe.objects.get(id=golpe)
            item_usuario = User.objects.get(id=usuario)
            teclas = ConfigGolpe.objects.filter(user=item_usuario)
            if teclas.filter(tecla=tecla).exists():
                return NuevaTecla(error="Ya tienes configurado esa tecla", success=False)
            if teclas.filter(golpe=item_golpe).exists():
                return NuevaTecla(error="Ya tienes configurado ese golpe", success=False)
            ConfigGolpe.objects.create(golpe=item_golpe, user=item_usuario, tecla=tecla)
            return NuevaTecla(error=None, success=True)
        except Exception as e:
            return NuevaTecla(error=str(e), success=False)


class ActualizarTecla(Mutation):
    class Arguments:
        id = graphene.Int()
        tecla = graphene.String()
        golpe = graphene.Int()
        usuario = graphene.Int()

    error = graphene.String()
    success = graphene.Boolean()

    def mutate(self, info, tecla, usuario, golpe, id):
        try:
            item_tecla = ConfigGolpe.objects.get(id=id)
            item_golpe = Golpe.objects.get(id=golpe)
            item_usuario = User.objects.get(id=usuario)
            # teclas = ConfigGolpe.objects.filter(user=item_usuario)
            # if teclas.filter(tecla=tecla).exists():
            #     return NuevaTecla(error="Ya tienes configurado esa tecla", success=False)
            # if teclas.filter(golpe=item_golpe).exists():
            #     return NuevaTecla(error="Ya tienes configurado ese golpe", success=False)
            item_tecla.golpe = item_golpe
            item_tecla.user = item_usuario
            item_tecla.tecla = tecla
            item_tecla.save()
            return ActualizarTecla(error=None, success=True)
        except Exception as e:
            return ActualizarTecla(error=str(e), success=False)


class EliminarTecla(Mutation):
    class Arguments:
        id = graphene.Int()

    error = graphene.String()
    success = graphene.Boolean()

    def mutate(self, info, id):
        try:
            item_tecla = ConfigGolpe.objects.get(id=id)
            item_tecla.delete()
            return EliminarTecla(error=None, success=True)
        except Exception as e:
            return EliminarTecla(error=str(e), success=False)


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
    nuevoPugil = NuevoPugil.Field()
    actualizarPugil = ActualizarPugil.Field()
    eliminarPugil = EliminarPugil.Field()
    nuevoCombate = NuevoCombate.Field()
    actualizarCombate = ActualizarCombate.Field()
    eliminarCombate = EliminarCombate.Field()
    nuevoHistorico = NuevoHistorico.Field()
    actualizarHistorico = ActualizarHistorico.Field()
    eliminarHistorico = EliminarHistorico.Field()
    nuevoResultado = NuevoResultado.Field()
    actualizarResultado = ActualizarResultado.Field()
    eliminarResultado = EliminarResultado.Field()
    nuevoGolpe = NuevoGolpe.Field()
    actualizarGolpe = ActualizarGolpe.Field()
    eliminarGolpe = EliminarGolpe.Field()
    crearUsuario = CrearUsuario.Field()
    nuevaTecla = NuevaTecla.Field()
    actualizarTecla = ActualizarTecla.Field()
    eliminarTecla = EliminarTecla.Field()
