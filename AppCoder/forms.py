from django import forms

class EntrenadorFormulario(forms.Form):

    nombre=forms.CharField(max_length=60)
    apellido=forms.CharField(max_length=60)
    especialidad=forms.CharField(max_length=60)

class MaquinasFormulario(forms.Form):

    nombre=forms.CharField(max_length=30)
    zonaDeTrabajo=forms.CharField(max_length=60)
    pesoMax=forms.IntegerField()

class GimnasiosFormulario(forms.Form):

    nombre=forms.CharField(max_length=60)
    fechaCreacion=forms.DateField()
    Localicacion=forms.CharField(max_length=30)