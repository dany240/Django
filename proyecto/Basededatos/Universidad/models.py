# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' orderm
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import timezone

import psycopg2
from django.core.validators import *
from django.db import models,connection



from django.db import models
from django.contrib.auth.models import User

def ObtenerSequencia(valor):
    diccionario={'materia':'se_materia',
                 'id_semestre':'se_id_semestre',
                 'id_estudiante':'indiceEstudiante',
                 'año':'se_año',
                 'periodo':'se_periodo',
                 'notas':'notas_id_seq',
                 'materiayestudiante':'materiayestudiantes_registro_seq'

                 }
    dato=connection.cursor()
    dato.execute("select nextval( %s )",[diccionario[valor]])
    valor=dato.fetchone()[0]
    dato.close()
    return int(valor)

class Docentes(models.Model):
    cedula = models.BigIntegerField(primary_key=True, db_column='cedula')
    nombre_doc = models.CharField(max_length=45, blank=False, null=False, db_column='nombre_doc')
    apellido_doc = models.CharField(max_length=45, blank=False, null=False, db_column='apellido_doc')
    contraseña = models.CharField(max_length=45, blank=False, null=False, db_column='contraseña')
    celular = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True, db_column='celular')

    @staticmethod
    def Str(cedula:int):
        var = Docentes.objects.get(cedula=int(cedula)) #type: Docente
        return '{} '.format(var.nombre_doc)
    def __str__(self):
        return '{} {}'.format(str(self.nombre_doc),str(self.apellido_doc))
    class Meta:
        managed = False
        db_table = 'docentes'




def Str(Dato,tabla,columna):
    conexion=connection.cursor()
    try:
     conexion.execute("select %s from %s where %s = %s ",[columna,tabla ,columna,Dato])
     valor = conexion.fetchone()[0]
     conexion.close()
    except psycopg2.ProgrammingError as Error:
     print(conexion.query)
     valor=''
    return str(valor)


class Semestre(models.Model):
    valores=(
        ('Sin novedad','Sin novedad'),
        ('Anormalidad Academica','Paro'),
        ('Semestre Canselado','Semestre Cancelado')
    )
    id_semestre = models.IntegerField(primary_key=True,default=ObtenerSequencia('id_semestre'),db_column='id_semestre')
    año = models.IntegerField(blank=False, null=False,default=ObtenerSequencia('año'),db_column='año',validators=[MinValueValidator(limit_value=0,message="Rango menor a lo esperado")])
    novedades = models.CharField(max_length=45, blank=False, null=True,db_column='novedades',default='Sin Novedades',choices=valores)
    periodo = models.IntegerField(blank=False, null=False,default=ObtenerSequencia('periodo'),db_column='periodo',validators=[MaxValueValidator(limit_value=4,message="Solo existe periodo max periodo de 4 sin novedades ")])
    @staticmethod
    def Str(id_semestre):
        var = Semestre.objects.get(id_semestre=int(id_semestre))
        return '{} --- {}'.format(var.año, var.periodo)

    def __str__(self):
        return  'año :{} periodo :{}'.format(self.año,self.periodo)
    class Meta:
        managed = False
        db_table = 'semestre'
        unique_together=(("año","periodo"),)


class Estudiante(models.Model):
    cod_estudio = models.IntegerField( primary_key=True,default=ObtenerSequencia('id_estudiante'))
    nombre_est = models.CharField(max_length=45, blank=False, null=False)
    apellido_est = models.CharField(max_length=45, blank=False, null=False)
    quesemestre = models.IntegerField(blank=False, null=False)

    @staticmethod
    def Str(cod_estudio):
      var=Estudiante.objects.get(cod_estudio=int(cod_estudio))
      return '{} {}'.format(var.nombre_est,var.apellido_est)
    class Meta:
        managed = False
        db_table = 'estudiante'



class Materia(models.Model):
    cod_materia = models.IntegerField(primary_key=True,default=ObtenerSequencia('materia'))
    nombre_materia = models.CharField(max_length=45, blank=False, null=False)
    creditos = models.IntegerField(blank=False, null=False)
    semestre_id = models.IntegerField(blank=False, null=False)
    activo = models.BooleanField(blank=False, null=False,default=True)
    @staticmethod
    def Str(cod_materia):
      var=Materia.objects.get(cod_materia=int(cod_materia))
      return '{}'.format(var.nombre_materia)
    def __str__(self):
        return '{}'.format(str(self.nombre_materia))


    class Meta:
        managed = False
        db_table = 'materia'
        unique_together=(('cod_materia'),)

class DocentesEnSemestre(models.Model):
    id= models.AutoField(primary_key=True,db_column='id')
    id_semestre = models.OneToOneField(Semestre, models.DO_NOTHING,to_field='id_semestre',related_name='id_semestre_doc_sem', db_column='id_semestre')
    cedula_doc = models.OneToOneField(Docentes, models.DO_NOTHING,to_field='cedula',related_name='cedula_doc_sem', db_column='cedula_doc')
    def __str__(self):
         return 'el semestre{}  docente:{}'.format(self.id_semestre,
                                                   Docentes.Str(self.cedula_doc.cedula))
    class Meta:
        managed = False
        db_table = 'docentes_en_semestre'
        unique_together = (('id_semestre', 'cedula_doc'),)


class Estudianteysemestre(models.Model):
    id= models.AutoField(primary_key=True,db_column='id')
    id_semestre = models.OneToOneField(Semestre, models.DO_NOTHING,to_field='id_semestre',related_name='Estudiante_sem_id', db_column='id_semestre') #type: models.OneToOneField
    cod_estudio = models.OneToOneField(Estudiante, models.DO_NOTHING,to_field='cod_estudio',related_name='Estudiante_sem_cod', db_column='cod_estudio')
    print(str(id_semestre.__str__())+":"+str(cod_estudio.__str__())+":--------Estudianteysemestre--------------------")
    def __str__(self):

        return '{} {}'.format(
                               Estudiante.Str(self.cod_estudio.cod_estudio),
                               Semestre.Str(self.id_semestre.id_semestre)
        )
    @staticmethod
    def Str(id_semestre:int,cod_estudio:int):
        return '{}  {} '.format(Semestre.Str(id_semestre.id_semestre),Estudiante.Str(cod_estudio.cod_estudio))
    @staticmethod
    def Str_id_semestre(id_semestre:int):
        return '{}'.format(Semestre.Str(id_semestre))
    @staticmethod
    def Str_cod_estudio(cod_estudio):
        return '{}'.format(Estudiante.Str(cod_estudio))
    class Meta:
        managed = False
        db_table = 'estudianteysemestre'
        unique_together = (('id_semestre', 'cod_estudio'),)




class Materiayestudiantes(models.Model):
    registro = models.AutoField (primary_key=True,db_column='registro',default=ObtenerSequencia('materiayestudiante'))
    cod_materia = models.OneToOneField(Materia,models.DO_NOTHING,to_field='cod_materia',related_name='Materiasy_est_cod_mat',db_column='cod_materia')
    cod_estudio = models.OneToOneField(Estudianteysemestre,models.DO_NOTHING,to_field='cod_estudio',related_name='Materiasy_est_cod_est',db_column='cod_estudio')
    id_semestre = models.OneToOneField(Estudianteysemestre, models.DO_NOTHING,to_field='id_semestre', related_name='Materiasy_est_cod_mat',db_column='id_semestre')
    print(str(id_semestre.__str__())+":"+str(cod_estudio.__str__())+":"+str(cod_materia.__str__())+":--------Estudianteysemestre--------------------")


    def __str__(self):
        return 'Materia: {} {} ' .format(
        Materia.Str( self.cod_materia.cod_materia),
        Estudianteysemestre.Str(self.id_semestre.id_semestre,self.cod_estudio.cod_estudio)
        )
    class Meta:
        managed = False
        db_table = 'materiayestudiantes'
        unique_together = ('id_semestre', 'cod_estudio', 'cod_materia')



class Notas(models.Model):
    id =models.AutoField(primary_key=True,db_column='id',default=ObtenerSequencia('notas'))
    tipodenota = models.CharField(max_length=75)
    notas = models.IntegerField(blank=False, null=True)
    cod_materia = models.OneToOneField(Materiayestudiantes,models.DO_NOTHING, to_field='cod_materia',
                                    related_name='cod_materia_notas',db_column='cod_materia')
    cod_estudio = models.OneToOneField(Materiayestudiantes ,models.DO_NOTHING,to_field='cod_estudio',
                                    related_name='cod_estudi_notas',db_column='cod_estudio')
    id_semestre = models.OneToOneField(Materiayestudiantes, models.DO_NOTHING,to_field='id_semestre',
                                    related_name='id_semestre_notas',db_column='id_semestre')
    cedula_doc = models.OneToOneField(DocentesEnSemestre, models.DO_NOTHING,to_field='cedula_doc',
                                   related_name='cedula_notas',db_column='cedula_doc')
    porcentaje=models.DecimalField(max_digits=3,decimal_places=2,blank=None,null=None,db_column='porcentaje')


    def __str__(self):
        return '{} {} {} {}'.format(self.id_semestre,self.cod_estudio,self.cedula_doc,self.tipodenota,self.notas)
    class Meta:
        managed = False
        db_table = 'notas'
        unique_together = (('tipodenota', 'cod_materia', 'cod_estudio', 'id_semestre','cedula_doc'),)

