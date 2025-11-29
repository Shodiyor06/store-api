from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductFilterSerializer(serializers.Serializer):
    min_price = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)
    max_price = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)
    stock = serializers.IntegerField(required=False)
    created_at = serializers.DateField(required=False)
    search = serializers.CharField(required=False)
