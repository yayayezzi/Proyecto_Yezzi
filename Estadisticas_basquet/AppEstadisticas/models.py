from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    fundacion = models.DateField()
    ciudad = models.CharField(max_length=100)
    estadio = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    posicion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Liga(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    fundacion = models.DateField()

    def __str__(self):
        return self.nombre