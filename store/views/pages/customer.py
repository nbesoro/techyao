from django.shortcuts import render
from django.urls import reverse


def customer_list(request):
    context = {"page": "customer"}
    return render(request, "pages/customer/list.html", context)


def add_customer(request):
    context = {"page": "customer", "url_list": reverse("customer_list")}
    return render(request, "pages/customer/add.html", context)
