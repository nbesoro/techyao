from django.utils import timezone

from store.models import Order


def generate_order_number():
    today = timezone.now().strftime("%Y%m%d")
    last_order = (
        Order.objects.filter(number__startswith=today).order_by("number").last()
    )
    if last_order:
        last_number = int(last_order.number.split(".")[-1])
        return f"{today}.{last_number + 1}"
    else:
        return f"{today}.1"
