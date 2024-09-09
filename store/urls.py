from django.urls import path

from store.views import (
    generate_invoice_pdf,
    customer_list,
    add_customer,
    category_list,
    product_list,
    add_product,
    generate_invoice,
)



urlpatterns = [
    path("", customer_list, name="customer_list"),
    path("customer/new", add_customer, name="add_customer"),
    path("category", category_list, name="category_list"),
    path("product", product_list, name="product_list"),
    path("product/new", add_product, name="add_product"),
    path("invoice", generate_invoice, name="generate_invoice"),
    path("pdf", generate_invoice_pdf)
]
