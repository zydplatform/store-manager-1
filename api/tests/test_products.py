from unittest import TestCase
from flask import json
from api.app import app
from api.app.views import products

class ProductsTestCase(TestCase):

    def setUp(self):
        self.tester = app.test_client()

    def test_add_aproduct(self):
        response = self.tester.post('/api/v1/products', 
            content_type="application/json", 
            data=json.dumps(
                dict(
                    product_name = "grapes",
                    product_category = 1,
                    product_price = 1000,
                    product_quantity = 45,
                    product_minimum_stock_allowed = 10

                )
            )
        )
        self.assertEqual(response.status_code, 200)

