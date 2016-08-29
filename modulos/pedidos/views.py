from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Pedido
from .serializers import PedidoSerializer


class PedidoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Pedido.objects.all().order_by('-creado')
    serializer_class = PedidoSerializer
