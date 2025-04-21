from django.test import TestCase
from django.urls import reverse
from restaurant.models import MenuItem
from rest_framework.test import APIClient


#TestCase class
class MenuViewTest(TestCase):
    def setUp(self):
        # self.client = APIClient()
        # self.create_url = "/restaurant/menu/"
        MenuItem.objects.all().delete()
        MenuItem.objects.create(id=1, title="pizza", price=10, inventory=100)
        MenuItem.objects.create(id=2, title="pasta", price=20, inventory=100)

    def test_get_all(self):
        response = self.client.get(reverse('menu-list'))
        self.assertEqual(response.status_code, 200)
        expected_data = [
            { "id": 1, "title": "pizza", "price": "10.00", "inventory": 100},
            { "id": 2, "title": "pasta", "price": "20.00", "inventory": 100}
        ]
        self.assertEqual(response.json(), expected_data)