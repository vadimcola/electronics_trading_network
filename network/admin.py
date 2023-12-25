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
    list_display = ['name']
