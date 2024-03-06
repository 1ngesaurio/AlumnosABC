from django.shortcuts import render, redirect
from django.db.models import Count, ExpressionWrapper, fields
from django.db.models.functions import Now
from datetime import datetime
from datetime import date
from collections import Counter
import json
from django.shortcuts import render

from .models import Alumno
from .forms import AlumnoForm

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'registroAlumnos/lista_alumnos.html', {'alumnos': alumnos})

def alta_alumno(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'registroAlumnos/alta_alumno.html', {'form': form})

def baja_alumno(request, pk):
    Alumno.objects.filter(pk=pk).delete()
    return redirect('lista_alumnos')

def cambio_alumno(request, pk):
    alumno = Alumno.objects.get(pk=pk)
    if request.method == "POST":
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'registroAlumnos/cambio_alumno.html', {'form': form, 'alumno': alumno})



def calcular_edad(fecha_nacimiento):
    """Calcula la edad basada en la fecha de nacimiento."""
    hoy = date.today()
    return hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

def dashboard_view(request):
    # Obtener todos los alumnos
    alumnos = Alumno.objects.all()

    # Calcula la edad de cada alumno
    edades = [calcular_edad(alumno.fechaNacimiento) for alumno in alumnos]

    # Contar cuántos alumnos hay de cada edad
    edad_counts = Counter(edades)
    
    # Ordenar las edades y obtener las cantidades para esas edades
    edades_ordenadas = sorted(edad_counts)
    cantidades = [edad_counts[edad] for edad in edades_ordenadas]

    # Convertir datos a JSON
    edades_json = json.dumps(edades_ordenadas)
    cantidades_json = json.dumps(cantidades)

    # Pasar datos JSON al contexto como string
    return render(request, 'registroAlumnos/dashboard.html', {
        'edades_json': edades_json, 
        'cantidades_json': cantidades_json
    })
