from django.urls import path

from AppEntrega1Daneri import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    path('profeFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    path('estudiantesFormulario', views.estudianteFormulario, name="EstudianteFormulario"),
    path('busquedaComision',  views.busquedaComision, name="BusquedaComision"),
    path('buscar', views.buscar),
    path('resultadoBusqueda',  views.resultadoBusqueda, name="ResultadoBusqueda"),
   
]