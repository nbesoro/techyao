from django.db import models
from django.core.validators import MinValueValidator

from account.models import Customer
from .product import Product


class Order(models.Model):
    """Model definition for Order."""

    number = models.PositiveIntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        """Meta definition for Order."""

        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        """Unicode representation of Invoice."""
        return str(self.number)


class OrderItem(models.Model):
    """Model definition for OrderItem."""

    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
        ],
    )
    price_ttc = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        """Meta definition for OrderItem."""

        verbose_name = "OrderItem"
        verbose_name_plural = "OrderItems"

    def __str__(self):
        """Unicode representation of OrderItem."""
        return self.product.name
