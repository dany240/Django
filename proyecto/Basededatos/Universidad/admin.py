from django.contrib import admin

# Register your models here.
from .models import *


class materiasAdmin(admin.ModelAdmin):
	list_display = ("cod_materia","nombre_materia")
	search_fields = ("cod_materia" , "nombre_materia")
	list_filter = ("semestre_id", "activo")

class semestreAdmin(admin.ModelAdmin):
	list_display=("id_semestre","periodo","año")

"""class docentesAdmin(admin.ModelAdmin):
	list_display = ("cedula","nombre_doc")"""

class NotasAdmin(admin.ModelAdmin):
	list_display = ("tipodenota","cedula_doc")

class DocentesEnSemestre_admin(admin.ModelAdmin):
	list_display = ('id_semestre','cedula_doc')

#admin.site.register(Materia,holaperro)
admin.site.register(Materia,materiasAdmin)
admin.site.register(Semestre,semestreAdmin)
#admin.site.register(Docentes,docentesAdmin)
admin.site.register(Notas,NotasAdmin)
admin.site.register(DocentesEnSemestre,DocentesEnSemestre_admin)
