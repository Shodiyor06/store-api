from django.urls import path
from .views import ProductViewSet

urlpatterns = [
    path('products/', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product-list'),
    path('products/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'}), name='product-detail'),
]