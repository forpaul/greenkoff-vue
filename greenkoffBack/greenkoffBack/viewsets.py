from django.conf.urls import url
from django.urls import include
from rest_framework import viewsets, routers

from greenkoffBack.models import Product, Service
from greenkoffBack.serializers import ProductSerializer, ServiceSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


router = routers.DefaultRouter()

router.register(r'api/products', ProductViewSet)
router.register(r'api/services', ServiceViewSet)
