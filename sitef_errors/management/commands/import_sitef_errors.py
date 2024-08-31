import csv
from django.core.management.base import BaseCommand
from sitef_errors.models import SitefError

class Command(BaseCommand):
    help = 'Importa erros do Sitef a partir de um arquivo CSV'

    def handle(self, *args, **kwargs):
        with open('csvfile.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                SitefError.objects.get_or_create(
                    code=row['error_code'],
                    description=row['error_description']
                )
        self.stdout.write(self.style.SUCCESS('Erros do Sitef importados com sucesso!'))
