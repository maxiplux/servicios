from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Perfil
from .serializers import PerfilSerializer



class PerfilViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Perfil.objects.all().order_by('-creado')
    serializer_class = PerfilSerializer
