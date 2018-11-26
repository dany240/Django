from django.conf.urls import  url
from Basededatos.Universidad import views


urlpatterns = [
    url(r'^$',views.Index,name='index'),
    url(r'^Nuevodocente$',views.Crear_Docente,name="Nuevos_docentes"),
    url(r'^NuevoEstudiante$', views.Crear_Estudiantes, name="Nuevos_estudiante"),
    url(r'^NuevaMateria$', views.Crear_Materia, name="Nuevos_Materia"),
    url(r'^InscrProfesores_semestre$', views.Crear_enlace_profesorSemestre, name="Docentes_ensemestre"),
    url(r'^ValidacionDeEstudiantes_validos$', views.Crear_enlace_SemestreyEstudiante, name="SemestreyEstudiante"),
    url(r'^Inscr$$', views.Crear_Materiayestudiantes, name="Materiayestudiantes"),
    url(r'^NuevaNotas$', views.Crear_Notas, name="Nuevos_Materia")

]
