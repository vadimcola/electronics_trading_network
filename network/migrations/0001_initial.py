# Generated by Django 4.2.8 on 2023-12-27 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('contact_email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('country', models.CharField(max_length=255, verbose_name='Страна')),
                ('city', models.CharField(max_length=255, verbose_name='Город')),
                ('street', models.CharField(max_length=255, verbose_name='Улица')),
                ('house_number', models.IntegerField(verbose_name='Номер дома')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование продукта')),
                ('model', models.CharField(max_length=255, verbose_name='Модель')),
                ('release_date', models.DateField(verbose_name='Дата выхода продукта на рынок')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование поставщика')),
                ('category', models.IntegerField(choices=[(0, 'Завод'), (1, 'Розничная сеть'), (2, 'Индивидуальный предприниматель')], verbose_name='Категория поставщика')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_contact', to='network.contact', verbose_name='Контакты')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование сети')),
                ('category', models.IntegerField(choices=[(0, 'Завод'), (1, 'Розничная сеть'), (2, 'Индивидуальный предприниматель')], verbose_name='Категория сети')),
                ('debt', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Задолженность перед поставщиком')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='network_contact', to='network.contact', verbose_name='Контакты сети')),
                ('product', models.ManyToManyField(related_name='product', to='network.product', verbose_name='Продукты')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier', to='network.supplier', verbose_name='Поставшик')),
            ],
            options={
                'verbose_name': 'Сеть продаж',
                'verbose_name_plural': 'Сети продаж',
            },
        ),
    ]
