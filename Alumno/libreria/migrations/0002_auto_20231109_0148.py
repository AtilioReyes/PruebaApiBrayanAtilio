# Generated by Django 3.2.8 on 2023-11-09 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='celular',
            field=models.IntegerField(verbose_name='celular'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='edad',
            field=models.IntegerField(null=True, verbose_name='edad'),
        ),
    ]