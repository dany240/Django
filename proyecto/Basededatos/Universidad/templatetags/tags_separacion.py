from django import template

from Basededatos.Universidad.models import Estudianteysemestre

register = template.Library()

@register.simple_tag
def define(val=None):
  return val

@register.simple_tag
def default_estudiantes():
  var=Estudianteysemestre.objects.all()
  print(var+"default_estudiantes________________________________--")
  return var
