from django import forms
from .models import Pelicula, Actor



class PeliculaForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Pelicula
        fields = ('nombre', 'anio', 'actores')

#Redefinimos que control (widget) vamos a mostrar para ingresar los actores.
#Cuando el modelo es Many To Many, por defecto se usa un lisbotx multiseleccionable.


def __init__ (self, *args, **kwargs):
        super(PeliculaForm, self).__init__(*args, **kwargs)

#En este caso vamos a usar el widget checkbox multiseleccionable.

        self.fields["actores"].widget = forms.CheckboxSelectMultiple()

#Podemos usar un texto de ayuda en el widget

        self.fields["actores"].help_text = "Ingrese los Actores que participaron en la película"

#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario

        self.fields["actores"].queryset = Actor.objects.all()
