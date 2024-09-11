from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse


@login_required
def category_list(request):
    context = {"page": "category", "url_list": reverse("category_list")}
    return render(request, "pages/store/category/list.html", context)


@login_required
def product_list(request):
    context = {"page": "product"}
    return render(request, "pages/store/product/list.html", context)


@login_required
def add_product(request):
    context = {"page": "product", "url_list": reverse("product_list")}
    return render(request, "pages/store/product/add.html", context)
