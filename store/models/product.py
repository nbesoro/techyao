from django.db import models
from core.utils import constants


class Category(models.Model):
    """Model definition for Category."""

    name = models.CharField(max_length=constants.SHORT_CHARFIELD, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Category."""

        verbose_name = "Category"
        verbose_name_plural = "Categoryies"

    def __str__(self):
        """Unicode representation of Category."""
        return self.name


class Product(models.Model):
    """Model definition for Product."""

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=constants.NORMAL_CHARFIELD)
    brand = models.CharField(max_length=constants.SHORT_CHARFIELD)
    ref = models.CharField(max_length=constants.SHORT_CHARFIELD)
    price = models.FloatField()
    vat = models.FloatField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Product."""

        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        """Unicode representation of Product."""
        return self.name
