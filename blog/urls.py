from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.articulo_lista),
    url(r'^post/(?P<pk>[0-9]+)/$', views.articulo_detalle),
    url(r'^post/new/$', views.articulo_nuevo, name='articulo_nuevo'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.articulo_editar, name='articulo_editar'),

]
