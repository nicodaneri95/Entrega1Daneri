from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppEntrega1Daneri.models import Curso, Profesor,Estudiante
from AppEntrega1Daneri.forms import CursoFormulario, ProfesorFormulario,EstudiantesFormulario

# Create your views here.

def curso(request):

      curso =  Curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"


      return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppEntrega1Daneri/inicio.html")



def estudiantes(request):

      return render(request, "AppEntrega1Daneri/estudiantes.html")


def entregables(request):

      return render(request, "AppEntrega1Daneri/entregables.html")


def cursos(request):

      if request.method == 'POST':

            miFormulario = CursoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  curso = Curso (nombre=informacion['curso'], comision=informacion['comision']) 

                  curso.save()

                  return render(request, "AppEntrega1Daneri/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= CursoFormulario() #Formulario vacio para construir el html

      return render(request, "AppEntrega1Daneri/cursos.html", {"miFormulario":miFormulario})




def profesores(request):

      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], profesion=informacion['profesion']) 

                  profesor.save()

                  return render(request, "AppEntrega1Daneri/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ProfesorFormulario() #Formulario vacio para construir el html

      return render(request, "AppEntrega1Daneri/profesores.html", {"miFormulario":miFormulario})






def buscar(request):
      """ if "comision" in request.GET:
            return HttpResponse(f"Estoy buscando la comision {request.GET['comision']}") """
      comisiona = request.GET['comision'] 
      if  comisiona!="":

	      
            comisiona = request.GET['comision'] 
            cursos = Curso.objects.filter(comision=comisiona)

            return render(request, "AppEntrega1Daneri/resultadoBusqueda.html", {"cursos":cursos})

      else: 

	      return render(request, "AppEntrega1Daneri/busquedaComision.html",{"mensaje":"Ingresa una comision correcta"}) 
             
def busquedaComision(request):
      return render(request,"AppEntrega1Daneri/busquedaComision.html")

def resultadoBusqueda(request):
      return render(request, "AppEntrega1Daneri/resultadoBusqueda.html")

def cursoFormulario(request):
      if request.method == 'POST':
            miFormulario=CursoFormulario(request.POST)
            print(miFormulario)
            if (miFormulario.is_valid): 

                  informacion = miFormulario.cleaned_data

                  curso = Curso (nombre=informacion['curso'], comision=informacion['comision']) 
                  
                  curso.save()

                  return render(request, "AppEntrega1Daneri/inicio.html", {"mensaje":"Se guardo el curso correctamente"})
            else:
                  return render(request, "AppEntrega1Daneri/cursoFormulario.html",{"form": miFormulario,"mensaje":"Informacion no valida"}) 

      else: 

            formulario= CursoFormulario()
            return render(request, "AppEntrega1Daneri/cursoFormulario.html",{"form": formulario})

def profesorFormulario(request):
      if request.method == 'POST':
            miFormulario=ProfesorFormulario(request.POST)
            print(miFormulario)
            if (miFormulario.is_valid): 

                  informacion = miFormulario.cleaned_data
                  nombre=informacion['nombre']
                  apellido=informacion['apellido']
                  email=informacion['email']
                  profesion=informacion['profesion']
                  profesor = Profesor (nombre=nombre,apellido=apellido,email=email,profesion=profesion) 
                  profesor.save()

                  return render(request, "AppEntrega1Daneri/inicio.html", {"mensaje":"Se guardo el profesor correctamente"})
            else:
                  return render(request, "AppEntrega1Daneri/profeFormulario.html",{"form": miFormulario,"mensaje":"Informacion no valida"}) 

      else: 

            formulario= ProfesorFormulario()
            return render(request, "AppEntrega1Daneri/profeFormulario.html",{"form": formulario})

def estudianteFormulario(request):
      if request.method == 'POST':
            miFormulario=EstudiantesFormulario(request.POST)
            print(miFormulario)
            if (miFormulario.is_valid): 

                  informacion = miFormulario.cleaned_data
                  nombre=informacion['nombre']
                  apellido=informacion['apellido']
                  email=informacion['email']
                  
                  estudiante = Estudiante (nombre=nombre,apellido=apellido,email=email) 
                  estudiante.save()

                  return render(request, "AppEntrega1Daneri/inicio.html", {"mensaje":"Se guardo el estudiante correctamente"})
            else:
                  return render(request, "AppEntrega1Daneri/estudiantesFormulario.html",{"form": miFormulario,"mensaje":"Informacion no valida"}) 

      else: 

            miFormulario= EstudiantesFormulario()
            return render(request, "AppEntrega1Daneri/estudiantesFormulario.html",{"form": miFormulario})