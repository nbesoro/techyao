from django.shortcuts import render


def customer_list(request):
    context = {"page": "customer"}
    return render(request, "pages/customer/list.html", context)

def add_customer(request):
    context = {"page": "customer"}
    return render(request, "pages/customer/add.html", context)
