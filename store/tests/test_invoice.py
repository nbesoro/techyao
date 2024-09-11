from django.urls import reverse
from account.tests import TestCase
from store.models import Order

from PyPDF2 import PdfReader
import tempfile


class CustomerTestCase(TestCase):
    def test_invoice_pdf_content(self):
        from_db = Order.objects.first()
        state = self.client.login(username=self.user.email, password=self.TEST_PASSWORD)
        self.assertTrue(state)

        response = self.client.get(reverse("generate_invoice_pdf", kwargs={"order_id": from_db.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/pdf")

        # Save PDF temporarily for analysis
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_pdf:
            temp_pdf.write(response.content)
            temp_pdf.seek(0)

            reader = PdfReader(temp_pdf.name)
            pdf_text = ""
            for page in reader.pages:
                pdf_text += page.extract_text()

            self.assertIn(from_db.number, pdf_text)
