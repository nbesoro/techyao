from django.urls import reverse
from rest_framework import status
from account.tests import TestCase
from account.models import Customer


class CustomerTestCase(TestCase):
    def test_create_cutomer_ok(self):
        payload = {
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "janesmith@example.com",
            "phone": "123456",
            "phone2": "654321",
            "addresse": "456 Test Ave",
            "postal_code": "75002",
            "city": "Paris",
            "gender": "Mr",
        }

        url = reverse("customer-list")
        # get all fixtures customer
        from_db = Customer.objects.all()

        # not loggin test
        self.assertEqual(from_db.count(), 5)  # fixtures count

        response = self.client.post(url, data=payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(from_db.count(), 5)  # Not chnage

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # loggin test
        state = self.client.login(username=self.user.email, password=self.TEST_PASSWORD)
        self.assertTrue(state)

        response = self.client.post(url, data=payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(from_db.count(), 6)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(from_db.count(), data["count"])

    def test_create_cutomer_nok(self):
        payload = {
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "janesmith@example.com",
            "phone": "123456",
            "phone2": "654321",
            "addresse": "456 Test Ave",
            "postal_code": "75002",
            "city": "Paris",
            "gender": "Ms",  # invalid choice
        }

        url = reverse("customer-list")
        # get all fixtures customer
        from_db = Customer.objects.all()
        self.assertEqual(from_db.count(), 5)
        # loggin test
        state = self.client.login(username=self.user.email, password=self.TEST_PASSWORD)
        self.assertTrue(state)

        response = self.client.post(url, data=payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("gender", response.json())
        self.assertNotIn("email", response.json())
        self.assertEqual(from_db.count(), 5)

        payload["email"] = "bonjour@nbesoro.com"  # existing email addresse
        response = self.client.post(url, data=payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.json())
        self.assertEqual(from_db.count(), 5)

    def test_allowed_method(self):
        state = self.client.login(username=self.user.email, password=self.TEST_PASSWORD)
        self.assertTrue(state)

        from_db = Customer.objects.all()
        self.assertEqual(from_db.count(), 5)

        url = reverse("customer-detail", kwargs={"pk": 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        from_db = Customer.objects.all()
        self.assertEqual(from_db.count(), 5)
