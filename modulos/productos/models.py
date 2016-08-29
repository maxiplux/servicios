from __future__ import unicode_literals
import pyclbr

from django.db import models

# Create your models here.
from modulos.maestras.models import Maestra
from sorl.thumbnail import ImageField

class Producto(Maestra):
    descripcion = models.TextField(null=True,blank=True) # fecha de creacion
    imagen = ImageField(upload_to='fotos/productos')
    valor=models.FloatField(default=0.0)
    iva=models.FloatField(default=16.0/100.0)

    @property
    def valor_producto(self):
        return self.valor+self.valor*self.iva


    class Meta(Maestra.Meta):
        verbose_name = u"Producto"
        verbose_name_plural = u"Productos"



def clases():
    for clase in pyclbr.readmodule(__name__).keys():
        if clase not in []:

            yield eval(clase)

