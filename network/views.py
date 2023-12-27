from rest_framework import viewsets

from network.models import Network, Contact, Product, Supplier
from network.serializers import NetworkSerializer, ViewNetworkSerializer, ContactSerializer, ProductSerializer, \
    SupplierSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ViewNetworkSerializer
        return NetworkSerializer
