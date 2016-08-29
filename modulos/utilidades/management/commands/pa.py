from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        #manage.py pa  plandeapoyofamiliar proyectar
        #manage.py pa  home(usernamelinux) proyectoappdjango
        proyecto=args[1]
        home=args[0]
        from django.template.loader import render_to_string
        cadena = render_to_string('modulos/utilidades/commands/passenger_wsgi.txt', { 'proyecto': proyecto ,'home':home})
        f=open('passenger_wsgi.py','w')
        f.write(cadena.replace("\n\n","\n"))
        f.close()


