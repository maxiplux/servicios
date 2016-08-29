# -*- coding: utf-8 -*-
__author__ = 'Juan'
def convertir_cadena(string) :

    try:
        return str(string)
    except:
        try:
            return unicode(string, "UTF-8")
        except:
            return  string
    return  string

def cargar_planes():

    import time
    from modulos.planes.models import  PlanAccion,Indicador,LineaAccion
    from modulos.utilidades.models import VCARGUELINEADEACCION,VCARGUEENTREGABLE,VCARGUEINDICADOR
    cadena=""
    ini=time.time()
    i=0
    for vlineasdeaccion in  VCARGUELINEADEACCION.objects.all():

        linea_de_accion=PlanAccion()
        linea_de_accion.activo=vlineasdeaccion.activo
        linea_de_accion.nombre=vlineasdeaccion.NOMBRE_LINEA_DE_ACCION

        linea_de_accion.departamento_id = int(vlineasdeaccion.DEPARTAMENTO)
        linea_de_accion.grupo_id = int(vlineasdeaccion.GRUPO)
        linea_de_accion.ruta_id = int(vlineasdeaccion.RUTA)
        try:
            linea_de_accion.save()
            i=i+1
        except Exception, e:
            cadena=cadena+"se van omitir el doc"+convertir_cadena('u'+linea_de_accion.nombre)+cadena+convertir_cadena(vlineasdeaccion.id) +"ERROR :"+convertir_cadena(e)

    cadena=cadena+"Se procesaron la cantidad de "+convertir_cadena(i) + " lineas de accion"+"\n"
    fin= time.time()
    cadena=cadena+"Tiempo Empleado "+ convertir_cadena(fin-ini)+"\n"

    i=0



    for ventregable in VCARGUEENTREGABLE.objects.all():
        indicador = LineaAccion()


        indicador.nombre = ventregable.ENTREGABLE
        indicador.plan_de_accion_id = ventregable.PLANACCION_ID

        indicador.grupo_id = int(ventregable.GRUPO)
        indicador.departamento_id = int(ventregable.DEPARTAMENTO)
        indicador.ruta_id = int(ventregable.RUTA)

        indicador.activo=ventregable.activo
        indicador.creado=ventregable.creado
        indicador.modificado=ventregable.modificado

        try:
            indicador.save()
            i=i+1
        except Exception, e:
            cadena=cadena+ "el entregable "+convertir_cadena('u'+indicador.nombre)+convertir_cadena(ventregable.id)+"ERROR :"+convertir_cadena(e)+"\n"


    cadena=cadena+ "Se procesaron la cantidad de "+convertir_cadena(i) + " entregables"+"\n"
    fin= time.time()
    cadena=cadena+"Tiempo Empleado "+convertir_cadena(fin-ini)+"\n"

    i=0







    for vindicador in VCARGUEINDICADOR.objects.all():
        indicador = Indicador()
        indicador.linea_de_accion_id = int(vindicador.ENTREGABLE_ID)
        indicador.indicador_de_medicion=vindicador.META_INDICADOR
        indicador.nombre = vindicador.INDICADOR


        try :
            indicador.save()
            i=i+1
        except Exception, e:
            cadena=cadena+ "el indicador "+convertir_cadena('u'+vindicador.nombre)+convertir_cadena(vindicador.id)+"ERROR :"+convertir_cadena(e)+"\n"


    cadena=cadena+"Se procesaron la cantidad de "+convertir_cadena(i) + " indicadores"+"\n"
    fin= time.time()
    cadena=cadena+"Tiempo Empleado "+convertir_cadena(fin-ini)+"\n"

    return  cadena

