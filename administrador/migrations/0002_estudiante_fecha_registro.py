# Generated by Django 3.1.1 on 2020-09-18 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='fecha_registro',
            field=models.DateField(null=True),
        ),
    ]