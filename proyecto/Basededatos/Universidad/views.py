from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.contrib.auth.models import User
from django.db import connection
from   .Utilidades import Encriptar
from   .models import *
from   .templatetags.tags_separacion import *
from   .forms import Formas_entrada_Docentes,Formas_entrada_Notas,Fromas_entradaMaterias,Formas_entrada_Estudiante,Formas_DocentesEnSemestre,Formas_Estudianteysemestre,Formas_Materiayestudiantes
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

def Listar_docentes(request):
    docentes=Docentes.objects.all().order_by('cedula')
    context={'docentes_mostrar':docentes}
    return  render (request,'Busqueda/Resultados_docentes.html',context)
def Actualizar_docentes(request,cedula):

     actualizardocente=Docentes.objects.get(cedula=cedula)
     if (request.method == 'GET'):
         form = Formas_entrada_Docentes( instance= actualizardocente)

     else:
         form = Formas_entrada_Docentes(request.POST, instance=actualizardocente)
         if (form.is_valid()):

            forma=form.cleaned_data

            if not(Validar_existencia_multiple("docentes","cedula",(forma.get('cedula')))):
                Coneccion = connection
                dato=Coneccion.cursor()
                dato.execute('update docentes set cedula= %s , nombre_doc= %s , apellido_doc =%s , contraseña= %s ,celular=%s where cedula =%s',
                             [forma.get('cedula'),forma.get('nombre_doc'),forma.get('apellido_doc'),forma.get('contraseña'),forma.get('celular'),forma.get('cedula')])
                Coneccion.commit()
                dato.close()
                Coneccion.close()
                print("Antes de responder")
                return redirect('listar-docentes')
         else:
                messages.error(request, 'La Cedula que usted dijito esta repetida con otro registro ')
                print("Varios___________________________________________________________________")
     return render(request, 'Crear/Crear.html', {'form': form})



def Ocultar_docentes(request,cedula):

    Usuarios=User.objects.get(cedula=cedula)
    if(request.method=='POST'):
        Usuarios.is_staff





def Crear_Materia(request):
    if request.method == 'POST':
        form=Fromas_entradaMaterias(request.POST)
        if(form.is_valid()):
            form.save()
        return redirect('index')
    else:
         form=Fromas_entradaMaterias()
    return render(request,'Crear/Crear.html',{'form':form})

def Listar_Materia(request):
    materias=Materia.objects.all().order_by('cod_materia')
    context={'Materia_listar':materias}
    return  render (request,'Busqueda/Materias.html',context)
def Actualizar_Materia(request):
    pass

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

def Listar_Notas(request):
    pass


def Actualizar_Notas(request):
    if(request.method=='POST'):
         print(request.body)
         for var in (request.POST.items()):
             print(var)
         return redirect('index')
    else:
        dato=Estudianteysemestre.objects.all()
        print(str(dato)+"_____________________________________________________________________dato")
        form = Formas_Materiayestudiantes()

    return render(request,'Crear/prueba.html',{'form':form,'Datos':dato})



def Eliminar_Notas(request):
    pass




def Crear_Estudiantes(request):
    if request.method == 'POST':
        form=Formas_entrada_Estudiante(request.POST)
        if(form.is_valid()):
            form.save()
        return redirect('index')
    else:
         form=Formas_entrada_Estudiante()
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
        form=Formas_Materiayestudiantes(request.POST)
        if (form.is_valid()):
            form.save()
        return redirect('index')
    else:
         form = Formas_Materiayestudiantes()

         return render(request, 'Crear/Crear_materiasyestudiantes.html', {'form': form})


def Validar_existencia_multiple(Tabla,Fila,Valor):
    dato = connection.cursor()
    Stringparamentro='select * from '+str(Tabla)+' where '+str(Fila)+' = %s'
    dato.execute(Stringparamentro,[str(Valor)] )
    print(dato.query)
    valor = dato.fetchall()
    dato.close()

    if(len(valor)>1 ): return True
    else:return False

def __FiltrarLLaveforanea(form,form1,comparar):
    """ """
    var=form
    pass