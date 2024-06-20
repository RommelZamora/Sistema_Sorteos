from django.shortcuts import render
from rest_framework import generics
from .models import Roles, Planes, Usuario, PlanesUsuario, Notificacion, Sorteo, HistorialSorteo, Participante, SorteoParticipante, Ganadores, Publicacion
from .serializers import RolesSerializer, PlanesSerializer, UsuarioSerializer, PlanesUsuarioSerializer, NotificacionSerializer, SorteoSerializer, HistorialSorteoSerializer, ParticipanteSerializer, SorteoParticipanteSerializer, GanadoresSerializer, PublicacionSerializer

class RolesListCreate(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

class RolesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

class PlanesListCreate(generics.ListCreateAPIView):
    queryset = Planes.objects.all()
    serializer_class = PlanesSerializer

class PlanesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Planes.objects.all()
    serializer_class = PlanesSerializer

class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PlanesUsuarioListCreate(generics.ListCreateAPIView):
    queryset = PlanesUsuario.objects.all()
    serializer_class = PlanesUsuarioSerializer

class PlanesUsuarioRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlanesUsuario.objects.all()
    serializer_class = PlanesUsuarioSerializer

class NotificacionListCreate(generics.ListCreateAPIView):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer

class NotificacionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer

class SorteoListCreate(generics.ListCreateAPIView):
    queryset = Sorteo.objects.all()
    serializer_class = SorteoSerializer

class SorteoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sorteo.objects.all()
    serializer_class = SorteoSerializer

class HistorialSorteoListCreate(generics.ListCreateAPIView):
    queryset = HistorialSorteo.objects.all()
    serializer_class = HistorialSorteoSerializer

class HistorialSorteoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistorialSorteo.objects.all()
    serializer_class = HistorialSorteoSerializer

class ParticipanteListCreate(generics.ListCreateAPIView):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer

class ParticipanteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer

class SorteoParticipanteListCreate(generics.ListCreateAPIView):
    queryset = SorteoParticipante.objects.all()
    serializer_class = SorteoParticipanteSerializer

class SorteoParticipanteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SorteoParticipante.objects.all()
    serializer_class = SorteoParticipanteSerializer

class GanadoresListCreate(generics.ListCreateAPIView):
    queryset = Ganadores.objects.all()
    serializer_class = GanadoresSerializer

class GanadoresRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ganadores.objects.all()
    serializer_class = GanadoresSerializer

class PublicacionListCreate(generics.ListCreateAPIView):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer

class PublicacionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer