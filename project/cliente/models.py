from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField(null=True, blank=True)
    pais_origen = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.nombre