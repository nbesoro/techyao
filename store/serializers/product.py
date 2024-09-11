from rest_framework import serializers

from store.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M", read_only=True)
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = "__all__"

    def get_product_count(self, obj):
        return obj.product_set.count()


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ["category", "name", "brand", "ref", "vat", "price", "description"]


class ProductListSerializer(ProductSerializer):
    category = serializers.SerializerMethodField()
    price_ttc = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M", read_only=True)

    class Meta:
        model = Product
        fields = "__all__"

    def get_category(self, obj):
        return obj.category.name

    def get_price_ttc(self, obj):
        return obj.price + (obj.price * obj.vat) / 100
