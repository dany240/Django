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
    url(r'^NuevaNotas$', views.Crear_Notas, name="Nuevos_Materia"),
    url(r'^Docentes_listar$',views.Listar_docentes,name="listar-docentes"),
    url(r'^Docentes_Modificar/(?P<cedula>\d+)/$', views.Actualizar_docentes, name="actualizar-docentes"),
    url(r'^Materias_Listar$',views.Listar_Materia,name='Listar-materia'),
    url(r'^prueba$',views.Actualizar_Notas,name='prueba-notas')

]
