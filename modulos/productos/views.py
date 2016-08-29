from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from modulos.productos.models import Producto
from modulos.productos.serializers import ProductoSerializer


class ProductoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Producto.objects.all().order_by('-creado')
    serializer_class = ProductoSerializer
