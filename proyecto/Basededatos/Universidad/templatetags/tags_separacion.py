from django import template

from Basededatos.Universidad.models import Estudianteysemestre,Docentes,Estudiante
from django.core.serializers import json
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def define(val=None):
  return val

@register.simple_tag
def default_estudiantes():
  var=Estudianteysemestre.objects.all()
  retornar= var[0]
  print(str(var)+"default_estudiantes________________________________--")
  return retornar

@register.simple_tag
def Materiasyestudiantes_tag(declaraciones:int =0):
        var=Estudianteysemestre.objects.filter(cod_estudio=declaraciones).order_by('cod_estudio').values()
        return var

@register.simple_tag
def sacarvalor(declaraciones:[]=None):
    print("sacar valores:"+declaraciones)
    return str('a')

@register.simple_tag
def SacarNombredocente(cedula:int):
    valor=Docentes.objects.filter(cedula=cedula).values() #type:{ }
    return valor
@register.filter(name='nomEstud')
def SacarnombresEstudiantes(cod_estudio:int):
    if(cod_estudio):
        return ' N '+str(Estudiante.Str(cod_estudio))
    else :
        return 'Error en los datos'
