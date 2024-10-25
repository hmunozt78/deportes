# Generated by Django 5.1.2 on 2024-10-25 01:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('liga', models.CharField(choices=[('Primera A', 'Primera Division'), ('Primera B', 'Segunda Division'), ('Sin Categoria', 'Sin Division')], default='Sin Categoria', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('dorsal', models.PositiveSmallIntegerField(max_length=3)),
                ('posicion', models.CharField(choices=[('Arquero', 'Arquero'), ('Defensa', 'Defensa'), ('Medio Campo', 'Medio Campo'), ('Lateral', 'Lateral'), ('Delantero', 'Delantero'), ('Sin Posicion', 'Sin Posicion')], default='Sin Posicion', max_length=100)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jugadores', to='club.club')),
            ],
        ),
    ]
