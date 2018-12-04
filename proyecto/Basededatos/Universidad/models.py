# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' orderm
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import timezone

from django.core.validators import *
from django.db import models,connection
from django.db import models


from django.db import models
from django.contrib.auth.models import User




class Docentes(models.Model):
    cedula = models.BigIntegerField(primary_key=True, db_column='cedula')
    nombre_doc = models.CharField(max_length=45, blank=False, null=False, db_column='nombre_doc')
    apellido_doc = models.CharField(max_length=45, blank=False, null=False, db_column='apellido_doc')
    contraseña = models.CharField(max_length=45, blank=False, null=False, db_column='contraseña')
    celular = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True, db_column='celular')

    class Meta:
        managed = False
        db_table = 'docentes'


def ObtenerSequencia(valor):
    diccionario={'materia':'se_materia',
                 'id_semestre':'se_id_semestre',
                 'id_estudiante':'indiceEstudiante',
                 'año':'se_año',
                 'periodo':'se_periodo'
                 }
    dato=connection.cursor()
    dato.execute("select nextval( %s )",[diccionario[valor]])
    valor=dato.fetchone()[0]
    return int(valor)


class Semestre(models.Model):
    valores=(
        ('Sin novedad','Sin novedad'),
        ('Anormalidad Academica','Paro'),
        ('Semestre Canselado','Semestre Canselado')
    )
    id_semestre = models.IntegerField(primary_key=True,default=ObtenerSequencia('id_semestre'),db_column='id_semestre')
    año = models.IntegerField(blank=False, null=False,default=ObtenerSequencia('año'),db_column='año',validators=[MinValueValidator(limit_value=0,message="Rango menor a lo esperado")])
    novedades = models.CharField(max_length=45, blank=False, null=True,db_column='novedades',default='Sin Novedades',choices=valores)
    periodo = models.IntegerField(blank=False, null=False,default=ObtenerSequencia('periodo'),db_column='periodo',validators=[MaxValueValidator(limit_value=4,message="Solo existe periodo max periodo de 4 sin novedades ")])


    print(str(id_semestre.get_attname())+"_____Semestre_________")
    def __str__(self):
        return  'semestre id= {},Año: {} -- Semestre:{} -- Novedad: {}'.format(self.id_semestre,self.año,self.periodo,self.novedades)
    class Meta:
        managed = False
        db_table = 'semestre'
        unique_together=(("año","periodo"),)


class Estudiante(models.Model):
    cod_estudio = models.IntegerField(primary_key=True,default=ObtenerSequencia('id_estudiante'))
    nombre_est = models.CharField(max_length=45, blank=False, null=False)
    apellido_est = models.CharField(max_length=45, blank=False, null=False)
    quesemestre = models.IntegerField(blank=False, null=False)
    print(str(cod_estudio)+"_____________Estudiante__________________________________")
    def __str__(self):
        return  'CodigoEstudiante  {} nombreEstudiante  {} ApellidoEstudiante  {} Semestre_cursando  {}'.format(self.cod_estudio,self.nombre_est,self.apellido_est,self.quesemestre)
    class Meta:
        managed = False
        db_table = 'estudiante'



class Materia(models.Model):
    cod_materia = models.IntegerField(primary_key=True,default=ObtenerSequencia('materia'))
    nombre_materia = models.CharField(max_length=45, blank=False, null=False)
    creditos = models.IntegerField(blank=False, null=False)
    semestre_id = models.IntegerField(blank=False, null=False)
    activo = models.BooleanField(blank=False, null=False,default=True)
    def __str__(self):
        return 'cod_materia{} {} {} {}'.format(self
                                    .cod_materia,self.nombre_materia,self.creditos,self.semestre_id,self.activo)
    print(str(cod_materia.__str__())+"::::::MAteria:::::")
    class Meta:
        managed = False
        db_table = 'materia'
        unique_together=(('cod_materia'),)

class DocentesEnSemestre(models.Model):
    id_semestre = models.ForeignKey('Semestre', models.DO_NOTHING,unique=True,to_field='id_semestre',related_name='id_semestre_doc_sem', db_column='id_semestre', primary_key=True)
    cedula_doc = models.ForeignKey(Docentes, models.DO_NOTHING,unique=True,to_field='cedula',related_name='cedula_doc_sem', db_column='cedula_doc')
    def __str__(self):
        return '{} {}'.format(self.id_semestre,self.cedula_doc)
    class Meta:
        managed = False
        db_table = 'docentes_en_semestre'
        unique_together = (('id_semestre', 'cedula_doc'),)


class Estudianteysemestre(models.Model):
    id_semestre = models.ForeignKey('Semestre', models.DO_NOTHING,unique=True,to_field='id_semestre',related_name='Estudiante_sem_id', db_column='id_semestre', primary_key=True)
    cod_estudio = models.ForeignKey(Estudiante, models.DO_NOTHING,unique=True,to_field='cod_estudio',related_name='Estudiante_sem_cod', db_column='cod_estudio')
    print(str(id_semestre.__str__())+":"+str(cod_estudio.__str__())+":--------Estudianteysemestre--------------------")
    def __str__(self):
        return '{} {}'.format(self.cod_estudio,self.id_semestre)
    class Meta:
        managed = False
        db_table = 'estudianteysemestre'
        unique_together = (('id_semestre', 'cod_estudio'),)




class Materiayestudiantes(models.Model):
    cod_materia = models.ForeignKey(Materia,models.DO_NOTHING, to_field='cod_materia',unique=True,related_name='Materiasy_est_cod_mat',db_column='cod_materia')
    cod_estudio = models.ForeignKey(Estudianteysemestre,models.DO_NOTHING,to_field='cod_estudio',unique=True,related_name='Materiasy_est_cod_est',db_column='cod_estudio')
    id_semestre = models.ForeignKey(Estudianteysemestre, models.DO_NOTHING,to_field='id_semestre',unique=True, related_name='Materiasy_est_cod_mat',db_column='id_semestre', primary_key=True)
    print(str(id_semestre.__str__())+":"+str(cod_estudio.__str__())+":"+str(cod_materia.__str__())+":--------Estudianteysemestre--------------------")
    def __str__(self):
        return '{} {} {}' .format(self.cod_estudio,self.cod_estudio,self.id_semestre)
    class Meta:
        managed = False
        db_table = 'materiayestudiantes'
        unique_together = (('id_semestre', 'cod_estudio', 'cod_materia'),)



class Notas(models.Model):
    tipodenota = models.CharField(primary_key=True, max_length=75)
    notas = models.IntegerField(blank=False, null=True)
    cod_materia = models.ForeignKey(Materiayestudiantes,models.DO_NOTHING,unique=True,to_field='cod_materia',
                                    related_name='cod_materia_notas',db_column='cod_materia')
    cod_estudio = models.ForeignKey(Materiayestudiantes ,models.DO_NOTHING,unique=True,to_field='cod_estudio',
                                    related_name='cod_estudi_notas',db_column='cod_estudio')
    id_semestre = models.ForeignKey(Materiayestudiantes, models.DO_NOTHING,to_field='id_semestre',
                                    related_name='id_semestre_notas',db_column='id_semestre')
    cedula_doc = models.ForeignKey(DocentesEnSemestre, models.DO_NOTHING,unique=True,to_field='cedula_doc',
                                   related_name='cedula_notas',db_column='cedula_doc')
    print(str(id_semestre.__str__())+":"+str(cod_estudio.__str__())+":"+str(cod_materia.__str__())+":--------Notas--------------------")


    def __str__(self):
        return '{} {} {} {}'.format(self.id_semestre,self.cod_estudio,self.cedula_doc,self.tipodenota,self.notas)
    class Meta:
        managed = False
        db_table = 'notas'
        unique_together = (('tipodenota', 'cod_materia', 'cod_estudio', 'id_semestre','cedula_doc'),)

