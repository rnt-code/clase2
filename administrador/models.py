from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    edad=models.IntegerField()
    fecha_registro=models.DateField(null=True)

    def __str__(self):
        return "{} {} y su edad es {}".format(self.nombre, self.apellido, self.edad)
