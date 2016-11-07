from django.shortcuts import render
# Create your views here.
from django.contrib import messages
from .forms import PeliculaForm
from cine.models import Pelicula, Actuacion

#Vista para insertar una nueva película y los actores que actúan en ella.
def pelicula_nueva(request):
    if request.method == "POST":
#Creamos un objeto que va a contener todos los datos que el formulario PeliculaForm nos manda a través del método POST
        formulario = PeliculaForm(request.POST)
        if formulario.is_valid():
#Guardamos primero la Película, para que exista un ID para relacionar a los actores en la tabla Actuaciones
#Como el formulario incluye campos de varias tablas, aquí es necesario indicar los campos que corresponden a Película.
            pelicula = Pelicula.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])
#Por cada actor que esté seleccionado en el formulario, recorrerlo para guardarlo en la tabla Actuación
            for actor_id in request.POST.getlist('actores'):
#A la tabla Actuación le decimos cual es el ID del Actor y el ID de Película
               actuacion = Actuacion(actor_id=actor_id, pelicula_id = pelicula.id)
               actuacion.save()
               messages.add_message(request, messages.SUCCESS, 'Pelicula Guardada Exitosamente')
#Vamos guardando cada actuación que va recorriendo el cilco for
#Al terminar el ciclo for, mandamos un mensaje al template para que diga que los datos se guardaron exitosamente
    else:
        formulario = PeliculaForm()
    return render(request, 'cine/Pelicula_editar.html', {'formulario': formulario})
