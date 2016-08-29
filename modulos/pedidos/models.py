from __future__ import unicode_literals
import pyclbr

from django.db import models

# Create your models here.
from modulos.facturas.models import Factura
from modulos.maestras.models import Maestra, MaestraSimple
from sorl.thumbnail import ImageField
from modulos.perfiles.models import Perfil
from modulos.productos.models import Producto


class Pedido(MaestraSimple):
    factura=models.ForeignKey(Factura)
    direccion= models.CharField(max_length=255)
    mensajero=models.ForeignKey(Perfil,related_name="mensajero")





    class Meta(Maestra.Meta):
        verbose_name = u"Pedido"
        verbose_name_plural = u"Pedidos"



def clases():
    for clase in pyclbr.readmodule(__name__).keys():
        if clase not in []:
            yield eval(clase)
