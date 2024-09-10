from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML

from store.models import Order
from store.serializers import OrderPdfSerializer


def generate_invoice_pdf(request, order_id):

    order = Order.objects.get(id=order_id)

    serializer = OrderPdfSerializer(instance=order)
    template = get_template("print/invoice.html")
    html_content = template.render(serializer.data)

    html = HTML(string=html_content, base_url=request.build_absolute_uri())
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = 'inline; filename="output.pdf"'

    return response
