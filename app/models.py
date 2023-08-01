from django.db import models

# Create your models here.

class Tinto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
         return f"{self.nombre}, ({self.precio})"

class Blancos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()

    
    def __str__(self):
        return f"{self.nombre}, ({self.precio})"


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()

def __str__(self):
    return f"{self.apellido}, {self.nombre}, {self.email},  {self.telefono}"
