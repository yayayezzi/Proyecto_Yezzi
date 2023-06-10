from django.shortcuts import render, redirect
from .models import Equipo, Jugador, Liga
from .forms import EquipoForm, JugadorForm, LigaForm

def listar_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipos/listar.html', {'equipos': equipos})

def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_equipos')
    else:
        form = EquipoForm()
    return render(request, 'equipos/crear.html', {'form': form})

def listar_jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'jugadores/listar.html', {'jugadores': jugadores})

def crear_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_jugadores')
    else:
        form = JugadorForm()
    return render(request, 'jugadores/crear.html', {'form': form})

def listar_ligas(request):
    ligas = Liga.objects.all()
    return render(request, 'ligas/listar.html', {'ligas': ligas})

def crear_liga(request):
    if request.method == 'POST':
        form = LigaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_ligas')
    else:
        form = LigaForm()
    return render(request, 'ligas/crear.html', {'form': form})
