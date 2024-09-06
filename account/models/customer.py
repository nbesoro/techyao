from django.db import models
from core.utils import constants
from .user import User


class Customer(User):
    phone = models.CharField(max_length=constants.VERY_SHORT_CHARFIELD)
    addresse = models.CharField(max_length=constants.NORMAL_CHARFIELD)
    postal_code = models.CharField(max_length=constants.VERY_SHORT_CHARFIELD)
    city = models.CharField(max_length=constants.SHORT_CHARFIELD)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customer's"
