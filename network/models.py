from django.db import models
from django.core.exceptions import ValidationError

NULLABLE = {'blank': True, 'null': True}


class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    contact_email = models.EmailField(verbose_name='e-mail')
    country = models.CharField(max_length=255, verbose_name='Страна')
    city = models.CharField(max_length=255, verbose_name='Город')
    street = models.CharField(max_length=255, verbose_name='Улица')
    house_number = models.IntegerField(verbose_name='Номер дома')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Supplier(models.Model):
    CATEGORY = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель')
    )

    name = models.CharField(max_length=255, verbose_name='Наименование поставщика')
    category = models.IntegerField(choices=CATEGORY, verbose_name='Категория поставщика')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE,
                                related_name='supplier_contact', verbose_name='Контакты')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование продукта')
    model = models.CharField(max_length=255, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода продукта на рынок')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Network(models.Model):
    CATEGORY = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель')
    )

    name = models.CharField(max_length=255, verbose_name='Наименование сети')
    category = models.IntegerField(choices=CATEGORY, verbose_name='Категория сети')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE,
                                related_name='network_contact', verbose_name='Контакты сети')
    product = models.ManyToManyField(Product,
                                     related_name='product', verbose_name='Продукты')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,
                                 related_name='supplier', verbose_name='Поставшик')
    debt = models.DecimalField(max_digits=10, decimal_places=2, **NULLABLE,
                               verbose_name='Задолженность перед поставщиком')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def clean(self):
        """
        В данном методе сравнивается категория поставщика с категорией сети
        """
        supplier_category = self.supplier.category
        network_category = self.category
        if not network_category - 1 == supplier_category:
            raise ValidationError(
                'Категория поставщика должна быть предыдущей по иерархии'
            )
        super().clean()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Сеть продаж'
        verbose_name_plural = 'Сети продаж'
