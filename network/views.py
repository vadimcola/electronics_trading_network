from rest_framework import viewsets

from network.models import Network, Contact
from network.serializers import NetworkSerializer, ContactSerializer


class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
