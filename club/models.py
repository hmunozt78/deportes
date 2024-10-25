from django.db import models

# Create your models here


class Club(models.Model):

    LIGAS = [
        ('Primera A','Primera Division'),
        ('Primera B','Segunda Division'),
        ('Sin Categoria','Sin Division')
    ]

    nombre = models.CharField(max_length=100, blank=False, null=False)
    liga = models.CharField(max_length=100, blank=False, null=False, choices=LIGAS, default='Sin Categoria')
    

    def __str__(self):
        return self.nombre
    
class Jugador(models.Model):

    POSICIONES = [
        ('Arquero','Arquero'),
        ('Defensa','Defensa'),
        ('Medio Campo','Medio Campo'),
        ('Lateral','Lateral'),
        ('Delantero','Delantero'),
        ('Sin Posicion','Sin Posicion')
    ]

    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellido = models.CharField(max_length=100, blank=False, null=False)
    dorsal = models.PositiveSmallIntegerField(max_length=3)
    posicion = models.CharField(max_length=100, blank=False, null=False, choices=POSICIONES, default='Sin Posicion')
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='jugadores')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"



    

