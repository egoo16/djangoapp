from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Articulo
from .forms import ArticuloForm


# Create your views here.
def articulo_lista(request):
    articulos = Articulo.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/articulo_lista.html', {'articulos':articulos})

def articulo_detalle(request, pk):
        post = get_object_or_404(Articulo, pk=pk)
        return render(request, 'blog/articulo_detalle.html', {'post': post})

def articulo_nuevo(request):
    if request.method == "POST":
        formulario = ArticuloForm(request.POST)
        if formulario.is_valid():
            articulo = formulario.save(commit=False)
            articulo.autor = request.user
            articulo.fecha_publicacion = timezone.now()
            post.save()
            return redirect('blog.views.articulo_detalle', pk=articulo.pk)
    else:
        formulario = ArticuloForm()
    return render(request, 'blog/articulo_editar.html', {'formulario': formulario})

def articulo_editar(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == "POST":
        formulario = ArticuloForm(request.POST, instance=articulo)
        if formulario.is_valid():
            articulo = formulario.save(commit=False)
            articulo.autor = request.user
            articulo.save()
            return redirect('blog.views.articulo_detalle', pk=articulo.pk)
    else:
        formulario = ArticuloForm(instance=articulo)
    return render(request, 'blog/articulo_editar.html', {'formulario': formulario})
