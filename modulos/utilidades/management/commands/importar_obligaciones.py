from django.core.management.base import BaseCommand, CommandError
from modulos.utilidades.models import RELAOBLIGENTRE, ROBLIGACIONESENTREGABLES, ROBLIGACIONESDOCUMENTOS, RELADOCOBLIG, \
    RELACIONDOCUENTRE, RENTREGABLESDOCUMENTOS, VDEPARTAMENTOSRUTAS, DEPARTAMENTOSRUTAS, VGRUPODEPARTAMENTO, \
    GRUPODEPARTAMENTO


class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        import time
        from modulos.acciones.models import  Obligacion,Entregable,Documento
        from modulos.utilidades.models import VCARGUEDOCUMENTOS,VCARGUEOBLIGACION,VENTREGABLES
        ini=time.time()
        i=0
        for vdocumento in  VCARGUEDOCUMENTOS.objects.all():
            i=i+1
            doc=Documento()
            doc.activo=vdocumento.activo
            doc.noaplica=not vdocumento.activo
            doc.nombre=vdocumento.NOMBRE_DOCUMENTO
            doc.codigo=vdocumento.DOCUMENTO
            doc.grupo_id = vdocumento.GRUPO
            doc.departamento_id = vdocumento.DEPARTAMENTO
            doc.ruta_id = vdocumento.RUTA
            doc.nota_id=22
            try:
                doc.save()
            except:
                print "se van omitir el doc",doc,vdocumento.id

        print "PROCESE DOCUMENTOS",'cantidad :'+str(i)
        fin= time.time()
        print "Tiempo Empleado ",fin-ini

        i=0
        for vobligacion in VCARGUEOBLIGACION.objects.all():
            oblg = Obligacion()

            oblg.nombre = vobligacion.NOMBRE_OBLIGACION
            oblg.codigo = vobligacion.OBLIGACION

            oblg.grupo_id = vobligacion.GRUPO
            oblg.departamento_id = vobligacion.DEPARTAMENTO
            oblg.ruta_id = vobligacion.RUTA
            oblg.activo=vobligacion.activo
            try:
                oblg.save()
            except:
                print "se va omitir la obl",oblg,vobligacion.id


        print "PROCESE DOBLIGACIONES",'cantidad :'+str(i)
        fin= time.time()
        print "Tiempo Empleado ",fin-ini

        i=0
        for ventregable in VENTREGABLES.objects.all():
            entl = Entregable()


            entl.nombre = ventregable.ENTREGABLE
            entl.codigo = ventregable.CODIGO

            entl.grupo_id = ventregable.GRUPO
            entl.departamento_id = ventregable.DEPARTAMENTO
            entl.ruta_id = ventregable.RUTA
            entl.activo=ventregable.activo
            try:
                entl.save()
            except:
                print "se va omitir la ent",entl,ventregable.id
        print "PROCESE ENTREGABLES",'cantidad :'+str(i)
        fin= time.time()
        print "Tiempo Empleado ",fin-ini


        i=0
        for renobl in RELAOBLIGENTRE.objects.all():
            obj = ROBLIGACIONESENTREGABLES()
            obj.entregable=renobl.entregable
            obj.obligacion=renobl.obligacion
            obj.save()
        print "PROCESE RELACIONES DE OBLIGACION ENTREGABLES",'cantidad :'+str(i)

        i=0
        for renobldoc in RELADOCOBLIG.objects.all():
            obj = ROBLIGACIONESDOCUMENTOS()
            obj.documento = renobldoc.documento
            obj.obligacion = renobldoc.obligacion
            obj.save()

        print "PROCESE RELACIONES DE OBLIGACION DOCUMENTO",'cantidad :'+str(i)
        fin= time.time()
        print "Tiempo Empleado ",fin-ini

        i=0
        for renobldoc in RELACIONDOCUENTRE.objects.all():
            obj = RENTREGABLESDOCUMENTOS()
            obj.documento = renobldoc.documento
            obj.entregable = renobldoc.entregable
            obj.save()
        print "PROCESE RELACIONES DE ENTREGABLE DOCUMENTO",'cantidad :'+str(i)
        fin= time.time()
        print "Tiempo Empleado ",fin-ini
        #falta agregar grupos y departamentos

        i=0
        for renobldoc in VDEPARTAMENTOSRUTAS.objects.all():
            obj = DEPARTAMENTOSRUTAS()
            obj.departamento = renobldoc.departamento
            obj.ruta = renobldoc.ruta

            obj.save()

        print "PROCESE RELACIONES DE RUTAS Y DEPARTAMENTOS",'cantidad :'+str(i)
        fin= time.time()
        print "Tiempo Empleado ",fin-ini

        i=0
        for renobldoc in VGRUPODEPARTAMENTO.objects.all():
            obj = GRUPODEPARTAMENTO()
            obj.departamento = renobldoc.departamento
            obj.grupo= renobldoc.grupo

            obj.save()
        print "PROCESE RELACIONES DE GRUPOS  Y DEPARTAMENTOS",'cantidad :'+str(i)
        fin= time.time()
        print "Tiempo Empleado ",fin-ini
        #falta agregar grupos y departamentos