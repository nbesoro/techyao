from django.db import transaction
from rest_framework import viewsets
from store.models import Order, OrderItem
from store.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        items_data = self.request.data.pop("items")
        order = serializer.save()
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
