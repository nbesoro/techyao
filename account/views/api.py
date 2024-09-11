from rest_framework import viewsets

# Create your views here.

from account.models import Customer
from account.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    search_fields = [
        "first_name",
        "last_name",
        "email",
        "phone",
        "phone2",
        "addresse",
        "postal_code",
        "city",
    ]
    ordering = [
        "first_name",
        "last_name",
    ]
    http_method_names = ["get", "post", "head"]
