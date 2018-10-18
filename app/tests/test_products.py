
import unittest
from flask import json
from app import app

product = {
            "product_id": 4,
            "product_name": "Apple",
            "product_category": "Fruits",
            "product_price": 1000,
            "product_quantity": 50,
            "product_minimum_stock_allowed": 20
        }

class TestProducts(unittest.TestCase):

    def setUp(self):
        self.test_client = app.test_client()

    def test_home(self):
        response = self.test_client.get('/api/v1/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome To The Store Manager System API Version 1", response.data)

    def test_add_product(self):
        response = self.test_client.post('api/v1/admin/products', content_type="application/json",  data=json.dumps(product))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"The product has been added", response.data)
