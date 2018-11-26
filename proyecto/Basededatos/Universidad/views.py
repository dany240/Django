from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.contrib.auth.models import User
from django.db import connection
from  Basededatos.Universidad.Encriptar import Encriptar
from  Basededatos.Universidad.models import Docentes
from  Basededatos.Universidad.forms import Formas_entrada_Docentes,Formas_entrada_Notas,Fromas_entradaMaterias,Formas_entrada_Estudiante,Formas_DocentesEnSemestre,Formas_Estudianteysemestre,Formas_Materiayestudiantes
# Create your views here.

def Index (request):
    return render(request,'Pantalla principal.html')



def Crear_Docente(request):
    if request.method == 'POST':
        form=Formas_entrada_Docentes(request.POST)
        if(form.is_valid()):
            forma=form.cleaned_data
            docente=Docentes(cedula=forma.get('cedula'),nombre_doc=forma.get('nombre_doc'),apellido_doc=forma.get('apellido_doc'),contraseña=Encriptar(forma.get('contraseña')),celular=forma.get('celular'))
            Usuario=User.objects.create_user(forma.get('cedula'),password=forma.get('contraseña'))
            Usuario.is_superuser = False
            Usuario.is_staff=False
            docente.save()
            Usuario.save()
            return redirect('index')
    else:
         form=Formas_entrada_Docentes()
    return render(request,'Crear/Crear.html',{'form':form})


def Crear_Materia(request):
    if request.method == 'POST':
        form=Fromas_entradaMaterias(request.POST)
        if(form.is_valid()):
            form.save()
        return redirect('index')
    else:
         form=Fromas_entradaMaterias()
    return render(request,'Crear/Crear.html',{'form':form})


def Crear_Notas(request):
    if request.method == 'POST':
        form=Formas_entrada_Notas(request.POST)
        if(form.is_valid()):
            form.save()
        return redirect('index')
    else:
         form=Formas_entrada_Notas()
         print(form)
    return render(request,'Crear/Crear.html',{'form':form})

def Crear_Estudiantes(request):
    if request.method == 'POST':
        form=Formas_entrada_Estudiante(request.POST)
        if(form.is_valid()):
            form.save()
        return redirect('index')
    else:
         form=Formas_entrada_Notas()
    return render(request,'Crear/Crear.html',{'form':form})

def Crear_enlace_profesorSemestre(request):
    if(request.method=='POST'):
        form=Formas_DocentesEnSemestre(request.POST)
        if (form.is_valid()):
            form.save()
        return redirect('index')
    else:
         form = Formas_DocentesEnSemestre()
         return render(request, 'Crear/Crear.html', {'form': form})

def Crear_enlace_SemestreyEstudiante(request):
    if(request.method=='POST'):
        form=Formas_Estudianteysemestre(request.POST)
        if (form.is_valid()):
            form.save()
        return redirect('index')
    else:
         form = Formas_Estudianteysemestre()
         return render(request, 'Crear/Crear.html', {'form': form})

def Crear_Materiayestudiantes(request):
    if(request.method=='POST'):
        form=Formas_Estudianteysemestre(request.POST)
        if (form.is_valid()):
            form.save()
        return redirect('index')
    else:
         form = Formas_Estudianteysemestre()
         return render(request, 'Crear/Crear.html', {'form': form})


def __Validar_existencia(Tabla,Fila,Valor):
    dato = connection.cursor()
    dato.execute("select * %s where %s = %s",[Tabla,Fila,Valor] )
    valor = dato.fetchall()
    dato.close()
    if(valor != None): return True
    else:return False