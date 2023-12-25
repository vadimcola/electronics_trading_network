from rest_framework import routers

from network.apps import NetworkConfig
from network.views import NetworkViewSet

app_name = NetworkConfig.name

urlpatterns = [

]

router = routers.SimpleRouter()
router.register('network', NetworkViewSet)
urlpatterns += router.urls
