from django.db import models
from django.contrib import admin
from django.utils import timezone

# Create your models here.

class Paciente(models.Model):
    nombre  =   models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    def __str__(self):
        return self.nombre

class Doctor(models.Model):
    nombre = models.CharField(max_length=40)
    clinica = models.CharField(max_length=40)
    telefono = models.CharField(max_length=15)
    def __str__(self):
        return self.nombre

class Cita(models.Model):
    autor = models.ForeignKey('auth.User',blank=True, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=100,blank=False, null=True)
    hora = models.CharField(max_length=25,blank=False, null=True)
    obs = models.CharField(max_length=100,blank=True, null=True)

class CitaInLine(admin.TabularInline):
    model = Cita
    extra = 1

class PacienteAdmin(admin.ModelAdmin):
    inlines = (CitaInLine,)

class DoctorAdmin(admin.ModelAdmin):
    inlines = (CitaInLine,)
