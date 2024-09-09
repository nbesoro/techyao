from rest_framework import viewsets

from store.models import Category, Product
from store.serializers import (
    CategorySerializer,
    ProductSerializer,
    ProductListSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ["name"]
    ordering = ["name"]
    
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ["category__name", "name", "brand", "ref"]
    ordering = ["name"]
    def get_serializer_class(self):
        if self.action == "list":
            return ProductListSerializer
        return super().get_serializer_class()
