from django.conf.urls import  url
from Basededatos.Universidad import views


urlpatterns = [
    url(r'^$',views.Index,name='index'),
    url(r'^Nuevodocente$',views.Crear_Docente,name="Nuevos_docentes"),
    url(r'^NuevoEstudiante$', views.Crear_Estudiantes, name="Nuevos_estudiante"),
    url(r'^NuevaMateria$', views.Crear_Materia, name="Nuevos_Materia"),
    url(r'^InscrProfesores_semestre$', views.Crear_enlace_profesorSemestre, name="Docentes_ensemestre"),
    url(r'^ValidacionDeEstudiantes_validos$', views.Crear_enlace_SemestreyEstudiante, name="SemestreyEstudiante"),
    url(r'^Inscrestudiantes$', views.Crear_Materiayestudiantes, name="Materiayestudiantes"),
    url(r'^Inscrestudiantes/(?P<id_semestre>\d+)/(?P<cod_materia>\d+)/$',views.Crear_Materiayestudiantes2,name="Materiayestudiantes2"),
    url(r'^NuevaNotas$', views.Crear_Notas, name="Nuevanotas"),
    url(r'^Docentes_listar$',views.Listar_docentes,name="listar-docentes"),
    url(r'^Docentes_Modificar/(?P<cedula>\d+)/$', views.Actualizar_docentes, name="actualizar-docentes"),
    url(r'^Materias_listar$',views.Listar_Materia,name='Listarmateria'),
    url(r'Modificar_materia/(?P<cod_materia>\d+)/$',views.Actualizar_Materia,name='ActMateria'),
    url(r'^Listar_estudiantes$',views.Listar__estudiantes,name='Listar_estudiantes'),
    url(r'^Modificar_estudiates',views.Modificar_estudiates,name='Modificar_estudiates'),
    url(r'^InscribirEstudoiantesmateria$',views.prueba2,name='prueba'),
    url(r'^prueba2$', views.CrearyusarMateriayestudiante, name='prueba2'),
    url(r'^prueba$',views.Prueba,name='prueba-notas'),
    url(r'^Peticionesajax$',views.procesarjson_procesar,name='json_pruebas'),
    url(r'^CrearNotas$',views.Crear_notas_tipo,name='notas_tipo')
]

"""
Creado
Docentes
crear:nuevo deocente
listar:Docentes_listar
Actualizar:Docentes_modificar
Eliminar:-------

Estudiante
crear:nuevo estudiante
lista:listar estudiantes
Actualizar:Modificar_estudiates

Materia
crear:nueva materia
Listar:Listar_estudiantes
actualizar:Modificar_estudiates
Eliminar:

Materiaydocentes

Semestreyestudiantes
Crear:ValidacionDeEstudiantes_validos
Listar
Actualizar:
Eliminar
Semestreyestudoiantesymateria



Notas





falta
loguin

"""