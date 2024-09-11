from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from account.serializers import CustomerSerializer
from store.models import Order, OrderItem


class OrderItemPdfSerializer(WritableNestedModelSerializer):
    price_ttc = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)
    vat = serializers.IntegerField(read_only=True)
    total_price_ttc = serializers.SerializerMethodField()
    product = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = [
            "product",
            "quantity",
            "price_ht",
            "vat",
            "price_ttc",
            "total_price_ttc",
        ]

    def get_total_price_ttc(self, obj):
        return obj.price_ttc * obj.quantity

    def get_product(self, obj):
        return obj.product.name


class OrderPdfSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    customer = CustomerSerializer()
    total_price_ht = serializers.SerializerMethodField()
    total_price_vat = serializers.SerializerMethodField()
    total_price_ttc = serializers.SerializerMethodField()
    items = OrderItemPdfSerializer(many=True, source="orderitem_set")

    class Meta:
        model = Order
        fields = ["id", "number", "customer", "items", "total_price_ht", "total_price_vat", "total_price_ttc", "created_at"]

    def get_total_price_ht(self, obj):
        total_ht = sum(item.price_ht * item.quantity for item in obj.orderitem_set.all())
        return total_ht

    def get_total_price_vat(self, obj):
        total_vat = sum((item.price_ht * item.vat / 100) * item.quantity for item in obj.orderitem_set.all())
        return total_vat

    def get_total_price_ttc(self, obj):
        total_ttc = sum(item.price_ttc * item.quantity for item in obj.orderitem_set.all())
        return total_ttc

    def get_created_at(self, obj):
        # Utiliser strftime pour formater la date en "March 31, 2018"
        return obj.created_at.strftime("%B %d, %Y")
