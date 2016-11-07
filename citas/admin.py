from django.contrib import admin
from citas.models import Paciente, PacienteAdmin, Doctor, DoctorAdmin, Cita, CitaInLine

#Registramos nuestras clases principales.
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Cita)
