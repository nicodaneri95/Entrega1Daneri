from django import forms


class CursoFormulario(forms.Form):

    #Especificar los campos
    curso = forms.CharField(label="Nombre Curso", max_length=50)
    comision = forms.IntegerField(label="Comision")


class ProfesorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

class EstudiantesFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()