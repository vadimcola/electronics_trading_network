from rest_framework import routers

from network.apps import NetworkConfig
from network.views import NetworkViewSet, ContactViewSet, ProductViewSet, SupplierViewSet

app_name = NetworkConfig.name

urlpatterns = [

]

router = routers.SimpleRouter()
router.register('network', NetworkViewSet)
router.register('contact', ContactViewSet)
router.register('product', ProductViewSet)
router.register('supplier', SupplierViewSet)
urlpatterns += router.urls
