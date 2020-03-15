from rest_framework import serializers
from greenkoffBack.models import Product, Service


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.IntegerField()

    class Meta:
        model = Product
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.IntegerField()

    class Meta:
        model = Service
        fields = '__all__'