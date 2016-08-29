
from rest_framework import serializers
from .models import  Producto


from rest_framework import permissions

class ProductoSerializer(serializers.HyperlinkedModelSerializer):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        model = Producto
        fields = Producto.GetFieldsSerializer()