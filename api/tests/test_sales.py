from unittest import TestCase
from flask import json
from api.app import app
from api.app.views import sales

class TestSalesCase(TestCase):

    def setUp(self):
        self.tester = app.test_client()

    def test_make_asale(self):
        response = self.tester.post('/api/v1/sales', 
            content_type="application/json", 
            data=json.dumps(
                dict(
                    product = 1,
                    quantity = 3
                )
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_get_all_sales_records(self):
        response = self.tester.get('/api/v1/sales')
        self.assertEqual(response.status_code, 200)
    
    def test_get_one_sales_record(self):
        response = self.tester.get('/api/v1/sales/1')
        self.assertEqual(response.status_code, 200)
    