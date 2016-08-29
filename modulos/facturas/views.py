
from django.shortcuts import render


from rest_framework.decorators import detail_route, list_route, api_view, permission_classes
from rest_framework import renderers,generics
from rest_framework.response import Response
# Create your views here.
from rest_framework import viewsets,permissions
from .models import DetalleFactura,Factura
from rest_framework.permissions import IsAuthenticated
from .serializers import FacturaSerializer,DetalleFacturaSerializer



class DetalleFacturaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DetalleFactura.objects.all().order_by('-creado')
    serializer_class = DetalleFacturaSerializer




class FacturaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Factura.objects.all().order_by('-creado')
    serializer_class = FacturaSerializer
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def facturar(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})