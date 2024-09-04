from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя канала')
    url = models.URLField(verbose_name='Ссылка на канал')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Количество')

    def __str__(self):
        return f'{self.name}'
