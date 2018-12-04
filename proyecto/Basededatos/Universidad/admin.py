from django.contrib import admin

# Register your models here.
from .models import *


class materiasAdmin(admin.ModelAdmin):
	fields = ("nombre_materia","semestre_id", "activo")
	list_display = ("cod_materia","nombre_materia")
	search_fields = ("cod_materia" , "nombre_materia")
	list_filter = ("semestre_id", "activo")

class semestreAdmin(admin.ModelAdmin):
	fields=("periodo","año","novedades")
	list_display=("id_semestre","periodo","año")
	search_fields=("año","periodo","id_semestre")
	list_filter=("año","periodo","id_semestre")
class docentesAdmin(admin.ModelAdmin):
	fields = ('cedula','nombre_doc','apellido_doc','celular','password')
	list_display = ("cedula","nombre_doc","apellido_doc","celular")
	list_filter=("cedula","nombre_doc","apellido_doc")
	search_fields=("cedula","nombre_doc","apellido")

class NotasAdmin(admin.ModelAdmin):
	list_display = ("tipodenota","cedula_doc","cod_estudio","id_semestre","notas")
	search_fields=("tipodenota","cedula_doc","cod_estudio","id_semestre")
	list_filter=("tipodenota","cedula_doc","cod_estudio","id_semestre")
class DocentesEnSemestre_admin(admin.ModelAdmin):
	list_display = ('id_semestre','cedula_doc')

	list_filter=('id_semestre','cedula_doc')
	search_fields=('id_semestre','cedula_doc')

class EstudiantesEnSemestre_admin(admin.ModelAdmin):
	fields = ('id_semestre','cod_estudio')
	list_display = ('id_semestre','cod_estudio')
	list_filter = ('id_semestre','cod_estudio')
	search_fields = ('id_semestre','cod_estudio')
class MAteria_semestre_docenteAdmin(admin.ModelAdmin):
	fields = ()
#admin.site.register(Materia,holaperro)
admin.site.register(Materia,materiasAdmin)
admin.site.register(Semestre,semestreAdmin)
admin.site.register(Docentes,docentesAdmin)
admin.site.register(Notas,NotasAdmin)
admin.site.register(DocentesEnSemestre,DocentesEnSemestre_admin)
admin.site.register(Estudianteysemestre,EstudiantesEnSemestre_admin)
