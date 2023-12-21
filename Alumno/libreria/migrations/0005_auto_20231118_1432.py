# Generated by Django 3.2.8 on 2023-11-18 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0004_rename_estudiante_alumno'),
    ]

    operations = [
        migrations.CreateModel(
            name='curso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, null=True, verbose_name='nombre')),
                ('seccion', models.CharField(max_length=100, null=True, verbose_name='seccion')),
                ('sala', models.CharField(max_length=100, null=True, verbose_name='sala')),
                ('cantidadEvaluaciones', models.IntegerField(null=True, verbose_name='cantidadEvaluacion')),
                ('cantidadHoras', models.IntegerField(null=True, verbose_name='cantidadHoras')),
                ('horario', models.CharField(max_length=100, null=True, verbose_name='horario')),
            ],
        ),
        migrations.AddField(
            model_name='alumno',
            name='curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='libreria.curso'),
        ),
    ]
