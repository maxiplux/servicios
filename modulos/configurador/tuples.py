# -*- coding: cp1252 -*-
__author__ = 'Juan'
AFIRMACIONES_BOOL = (
    (True, "SI"),
    (False, "NO"),
)

MULTIMODO_CHOICES = (
    (1, "Validado para obligaciones"),
    (2, "Valido para Planes de accion"),
    (3, "Valido para Planes de accion y obligaciones"),
)

AFIRMACIONES = (("SI", "SI"), ("NO", "NO"))
GENERO = (
    ('1', 'Mujer'),
    ('2', 'Hombre'),
)

TIPO_DOCUMENTO = (
    ('CC', 'Cedula'),
    ('TI', 'Tarjeta de identidad'),
    ('NIT', 'NIT O RUT'),
    ('RC', 'INDEFINIDO'),
)

TIPO_POBLACION = (
    (1, 'Individuo'),
    (2, 'Familia'),
    (3, 'Org de Base'),
)

DatoNoDisponible="Dato no disponible"


# -*- coding: cp1252 -*-
# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
import itertools as it
import glob
import os

from django.conf import  settings


def multiple_file_types(*patterns):
    return it.chain.from_iterable(glob.glob(pattern) for pattern in patterns)


def FONTS():
    valores=multiple_file_types(os.path.join(os.sep, settings.FONT_DIRECTORY, "*.TTF"),os.path.join(os.sep, settings.FONT_DIRECTORY, "*.otf"),os.path.join(os.sep, settings.FONT_DIRECTORY, "*.ttf"))
    if valores==[]:
        yield (None,None)
    for filename in valores:
        #settings.FONT_DIRECTORY
        yield (filename,filename.replace(".otf","").replace(".ttf","").replace(".TTF","").replace(settings.FONT_DIRECTORY,"").replace("/","").replace("\\",""))
