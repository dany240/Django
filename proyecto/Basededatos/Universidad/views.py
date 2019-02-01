from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse, HttpRequest, Http404, JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.contrib.auth.models import User
from django.db import connection, ProgrammingError
from django.core import serializers
from   .Utilidades import Encriptar
import json as JSON_Dar
from   .models import *

from   .templatetags.tags_separacion import *
from   .forms import Formas_entrada_Docentes,Formas_entrada_Notas,Fromas_entradaMaterias,Formas_entrada_Estudiante,Formas_DocentesEnSemestre,Formas_Estudianteysemestre,Formas_Materiayestudiantes
# Create your views here.

def Index (request):
    return render(request,'Pantalla principal.html')

#-___--_____________________________________________-------------------------------------__Docentes
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

            forma=form.cleaned_data #type:Formas_entrada_Docentes.cleaned_data

            if not(Validar_existencia_multiple("docentes","cedula",(forma.get('cedula')))):
                Coneccion = connection
                dato=Coneccion.cursor()
                dato.execute('update docentes set cedula= %s , nombre_doc= %s , apellido_doc =%s , contraseña= %s ,celular=%s where cedula =%s',
                             [forma.get('cedula'),forma.get('nombre_doc'),forma.get('apellido_doc'),forma.get('contraseña'),forma.get('celular'),cedula])
                Coneccion.commit()
                dato.close()
                Coneccion.close()
                cambiar_usuario=  User.objects.get(username=cedula) #type: User
                cambiar_usuario.username=forma.get('cedula')
                cambiar_usuario.set_password(forma.get('contraseña'))
                return redirect('listar-docentes')
         else:
                messages.error(request, 'La Cedula que usted dijito esta repetida con otro registro ')
                print("Varios___________________________________________________________________")
     return render(request, 'Crear/Crear.html', {'form': form})



def Ocultar_docentes(request,cedula):

    Usuarios=User.objects.get(cedula=cedula) #type: User
    if(request.method=='POST'):
        Usuarios.is_active=False
    redirect('index')


#---------------------------------------------------------------------------------MAteria


def Crear_Materia(request:HttpRequest):
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
    return render(request, 'Busqueda/Materias.html', context)


def Actualizar_Materia(request,cod_materia):
    actualizarmateria = Materia.objects.get(cod_materia=cod_materia)
    if (request.method == 'GET'):
        form = Fromas_entradaMaterias(instance=actualizarmateria)
    else:
        form = Fromas_entradaMaterias(request.POST, instance=actualizarmateria)
        if (form.is_valid()):
            form.save()
            return redirect('Listarmateria')
        else:
            messages.error(request, 'error en el formato')
            print("Varios___________________________________________________________________")
    return render(request, 'Crear/Crear.html', {'form': form})


#------------------------------------------------------------------------------------Estudiantes



def Crear_Estudiantes(request):
    if request.method == 'POST':
        form=Formas_entrada_Estudiante(request.POST)
        if(form.is_valid()):
            form.save()
        return redirect('index')
    else:
         form=Formas_entrada_Estudiante()
    return render(request,'Crear/Crear.html',{'form':form})

def Listar__estudiantes(request):
     estudiantes = Estudiante.objects.all().order_by('nombre_est')
     context = {'estudiantes_listar': estudiantes}
     return render(request, 'Busqueda/Estudiantes_inscritos.html', context)
def Modificar_estudiates(request,codigo):
    actualizarEstudiante = Estudiante.objects.get('cod_estudio')
    if request.method=="GET":
        forma=Formas_entrada_Estudiante(instance=actualizarEstudiante)

    else:
        forma=Formas_entrada_Estudiante(request.POST,instance=actualizarEstudiante)
        forma.save()
        redirect('Listar_estudiantes')
    return render('Crear/Crear.html',{'form':forma})



#-----------------------------------------Semesstreydocentes


def Crear_enlace_profesorSemestre(request:HttpRequest):
    if(request.method=='POST'):
        print(request.POST.dict())
        form=Formas_DocentesEnSemestre(request.POST)
        if (form.is_valid()):
            Datos_filtrados=request.POST.dict()
            Coneccion = connection
            dato = Coneccion.cursor()
            dato.execute('insert into docentes_en_semestre values ({},{}) '.format(Datos_filtrados['id_semestre'],Datos_filtrados['cedula_doc']))
            Coneccion.commit()
            dato.close()
            Coneccion.close()
            return redirect('index')
        else:
            messages.error(request,"mensaje")

    form = Formas_DocentesEnSemestre()
    return render(request, 'Crear/Crear.html', {'form': form})

def lista_enlace_profesor_semestre(request):
    profesorysemestre = DocentesEnSemestre.objects.all().order_by('id_semestre')
    context = {'Docysem': profesorysemestre}
    return render(request, 'Busqueda/Estudiantes_inscritos.html', context)


#semestre y estudiantes___------------------------------------------------------------------------------------------

def Crear_enlace_SemestreyEstudiante(request:HttpRequest):
    if(request.method=='POST'):
        form=Formas_Estudianteysemestre(request.POST) #type:Formas_entrada_Estudiante(request.POST)
        if (form.is_valid()):
            form.save()
            Avanzarsemestre(form.cleaned_data.get('cod_estudio'))
            print ("datos guardados"+str(form.cleaned_data))

            return redirect('index')
        else:
            messages.error(request,"error en los datos")
    else:
         form = Formas_Estudianteysemestre()
    return render(request, 'Crear/Crear.html', {'form': form})

def listarSemestreyestudiante(request):
    estudiantes = Estudianteysemestre.objects.all().order_by('nombre_est')
    context = {'estudiantes_listar': estudiantes} #type: context
    return render(request, 'Busqueda/Estudiantes_inscritos.html', context)
#-----------------------------------------------____----------------------------_Materiay estudiantes


def Crear_Materiayestudiantes(request:HttpRequest):#metodo encargado de decir la
    if(request.method=='POST'):
        print(request.POST.dict())
        id_semestre=int(request.POST.getlist('id_semestre')[0])
        cod_materia=int(request.POST.getlist('cod_materia')[0])
        if (id_semestre !=None and cod_materia != None):
         return HttpResponseRedirect('Inscrestudiantes/{}/{}'.format((id_semestre),(cod_materia)) )
    else:
          forma1 = Materia.objects.all().values() #type: Materia()
          forma2 = Formas_Estudianteysemestre
          return render(request, 'Crear/Crear_materiasyestudiantes.html', {'Materia': forma1,'estysem':forma2})


def Crear_Materiayestudiantes2(request:HttpRequest,id_semestre,cod_materia):
    #metodo encargado de decir la
    datosYaexistentes = Materiayestudiantes.objects.all().values('cod_estudio')
    formato = Estudianteysemestre.objects.filter(id_semestre=id_semestre).order_by('id_semestre').values(
        'cod_estudio')  # type: []
    excluir = []
    if (datosYaexistentes):
        for val in datosYaexistentes:
            excluir.append(val['cod_estudio'])
    excluir = tuple(excluir)
    print(excluir)
    id_semestre1 = Semestre.objects.filter(id_semestre=id_semestre)[0]  # type: Semestre
    cod_materia1 = Materia.objects.filter(cod_materia=cod_materia)[0]
    context = {'Estudiantes': formato, 'Semestre': id_semestre1, 'materia': cod_materia1, 'excluir': excluir}
    if(request.method=="POST"):

      cod_estudio= (request.POST.getlist('cod_estudio')[0])
      if(cod_estudio!=''):
        print(str(cod_estudio)+'--------------------------------')
        Coneccion = connection
        dato = Coneccion.cursor()
        dato.execute('insert into materiayestudiantes(cod_estudio,id_semestre,cod_materia) values ({},{},{}) '.format(
            cod_estudio,id_semestre,cod_materia
        ))
        Coneccion.commit()
        dato.close()
        Coneccion.close()

        return  redirect('index')
      else:
         messages.error(request,'Error no existen datos')


    return render(request,'Crear/crear_materiayestudaintefromato.html',context)

def Listar_Materiayestudiantes(request):
    materias=Materia.objects.all().order_by('cod_materia')
    context={'Materia_listar':materias}
    return  render (request,'Busqueda/Materias.html',context)

def Actualizar_materiayestudiantes(request,cod):
    pass





def CrearyusarMateriayestudiante(request:HttpRequest,dato):
    print(dato)
    return redirect('index')





























#Notas---------------------------------------------------------------

def Crear_Notas(request):
    if request.method == 'POST':
        form=Formas_entrada_Notas(request.POST)
        form=Formas_entrada_Notas(
            
        )
        if(form.is_valid()):
            print(str(form.cleaned_data)+"---------------------------------")
            form.save()
        return redirect('index')
    else:
         form=Formas_entrada_Notas()
         Maatyestu=Materiayestudiantes.objects.all()
         excluir= Notas.objects.all()
         for mat in Maatyestu:
             mat#type:Materiayestudiantes
             if(excluir!=None):
              for exc in excluir:
               print(mat==(exc))
               print(type(exc))


         context={}
    return render(request,'Crear/Crear.html',{'form':form})

def Crear_notas_tipo(request:HttpRequest):
    if(request.method=='POST'):
        n=Formas_entrada_Notas(request.POST)

    else:
        print()
        form=Formas_entrada_Notas()
        materiayseme=Materiayestudiantes.objects.all() #type:Materiayestudiantes
        materia=[]
        semestre=[]
        estudiante=[]
        profesorensemestre=DocentesEnSemestre.objects.all()

        for recorrer in materiayseme:
            materia.append(recorrer.cod_materia)


        return render(request,'Crear/Crear_notas.html',{'form':form})

def Listar_Notas(request):
     """
     
     :param request: 
     :return render:

  notas = Notas.objects.all().order_by('cod_materia') #type: Notas
        contexto = {'Materia_listar': Notas}#type: context
        return  render(request,'',contexto)

"""
     pass



def Actualizar_Notas(request):
    pass



def Eliminar_Notas(request):
    pass






def Validar_existencia_multiple(Tabla,Fila:[],Valor:[]) -> (bool):
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
def Prueba(request:HttpRequest) -> HttpResponse:
        """

        :type request: object
        """
        if (request.method == 'POST'):
            print(request.body)
            Valores =[] #type: []
            for llave,valor in (request.POST.items() ):
                llave,valor#type:str

                if(llave not in('id_semestre','csrfmiddlewaretoken','cod_materia')):
                     print(llave+"-"+valor)
                     Valores.append((llave,valor))

            return redirect('index')
        else:
            dato = Estudianteysemestre.objects.all().values()
            semestre = Estudianteysemestre.objects.all().values()
            form = Formas_Materiayestudiantes()
            return render(request, 'Crear/prueba.html', {'form': form, 'Datos': dato, 'semestre': semestre})


@csrf_exempt
def procesarjson_procesar(request:HttpRequest):
    if request.is_ajax()and  request.method=="POST":
        Datosreccibidos = request.POST.get('table')
        limpiardatos=JSON_Dar.loads(Datosreccibidos)
        obtener_datos_num=[] #type:[]
        for var in limpiardatos:
            obtener_datos_num.append(int(var))
            print(int(var))

        excluir=[]
        if(obtener_datos_num):
           datos_atomar= Estudianteysemestre.objects.all().values() #type: [{},{}]
           for recorrer in datos_atomar :
               recorrer#type:dict
               print(recorrer.get('cod_estudio_id')  )
               if(recorrer.get('cod_estudio_id') not in obtener_datos_num):
                   excluir.append(recorrer)
        else:
            var=Estudianteysemestre.objects.all().values()
            for recorrer in var:
                excluir.append(recorrer)
        if excluir==None : excluir.append(0)
        print(excluir)
        return  JsonResponse(serializers.serialize('json',excluir),safe=False)
    else:
        print(request)
        raise Http404

def prueba2(request):
    return redirect('prueba2',dato="lista")



def Avanzarsemestre(cod_estudio):
    conexion=connection.cursor() #type:connection
    connection.execute("select quesemestre from  estudiante where cod_estudio = %s",[cod_estudio])
    dato= int(conexion.dato.fetchone()[0])
    conexion.execute("update estudiantes quesemestre= %s where cod_estudio= %s",[dato,cod_estudio])
    conexion.close()