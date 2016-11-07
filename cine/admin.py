from django.contrib import admin
from cine.models import Actor, ActorAdmin, Pelicula, PeliculaAdmin

#Registramos nuestras clases principales.
admin.site.register(Actor, ActorAdmin)
admin.site.register(Pelicula, PeliculaAdmin)
