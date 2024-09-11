from django.shortcuts import render


def invoice_list(request):
    context = {"page": "invoice"}
    return render(request, "pages/store/invoice/list.html", context)


def generate_invoice(request):
    context = {"page": "invoice"}
    return render(request, "pages/store/invoice/generate.html", context)
