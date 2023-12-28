from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated


from network.models import Network, Contact, Product, Supplier
from network.permissions import UpdateDebtPermission
from network.serializers import NetworkSerializer, ViewNetworkSerializer, ContactSerializer, ProductSerializer, \
    SupplierSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    CRUD для модели Контактов
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    CRUD для модели Продуктов
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    """
    CRUD для модели Поставшика
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class NetworkViewSet(viewsets.ModelViewSet):
    """
    CRUD для модели Сети
    """
    queryset = Network.objects.all()
    permission_classes = [IsAuthenticated, UpdateDebtPermission]
    filter_backends = [SearchFilter]
    search_fields = ['contact__country']

    def get_serializer_class(self):
        """
        В методе в зависимости от запроса идет выбор сериализатора
        """
        if self.action in ['list', 'retrieve']:
            return ViewNetworkSerializer
        return NetworkSerializer
