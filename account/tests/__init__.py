from django.test import TestCase as DjangoTestCase
from rest_framework.test import APIClient
from account.models import User


class TestCase(DjangoTestCase):
    fixtures = [
        "users.json",
        "products.json",
        "orders.json",
    ]

    def setUp(self):
        self.client = APIClient()
        self.TEST_PASSWORD = "qwsderfgtyh12@#"
        self.user = User.objects.create_superuser(email="mail@00149.gmail.com", password=self.TEST_PASSWORD)
        self.assertIsNotNone(self.user)
        self.user.password = self.TEST_PASSWORD
        self.user.set_password(self.TEST_PASSWORD)
        self.user.save()
