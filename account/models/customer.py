from django.db import models
from core.utils import constants
from .user import User


class Customer(User):
    GENDER_CHOICES = (
        ("Mr", "Mr"),
        ("Mrs", "Mrs"),
    )
    phone = models.CharField(max_length=constants.VERY_SHORT_CHARFIELD)
    phone2 = models.CharField(max_length=constants.VERY_SHORT_CHARFIELD, null=True, blank=True)
    addresse = models.CharField(max_length=constants.NORMAL_CHARFIELD)
    postal_code = models.CharField(max_length=constants.VERY_SHORT_CHARFIELD)
    city = models.CharField(max_length=constants.SHORT_CHARFIELD)
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES, default="Mr")

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customer's"
