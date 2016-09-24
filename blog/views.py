from django.shortcuts import render
from django.utils import timezone
from blog.models import Articulo

# Create your views here.
def articulo_lista(request):
    articulos = Articulo.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/articulo_lista.html', {'articulos':articulos})
