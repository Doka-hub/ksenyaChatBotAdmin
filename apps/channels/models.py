from django.db import models


class Channel(models.Model):
    class Meta:
        db_table = 'channel'

    name = models.CharField(max_length=50, verbose_name='Имя канала')
    url = models.URLField(verbose_name='Ссылка на канал')
    eur_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма в Евро')
    rub_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма в Рублях')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
