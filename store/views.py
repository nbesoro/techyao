from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML


def generate_invoice_pdf(request):

    template = get_template("print/invoice.html")
    html_content = template.render({})

    html = HTML(string=html_content, base_url=request.build_absolute_uri())
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = 'inline; filename="output.pdf"'

    return response
