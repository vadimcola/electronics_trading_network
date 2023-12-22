from django.db import models


class Supplier(models.Model):

    CATEGORY = (
        (0, 'Factory'),
        (1, 'Retail Network'),
        (2, 'Individual Entrepreneur')
    )

    name = models.CharField(max_length=255, verbose_name='Наименование поставщика')
    category = models.IntegerField(choices=CATEGORY, verbose_name='Категория поставщика')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


