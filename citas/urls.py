from django.conf.urls import url
from . import views
#para llamar a nuestra página para insertar tenemos que invocar la dirección /pelicula/nueva

# se puede crear un hipervinculo para llamarla, en este ejemplo hay que invocar manualmente la dirección.

urlpatterns = [
    url(r'^$', views.cita_lista),
    url(r'^cita/(?P<pk>[0-9]+)/$', views.cita_detalle, name='cita_detalle'),
    url(r'^cita/nueva/$', views.cita_nueva, name='cita_nueva'),
    url(r'^cita/(?P<pk>[0-9]+)/editar/$', views.cita_editar, name='cita_editar'),
    url(r'^pacientes/', views.paciente_lista, name='paciente_lista'),
    url(r'^paciente/(?P<pk>[0-9]+)/$', views.paciente_detalle, name='paciente_detalle'),
    url(r'^paciente/nuevo/$', views.paciente_nuevo, name='paciente_nuevo'),
    url(r'^paciente/(?P<pk>[0-9]+)/editar/$', views.paciente_editar, name='paciente_editar'),
    url(r'^doctores/', views.doctor_lista, name='doctor_lista'),
    url(r'^doctor/(?P<pk>[0-9]+)/$', views.doctor_detalle, name='doctor_detalle'),
    url(r'^doctor/nuevo/$', views.doctor_nuevo, name='doctor_nuevo'),
    url(r'^doctor/(?P<pk>[0-9]+)/editar/$', views.doctor_editar, name='doctor_editar'),
    ]
