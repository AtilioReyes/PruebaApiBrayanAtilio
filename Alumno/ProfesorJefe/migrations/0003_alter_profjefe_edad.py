# Generated by Django 4.2.6 on 2023-11-09 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProfesorJefe', '0002_alter_profjefe_edad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profjefe',
            name='edad',
            field=models.CharField(max_length=2),
        ),
    ]
