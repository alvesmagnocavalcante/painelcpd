from django.db import models

class Balanca(models.Model):
    numero_balanca = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    setor = models.CharField(max_length=100)
    data_registro = models.DateTimeField(auto_now_add=True)

    def get_status(self):
        if self.peso < 19995:
            return 'fora_da_margem'
        elif self.peso == 19995:
            return 'aceitavel'
        else:
            return 'dentro_da_margem'

    def get_status_color(self):
        status = self.get_status()
        if status == 'fora_da_margem':
            return 'red'
        elif status == 'aceitavel':
            return 'yellow'
        else:
            return 'green'

    def __str__(self):
        return f"{self.numero_balanca} - {self.setor} - {self.peso}kg"
