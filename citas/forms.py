from django.contrib.admin import widgets
from django import forms
from .models import Paciente, Doctor, Cita

class CitaForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Cita
        fields = ('paciente', 'doctor','fecha','hora','obs')
#Redefinimos que control (widget) vamos a mostrar para ingresar los actores.
#Cuando el modelo es Many To Many, por defecto se usa un lisbotx multiseleccionable.
def __init__ (self, *args, **kwargs):
        super(CitaForm, self).__init__(*args, **kwargs)
        self.fields['fecha'].widget = forms.widgets.AdminSplitDateTime()
#        self.fields['obs'].widget.attrs['placeholder'] = self.fields['obs'].label or 'Ingrese las observaciones del paciente'
#En este caso vamos a usar el widget checkbox multiseleccionable.
        self.fields["doctor"].widget = forms.widgets.CheckboxSelectMultiple()
#Podemos usar un texto de ayuda en el widget
        self.fields["doctor"].help_text = "Escoja el doctor a citar"
#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario
        self.fields["doctor"].queryset = Doctor.objects.all()
#En este caso vamos a usar el widget checkbox multiseleccionable.
        self.fields["paciente"].widget = forms.widgets.CheckboxSelectMultiple()
#Podemos usar un texto de ayuda en el widget
        self.fields["paciente"].help_text = "Ingrese los Actores que participaron en la película"
#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario
        self.fields["paciente"].queryset = Paciente.objects.all()

#-----------------Paciente--------------------

class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ('nombre', 'telefono',)

#-----------------Doctor--------------------

class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = ('nombre', 'clinica','telefono',)
