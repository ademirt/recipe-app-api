from time import sleep

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    # Django pausa execução até a base de dados estar disponível.

    def handle(self, *args, **opt):
        self.stdout.write('Aguardando a base de dados...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Base de dados indisponível. Aguarde 3 segundos...')
                sleep(3)

        self.stdout.write(self.style.SUCCESS('Base de dados OK!!!'))