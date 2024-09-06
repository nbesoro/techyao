from django.urls import path

from store.views import generate_invoice_pdf

urlpatterns = [path("", generate_invoice_pdf)]
