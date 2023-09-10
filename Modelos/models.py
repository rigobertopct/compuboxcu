from django.contrib.auth.models import User
from django.db import models


class TipoEvento(models.Model):
    tipo = models.CharField(max_length=250, verbose_name="Tipo de Evento")

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = 'tipo_evento'
        verbose_name_plural = 'tipo_eventos'
        db_table = 'tipo_evento'


class Pais(models.Model):
    pais = models.CharField(max_length=250, verbose_name="País")
    siglas = models.CharField(max_length=250, verbose_name="Siglas")

    def __str__(self):
        return self.pais

    class Meta:
        verbose_name = 'pais'
        verbose_name_plural = 'paises'
        db_table = 'pais'


class Reglamento(models.Model):
    tipo = models.CharField(max_length=255, verbose_name="Reglamento", unique=True)
    cant_r = models.IntegerField(verbose_name="Cantidad de round")
    duracion = models.IntegerField(verbose_name="Duración")

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = 'reglamento'
        verbose_name_plural = 'reglamentos'
        db_table = 'reglamento'


class Evento(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Evento", unique=True)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)
    reglamento = models.ForeignKey(Reglamento, on_delete=models.SET_NULL, null=True, blank=True)
    tipoevento = models.ForeignKey(TipoEvento, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'evento'
        verbose_name_plural = 'eventos'
        db_table = 'evento'


class Categoria(models.Model):
    categoria = models.CharField(max_length=255, verbose_name="Categoría", unique=True)
    peso_min = models.DecimalField(max_digits=5, decimal_places=2)
    peso_max = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.categoria

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        db_table = 'categoria'


class Pugil(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre y Apellidos", unique=True)
    edad = models.PositiveIntegerField(null=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)
    foto = models.ImageField(upload_to='pugiles', null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'pugil'
        verbose_name_plural = 'pugils'
        db_table = 'pugil'


class HistoricoPeso(models.Model):
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    pugil = models.ForeignKey(Pugil, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateField()

    def __str__(self):
        return self.peso

    class Meta:
        verbose_name = 'histpeso'
        verbose_name_plural = 'histpesos'
        db_table = 'histpeso'


class Combate(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True)
    esquinaR = models.ForeignKey(Pugil, on_delete=models.SET_NULL, related_name='person1', null=True, blank=True)
    esquinaA = models.ForeignKey(Pugil, on_delete=models.SET_NULL, related_name='person', null=True, blank=True)
    evento = models.ForeignKey(Evento, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'combate'
        verbose_name_plural = 'combates'
        db_table = 'combate'


class CodifResultado(models.Model):
    resul = models.CharField(max_length=255, verbose_name="resultado")
    descripcion = models.CharField(max_length=255, verbose_name="descripción")

    def __str__(self):
        return self.resul

    class Meta:
        verbose_name = 'codifresultado'
        verbose_name_plural = 'codifresultados'
        db_table = 'codifresultado'


class Resultado(models.Model):
    combate = models.ForeignKey(Combate, on_delete=models.SET_NULL, null=True, blank=True)
    pugil = models.ForeignKey(Pugil, on_delete=models.SET_NULL, null=True, blank=True)
    resultado = models.ForeignKey(CodifResultado, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'resultado'
        verbose_name_plural = 'resultados'
        db_table = 'resultado'


class Golpe(models.Model):
    golpe = models.CharField(max_length=255, verbose_name="golpe")
    siglas = models.CharField(max_length=10, verbose_name="siglas", null=True, blank=True)
    efectivo = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.golpe

    class Meta:
        verbose_name = 'golpe'
        verbose_name_plural = 'golpes'
        db_table = 'golpe'


class ContadorGolpes(models.Model):
    combate = models.ForeignKey(Combate, on_delete=models.SET_NULL, null=True, blank=True)
    numero_asalto = models.PositiveIntegerField()
    golpe = models.ForeignKey(Golpe, on_delete=models.SET_NULL, null=True, blank=True)
    esquina = models.ForeignKey(Pugil, on_delete=models.SET_NULL, verbose_name="esquina", null=True, blank=True)

    def __str__(self):
        return self.esquina.nombre

    class Meta:
        verbose_name = 'contadorgolpe'
        verbose_name_plural = 'contadorgolpes'
        db_table = 'contador_golpe'


class ConfigGolpe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    golpe = models.ForeignKey(Golpe, on_delete=models.SET_NULL, null=True, blank=True)
    tecla = models.CharField(max_length=255, verbose_name="tecla")

    def __str__(self):
        return self.tecla

    class Meta:
        verbose_name = 'configolpe'
        verbose_name_plural = 'configolpes'
        db_table = 'config_golpe'
        