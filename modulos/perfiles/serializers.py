from rest_framework import serializers
from .models import  Perfil
from rest_framework import permissions
class PerfilSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perfil
        fields = []

