from django.shortcuts import render


def category_list(request):
    context = {"page": "category"}
    return render(request, "pages/store/category/list.html", context)


def product_list(request):
    context = {"page": "product"}
    return render(request, "pages/store/product/list.html", context)


def add_product(request):
    context = {"page": "product"}
    return render(request, "pages/store/product/add.html", context)
