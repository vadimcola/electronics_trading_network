from django.contrib import admin

from network.models import Supplier, Contact, Product, Network


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'supplier', 'debt')
    list_filter = ('contact__city',)
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        """
        Метод для отчистки задолженности перед поставщиком.
        """
        for obj in queryset:
            obj.debt = 0
            obj.save()

    clear_debt.short_description = 'Очистить задолженность перед поставщиком'
