from django.test import TestCase
from .models import Product
# Create your tests here.

class ProductModelTests(TestCase):

    def test_product_name(self):
        pizza = Product.create("Pizza")

        self.assertEqual(pizza.name, "Pizza")
        