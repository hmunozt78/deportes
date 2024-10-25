from django.contrib import admin
from .models import Club, Jugador

# Register your models here.

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    searchFields = ['nombre', 'liga']
    list_display = ['nombre', 'liga']
    ordering = ['nombre']
    
@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    searchFields = ['nombre','apellido','posicion']
    list_display = ['nombre','apellido','posicion','club']
    ordering = ['apellido']
