from rest_framework import serializers
from .models import Roles, Planes, Usuario, PlanesUsuario, Notificacion, Sorteo, HistorialSorteo, Participante, SorteoParticipante, Ganadores, Publicacion

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'

class PlanesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planes
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class PlanesUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanesUsuario
        fields = '__all__'

class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = '__all__'

class SorteoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sorteo
        fields = '__all__'

class HistorialSorteoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialSorteo
        fields = '__all__'

class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = '__all__'

class SorteoParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SorteoParticipante
        fields = '__all__'

class GanadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ganadores
        fields = '__all__'

class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = '__all__'