from rest_framework import viewsets

from network.models import Network
from network.serializers import NetworkSerializer, ViewNetworkSerializer


class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ViewNetworkSerializer
        return NetworkSerializer
