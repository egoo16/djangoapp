from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Articulo

# Create your views here.
def articulo_lista(request):
    articulos = Articulo.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/articulo_lista.html', {'articulos':articulos})

def articulo_detalle(request, pk):
        post = get_object_or_404(Articulo, pk=pk)
        return render(request, 'blog/articulo_detalle.html', {'post': post})
        
