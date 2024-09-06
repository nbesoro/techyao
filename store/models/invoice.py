from django.db import models
from django.core.validators import MinValueValidator

from account.models import Customer
from .product import Product


class Invoice(models.Model):
    """Model definition for Invoice."""

    number = models.PositiveIntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    class Meta:
        """Meta definition for Invoice."""

        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"

    def __str__(self):
        """Unicode representation of Invoice."""
        return str(self.number)


class Order(models.Model):
    """Model definition for Order."""

    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
        ],
    )
    price_ttc = models.FloatField()
    
    class Meta:
        """Meta definition for Order."""

        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        """Unicode representation of Order."""
        return self.product.name
