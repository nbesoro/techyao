from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def invoice_list(request):
    context = {"page": "invoice"}
    return render(request, "pages/store/invoice/list.html", context)


@login_required
def generate_invoice(request):
    context = {"page": "invoice"}
    return render(request, "pages/store/invoice/generate.html", context)
