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


class ViewNetworkSerializer(serializers.ModelSerializer):
    """
    Сериализатор для просмотра сети
    """
    contact = ContactSerializer()
    product = ProductSerializer(many=True, read_only=True)
    supplier = SupplierSerializer()

    class Meta:
        model = Network
        fields = ['name', 'category', 'contact', 'product', 'supplier', 'debt', 'created_at']


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = '__all__'

    def validate(self, data):
        """
        В данном методе сравнивается категория поставщика с категорией сети
        """
        supplier_category = data['supplier'].category
        network_category = data['category']
        if not network_category-1 == supplier_category:
            raise serializers.ValidationError(
                'Категория поставщика должна быть предыдущей по иерархии '
            )
        return data
