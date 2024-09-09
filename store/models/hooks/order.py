from django.db.models.signals import pre_save
from django.utils import timezone
from store.models import Order, OrderItem


def generate_order_number():
    today = timezone.now().strftime("%Y%m%d")
    last_order = Order.objects.filter(number__startswith=today).order_by("-id").last()
    if last_order:
        last_number = int(last_order.number.split(".")[-1])
        return f"{today}.{last_number + 1}"
    else:
        return f"{today}.1"


def set_order_number(sender, instance, **kwargs):
    if not instance.number:
        instance.number = generate_order_number()


pre_save.connect(set_order_number, sender=Order)
