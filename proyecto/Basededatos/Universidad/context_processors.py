
from Basededatos.Universidad.models  import Materiayestudiantes as estu_mate

def cod_estudiante(request):
     var=estu_mate.objects.filter('id_semestre')
     return var