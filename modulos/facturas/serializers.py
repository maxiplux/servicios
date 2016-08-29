from rest_framework import permissions
from rest_framework import serializers
from .models import  Factura,DetalleFactura

class FacturaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Factura
        fields = Factura.GetFieldsSerializer()+["cliente_id"]


class DetalleFacturaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DetalleFactura
        fields = DetalleFactura.GetFieldsSerializer()


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user