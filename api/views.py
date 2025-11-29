from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from django.db.models import Q

from .models import Product
from .serializers import ProductSerializer, ProductFilterSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        if self.action == 'list':
            filter_data = ProductFilterSerializer(data=self.request.query_params)

            if filter_data.is_valid(raise_exception=True):

                min_price = filter_data.validated_data.get('min_price')
                max_price = filter_data.validated_data.get('max_price')
                stock = filter_data.validated_data.get('stock')
                created_at = filter_data.validated_data.get('created_at')
                search = filter_data.validated_data.get('search')
                if min_price is not None:
                    queryset = queryset.filter(price__gte=min_price)
                if max_price is not None:
                    queryset = queryset.filter(price__lte=max_price)
                if stock is not None:
                    queryset = queryset.filter(stock=stock)
                if created_at is not None:
                    queryset = queryset.filter(created_at__date=created_at)
                if search:
                    queryset = queryset.filter(
                        Q(name__icontains=search) |
                        Q(category__icontains=search)
                    )

        return queryset
