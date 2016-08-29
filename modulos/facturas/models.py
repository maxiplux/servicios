from __future__ import unicode_literals
import pyclbr

from django.db import models

# Create your models here.
from modulos.maestras.models import Maestra, MaestraSimple
from sorl.thumbnail import ImageField
from modulos.perfiles.models import Perfil
from modulos.productos.models import Producto


class Factura(MaestraSimple):
    cliente=models.ForeignKey(Perfil)
    #articulos= models.ManyToManyField(Producto, through=u'DetalleFactura')
    total=models.FloatField(default=0)



    @property
    def articulos(self):
        detalle=DetalleFactura.objects.filter(factura=self)
        valor=map(lambda  x:x.articulo,detalle)
        if valor:
            return  valor
        return []

    class Meta(Maestra.Meta):
        verbose_name = u"Factura"
        verbose_name_plural = u"Facturas"




    def refrescar(self):
        if self.articulos:
            self.total=sum(lambda x: x.valor_producto, self.articulos)
            self.save()
            return self,1
        return self,0





class DetalleFactura(MaestraSimple):
    factura= models.ForeignKey(Factura,null=True)
    articulo = models.ForeignKey(Producto,null=True)
    cantidad= models.PositiveIntegerField()

def clases():
    for clase in pyclbr.readmodule(__name__).keys():
        if clase not in []:

            yield eval(clase)
