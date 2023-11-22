from django.db import models

class Usuario(models.Model):
    nombre_usuario = models.TextField(max_length=50)
    
    password_usuario = models.TextField(max_length= 20)

from django.db import models

class Alumno(models.Model):
    rut = models.TextField(max_length=20)
    primer_nombre = models.TextField(max_length=50)
    segundo_nombre = models.TextField(max_length=50, blank=True, null=True)
    apellido_paterno = models.TextField(max_length=50)
    apellido_materno = models.TextField(max_length=50)
    edad = models.IntegerField()
    nacionalidad = models.TextField(max_length=50)
    curso = models.TextField(max_length=10)
    sala = models.TextField(max_length=10)

    def __str__(self):
        return str(self.rut) + " - " + str(self.primer_nombre)  + " - " + str(self.segundo_nombre)+ " - " + str(self.apellido_paterno)+ " - " + str(self.apellido_materno)+ " - " + str(self.edad)+ " - " + str(self.nacionalidad)+ " - " + str(self.curso)+ " - " + str(self.sala) 




class Apoderado(models.Model):
    rut = models.TextField(max_length=20)
    primer_nombre = models.TextField(max_length=50)
    segundo_nombre = models.TextField(max_length=50, blank=True, null=True)
    apellido_paterno = models.TextField(max_length=50)
    apellido_materno = models.TextField(max_length=50)
    edad = models.IntegerField()
    parentesco = models.TextField(max_length=50)
    nacionalidad = models.TextField(max_length=50)
    
    def __str__(self):
        return str(self.rut) + " - " + str(self.primer_nombre)  + " - " + str(self.segundo_nombre)+ " - " + str(self.apellido_paterno)+ " - " + str(self.apellido_materno)+ " - " + str(self.edad)+ " - " + str(self.parentesco)+ " - " + str(self.nacionalidad)

class Profesor(models.Model):
    nombre = models.TextField(max_length=50)
    apellido = models.TextField(max_length=50)
    correo = models.TextField(max_length=100)
    cargo = models.CharField(max_length=50)
    asignatura = models.TextField(max_length=50)
    
    def __str__(self):
        return str(self.nombre) + " - " + str(self.apellido)  + " - " + str(self.correo)+ " - " + str(self.cargo)+ " - " + str(self.asignatura)



class Historial(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion_historial = models.TextField(max_length=200)
    tabla_afectada_historial = models.TextField(max_length=100)
    fecha_hora_historial = models.DateTimeField()

    def __str__(self):
        return str(self.usuario) + " - " + str(self.descripcion_historial)  + " - " + str(self.tabla_afectada_historial)  + " - " + str(self.fecha_hora_historial)