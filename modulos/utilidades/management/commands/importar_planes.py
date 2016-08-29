from django.core.management.base import BaseCommand
from modulos.utilidades.management.commands.cargar_planes import  cargar_planes

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'
    requires_model_validation=False
    def handle(self, *args, **options):
        print cargar_planes()

