
from django import forms
from django.contrib.auth.admin import UserAdmin
from .models import Estudiante,Materia,Docentes,Estudianteysemestre,Materiayestudiantes,DocentesEnSemestre,Notas

#manipulacion de docentes
class Formas_entrada_Docentes(forms.ModelForm):
    class Meta:

        model= Docentes
        fields=[
            'cedula',
            'nombre_doc',
            'apellido_doc',
            'contraseña',
            'celular',
        ]
        labels={
            'cedula' :'cedula',
            'nombre_doc':'Nombre del docente',
            'apellido_doc':'Apellido',
            'contraseña':'Contraseña',
            'celular':'Celular',
        }
        widgets={
            'cedula':forms.NumberInput(attrs={'class':'form-control','min':'999999999'}),
            'nombre_doc':forms.TextInput(attrs={'class':'form-control'}),
            'apellido_doc':forms.TextInput(attrs={'class':'form-control'}),
            'contraseña':forms.PasswordInput(attrs={'class':'form-control'}),
            'celular':forms.NumberInput(attrs={'class':'form-control','min':'99999','max':'9999999999'}),
        }


#formas para datos de estudiantes
class Formas_entrada_Estudiante(forms.ModelForm):

    class Meta:
        model=Estudiante

        fields=[
            'nombre_est',
            'apellido_est',
            'quesemestre'
        ]
        labels={
            'nombre_est':'Nombre del Estudiante',
            'apellido_est': 'Apellido Estudiante',
            'quesemestre': 'Semestre'
        }
        widgets={

        'nombre_est': forms.TextInput( attrs={'class':'form-control'}),
        'apellido_est':forms.TextInput( attrs={'class':'form-control'}),
        'quesemestre':forms.NumberInput(attrs={'class':'form-control'})
        }
#formas para entrada de materias
class Fromas_entradaMaterias(forms.ModelForm):


    class Meta:
        model=Materia
        fields = [
            'nombre_materia',
            'creditos',
            'semestre_id',
            'activo'
        ]
        labels = {
            'nombre_materia':'Nombre De la Materia',
            'creditos':'Creditos',
            'semestre_id':'Semestre ',
            'activo':'Activo'
        }
        widgets = {
            'nombre_materia':forms.TextInput(attrs={'class':'form-control'}),
            'creditos':forms.NumberInput(attrs={'class':'form-control','min':'1','max':'8'}),
            'semestre_id':forms.NumberInput(attrs={'class':'form-control','min':'1','max':'12'}),
            'activo': forms.CheckboxInput(attrs={'class':'form-control'})

        }

class Formas_DocentesEnSemestre(forms.ModelForm):
    class Meta:
        model=DocentesEnSemestre
        fields=['id_semestre','cedula_doc',]
        label={
            'id_semestre':'Semestre ',
            'cedula_doc':'Codigo de la materia'
        }
        widgets={
            'id_semestre':forms.Select(attrs={'class': 'form-control'}),
            'cedula_doc':forms.Select(attrs={'class': 'form-control'})
        }


class Formas_Estudianteysemestre(forms.ModelForm):
    class Meta:
        model = Estudianteysemestre
        fields = ['id_semestre','cod_estudio']
        label = {
            'cod_estudio':'Codigo de estudio',
            'id_semestre':'Semestre'
        }
        widgets = {
            'id_semestre':forms.Select(attrs={'class': 'form-control'}),
            'cod_estudio':forms.Select(attrs={'class': 'form-control'}),
        }


#formas para entrada de estudiantes y materias
class Formas_Materiayestudiantes(forms.ModelForm):

    class Meta:
      model=Materiayestudiantes
      fields=[
          'cod_materia','cod_estudio','id_semestre'
      ]
      label={
          'cod_materia':'codigo de la materia',
          'cod_estudio':'cedula del docente',
          'id_semestre':'Semestre perteneciente'
      }
      widgets={
        'cod_materia' : forms.Select(attrs={'class': 'form-control'}),
        'id_semestre ': forms.Select(attrs={'class': 'form-control'}),
        'cod_estudio':  forms.Select(attrs={'class': 'form-control'})
     }
#formas para ingresar docente en semestre


class Formas_entrada_Notas(forms.ModelForm):


    class Meta:
        model=Notas
        fields=[

            'cod_materia',
            'cod_estudio',
            'id_semestre',
            'cedula_doc',
            'tipodenota',
            'notas'
        ]
        labels={
            'cod_materia': 'Codigo De Materia',
            'cod_estudio': 'Codigo Estudiantes',
            'id_semestre': 'Codigo Semestre',
            'cedula_doc': 'Cedula del Docente',
            'tipodenota':'Tipos De notas',
            'notas':'Notas'

        }
        widgets={

            'cod_materia': forms.Select(attrs={'class':'form-control'}),
            'cod_estudio': forms.Select(attrs={'class':'form-control'}),
            'id_semestre': forms.Select(attrs={'class':'form-control'}),
            'cedula_doc':  forms.Select(attrs={'class':'form-control'}),
            'tipodenota':  forms.TextInput(attrs={'class':'form-control'}),
            'notas': forms.NumberInput(attrs={'class':'form-control','min':'0','max':'5'})
        }

