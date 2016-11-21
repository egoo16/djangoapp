from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import RequestContext
from .forms import CitaForm, PacienteForm, DoctorForm
from citas.models import Doctor, Paciente, Cita
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


@login_required
def cita_lista(request):
    citas = Cita.objects.all
    return render(request, 'citas/cita_lista.html', {'citas':citas})

def cita_detalle(request, pk):
    citas = get_object_or_404(Cita, pk=pk)
    return render(request, 'citas/cita_detalle.html', {'citas': citas})

def cita_nueva(request):
    if request.method == "POST":
        formulario = CitaForm(request.POST)
        if formulario.is_valid():
            cita = formulario.save(commit=False)
            for doctor_id in request.POST.getlist('doctor'):
                for paciente_id in request.POST.getlist('paciente'):
                    cita = Cita(doctor_id=doctor_id, paciente_id = paciente_id,fecha = formulario.cleaned_data['fecha'], hora = formulario.cleaned_data['hora'], obs = formulario.cleaned_data['obs'])
                    cita.save()
                    messages.add_message(request, messages.SUCCESS, 'Cita Guardada Exitosamente')
    else:
        formulario = CitaForm()
    return render(request, 'citas/cita_nueva.html', {'formulario': formulario})

def cita_editar(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == "POST":
        formulario = CitaForm(request.POST, instance=cita)
        if formulario.is_valid():
            cita = formulario.save(commit=False)
            for doctor_id in request.POST.getlist('doctor'):
                for paciente_id in request.POST.getlist('paciente'):
                    cita = Cita(doctor_id=doctor_id, paciente_id = paciente_id,fecha = formulario.cleaned_data['fecha'], hora = formulario.cleaned_data['hora'], obs = formulario.cleaned_data['obs'])
                    cita.save()
                    messages.add_message(request, messages.SUCCESS, 'Cita Editada Exitosamente')
    else:
        formulario = CitaForm(instance=cita)
    return render(request, 'citas/cita_editar.html', {'formulario': formulario})


#-------------------------- Vista de Paciente -----------------------------------

def paciente_lista(request):
    pacientes = Paciente.objects.all
    return render(request, 'paciente/paciente_lista.html', {'pacientes':pacientes})

def paciente_detalle(request, pk):
    pacientes = get_object_or_404(Paciente, pk=pk)
    return render(request, 'paciente/paciente_detalle.html', {'pacientes': pacientes})

def paciente_nuevo(request):
    if request.method == "POST":
        formulario = PacienteForm(request.POST)
        if formulario.is_valid():
            paciente = formulario.save(commit=False)
            paciente = Paciente(nombre = formulario.cleaned_data['nombre'], telefono = formulario.cleaned_data['telefono'])
            paciente.save()
            messages.add_message(request, messages.SUCCESS, 'Paciente Ingresado Exitosamente')
    else:
        formulario = PacienteForm()
    return render(request, 'paciente/paciente_nueva.html', {'formulario': formulario})

def paciente_editar(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == "POST":
        formulario = PacienteForm(request.POST, instance=paciente)
        if formulario.is_valid():
            paciente = formulario.save(commit=False)
            paciente = Paciente(nombre = formulario.cleaned_data['nombre'], telefono = formulario.cleaned_data['telefono'])
            paciente.save()
            messages.add_message(request, messages.SUCCESS, 'Paciente Editado Exitosamente')
    else:
        formulario = PacienteForm(instance=paciente)
    return render(request, 'paciente/paciente_editar.html', {'formulario': formulario})

#-------------------------- Vista de Doctor-----------------------------------

def doctor_lista(request):
    doctores = Doctor.objects.all
    return render(request, 'doctor/doctor_lista.html', {'doctores':doctores})

def doctor_detalle(request, pk):
    doctores = get_object_or_404(Doctor, pk=pk)
    return render(request, 'doctor/doctor_detalle.html', {'doctores': doctores})

def doctor_nuevo(request):
    if request.method == "POST":
        formulario = DoctorForm(request.POST)
        if formulario.is_valid():
            doctor = formulario.save(commit=False)
            doctor = Doctor(nombre = formulario.cleaned_data['nombre'],clinica = formulario.cleaned_data['clinica'], telefono = formulario.cleaned_data['telefono'])
            doctor.save()
            messages.add_message(request, messages.SUCCESS, 'Doctor Ingresado Exitosamente')
    else:
        formulario = DoctorForm()
    return render(request, 'doctor/doctor_nueva.html', {'formulario': formulario})

def doctor_editar(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == "POST":
        formulario = DoctorForm(request.POST, instance=doctor)
        if formulario.is_valid():
            doctor = formulario.save(commit=False)
            doctor = Doctor(nombre = formulario.cleaned_data['nombre'],clinica = formulario.cleaned_data['clinica'], telefono = formulario.cleaned_data['telefono'])
            doctor.save()
            messages.add_message(request, messages.SUCCESS, 'Paciente Editado Exitosamente')
    else:
        formulario = DoctorForm(instance=doctor)
    return render(request, 'doctor/doctor_editar.html', {'formulario': formulario})
