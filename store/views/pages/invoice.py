from django.shortcuts import render


def generate_invoice(request):
    context = {"page": "gen_invoice"}
    return render(request, "pages/store/invoice.html", context)

