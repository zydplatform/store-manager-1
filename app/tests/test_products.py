
import sys, os
sys.path.append(os.path.abspath(''))

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
        test_client = app.test_client()
        response = test_client.get('/api/v1/')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"The requested URL was not found on the server", response.data)

    def test_add_product(self):
        response = self.test_client.post('api/v1/admin/products', content_type="application/json",  data=json.dumps(product))
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"The requested URL was not found on the server", response.data)
