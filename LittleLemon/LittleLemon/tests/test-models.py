from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuTest(TestCase):

    def test_get_item(self):
        menu = Menu.objects.create(title = "IceCream", price = 40, inventory = 30)
        self.assertEqual(menu, "IceCream : 40")