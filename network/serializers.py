from rest_framework import serializers
from .models import Network, Contact, Product, Supplier


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['contact_email', 'country', 'city', 'street', 'house_number']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'model', 'release_date']


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name']


class NetworkSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    product = ProductSerializer(many=True, read_only=True)
    supplier = SupplierSerializer()

    class Meta:
        model = Network
        fields = ['name', 'contact', 'product', 'supplier', 'debt', 'created_at']
