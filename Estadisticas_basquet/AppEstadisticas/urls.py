from django.urls import path
from . import views

urlpatterns = [
    path('equipos/', views.listar_equipos, name='listar_equipos'),
    path('equipos/crear/', views.crear_equipo, name='crear_equipo'),
    path('jugadores/', views.listar_jugadores, name='listar_jugadores'),
    path('jugadores/crear/', views.crear_jugador, name='crear_jugador'),
    path('ligas/', views.listar_ligas, name='listar_ligas'),
    path('ligas/crear/', views.crear_liga, name='crear_liga'),
]
