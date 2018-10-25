from unittest import TestCase
from flask import json
from api.app import app
from api.app.views import products

class ProductsTestCase(TestCase):

    def setUp(self):
        self.tester = app.test_client()

    def test_add_aproduct(self):
        response = self.tester.post('/api/v1/admin/products/', 
            content_type="application/json", 
            data=json.dumps(
                dict(
                    product_name = "Melon",
                    product_category = "Fruits",
                    product_price = 5000,
                    product_quantity = 26,
                    product_minimum_stock_allowed = 20
                )
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_get_all_products(self):
        response = self.tester.get('/api/v1/admin/products/')
        response = self.tester.get('/api/v1/attendant/products/')
        self.assertEqual(response.status_code, 200)
    
    def test_get_one_product(self):
        response = self.tester.get('/api/v1/admin/products/1/')
        response = self.tester.get('/api/v1/attendant/products/1/')
        self.assertEqual(response.status_code, 200)

    