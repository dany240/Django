# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Docentes(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre_doc = models.CharField(max_length=45, blank=True, null=True)
    apellido_doc = models.CharField(max_length=45, blank=True, null=True)
    contraseña = models.CharField(max_length=45, blank=True, null=True)
    celular = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'docentes'


class DocentesEnSemestre(models.Model):
    id_semestre = models.ForeignKey('Semestre', models.DO_NOTHING, db_column='id_semestre', primary_key=True)
    cedula_doc = models.ForeignKey(Docentes, models.DO_NOTHING, db_column='cedula_doc')

    class Meta:
        managed = False
        db_table = 'docentes_en_semestre'
        unique_together = (('id_semestre', 'cedula_doc'),)


class Estudiante(models.Model):
    cod_estudio = models.AutoField(primary_key=True)
    nombre_est = models.CharField(max_length=45, blank=True, null=True)
    apellido_est = models.CharField(max_length=45, blank=True, null=True)
    quesemestre = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estudiante'


class Estudianteysemestre(models.Model):
    id_semestre = models.ForeignKey('Semestre', models.DO_NOTHING, db_column='id_semestre', primary_key=True)
    cod_estudio = models.ForeignKey(Estudiante, models.DO_NOTHING, db_column='cod_estudio')

    class Meta:
        managed = False
        db_table = 'estudianteysemestre'
        unique_together = (('id_semestre', 'cod_estudio'),)


class Materia(models.Model):
    cod_materia = models.AutoField(primary_key=True)
    nombre_materia = models.CharField(max_length=45, blank=True, null=True)
    creditos = models.IntegerField(blank=True, null=True)
    semestre_id = models.IntegerField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materia'


class Materiayestudiantes(models.Model):
    cod_materia = models.ForeignKey(Materia, models.DO_NOTHING, db_column='cod_materia')
    cod_estudio = models.IntegerField()
    id_semestre = models.ForeignKey(Estudianteysemestre, models.DO_NOTHING, db_column='id_semestre', primary_key=True)

    class Meta:
        managed = False
        db_table = 'materiayestudiantes'
        unique_together = (('id_semestre', 'cod_estudio', 'cod_materia'),)


class Notas(models.Model):
    tipodenota = models.CharField(primary_key=True, max_length=75)
    notas = models.IntegerField(blank=True, null=True)
    cod_materia = models.IntegerField()
    cod_estudio = models.IntegerField()
    id_semestre = models.ForeignKey(DocentesEnSemestre, models.DO_NOTHING, db_column='id_semestre')
    cedula_doc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notas'
        unique_together = (('tipodenota', 'cod_materia', 'cod_estudio', 'id_semestre'),)


class Semestre(models.Model):
    periodo = models.AutoField(blank=True, null=True)
    año = models.AutoField(blank=True, null=True)
    id_semestre = models.AutoField(primary_key=True)
    novedades = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'semestre'
