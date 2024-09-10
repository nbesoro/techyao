from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from store.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    price_ttc = serializers.DecimalField(
        max_digits=20, decimal_places=2, read_only=True
    )
    vat = serializers.IntegerField(read_only=True)
    price_ht = serializers.FloatField(required=True)
    class Meta:
        model = OrderItem
        fields = ["product", "quantity", "price_ht", "vat", "price_ttc"]

    def validate_price_ht(self, value):
        if value <= 0:
            raise serializers.ValidationError("Invalid price ht.")
        

class OrderSerializer(WritableNestedModelSerializer):
    items = OrderItemSerializer(many=True, source="orderitem_set")
    number = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        fields = ["number", "customer", "items"]
