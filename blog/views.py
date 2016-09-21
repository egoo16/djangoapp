from django.shortcuts import render

# Create your views here.
def articulo_lista(request):
    return render(request, 'blog/articulo_lista.html', {})
