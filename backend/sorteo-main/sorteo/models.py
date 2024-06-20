from django.db import models

# Create your models here.

class Roles(models.Model):
    rol = models.CharField(max_length=255)

class Planes(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Publicacion(models.Model):
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField()

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    rol = models.ForeignKey(Roles, on_delete=models.CASCADE) #REVISAR 
    plan = models.ForeignKey(Planes, on_delete=models.CASCADE) #REVISAR 

class PlanesUsuario(models.Model):
    idPlan = models.ForeignKey(Planes, on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.IntegerField()

class Notificacion(models.Model):
    mensaje = models.TextField()
    fecha = models.DateTimeField()
    idSorteo = models.ForeignKey('Sorteo', on_delete=models.CASCADE)

class Sorteo(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    estado = models.BooleanField()
    idOrganizador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    idPublicacion = models.ForeignKey('Publicacion', on_delete=models.CASCADE)

class HistorialSorteo(models.Model):
    idSorteo = models.ForeignKey(Sorteo, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    detalles = models.TextField()

class Participante(models.Model):
    nombre = models.CharField(max_length=255)
    comentario = models.BooleanField()
    reaccion = models.BooleanField()

class SorteoParticipante(models.Model):
    idSorteo = models.ForeignKey(Sorteo, on_delete=models.CASCADE)
    idParticipante = models.ForeignKey(Participante, on_delete=models.CASCADE)

class Ganadores(models.Model):
    idHistorial = models.ForeignKey(HistorialSorteo, on_delete=models.CASCADE)
    idParticipante = models.ForeignKey(Participante, on_delete=models.CASCADE)

