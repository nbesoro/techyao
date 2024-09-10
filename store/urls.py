from django.urls import path

from store.views import (
    generate_invoice_pdf,
    customer_list,
    add_customer,
    category_list,
    product_list,
    add_product,
    invoice_list,
    generate_invoice,
)


urlpatterns = [
    path("", customer_list, name="customer_list"),
    path("customer/new", add_customer, name="add_customer"),
    path("category", category_list, name="category_list"),
    path("product", product_list, name="product_list"),
    path("product/new", add_product, name="add_product"),
    path("invoice", invoice_list, name="invoice_list"),
    path("invoice/generate", generate_invoice, name="generate_invoice"),
    path("pdf/<int:order_id>", generate_invoice_pdf, name="generate_invoice_pdf"),
]
