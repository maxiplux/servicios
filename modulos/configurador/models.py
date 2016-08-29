# -*- coding: cp1252 -*-
import pyclbr
from django.db import models
from modulos.maestras.models import Maestra

MESES_RECAUDO=[("","")]+map(lambda  x: (x,x),range(1,32,1))

class TipoUsuario(Maestra):
    class Meta(Maestra.Meta):
        verbose_name = u"Tipo de usuario"
        verbose_name_plural = u"Tipos de usuarios"



def clases():
    for clase in pyclbr.readmodule(__name__).keys():
        if clase not in []:

            yield eval(clase)
