from unittest import TestCase
from flask import json
from api.app import app
from api.app.views import sales

class SalesTestCase(TestCase):

    def setUp(self):
        self.tester = app.test_client()

    def test_make_asale(self):
        response = self.tester.post('/api/v1/admin/sales/', 
            content_type="application/json", 
            data=json.dumps(
                dict(
                    seller = "Babale Adam",
                    product = "aple",
                    price = 1000,
                    quantity = 2,
                    total_cost = 2000,
                    date_sold = "12/10/2018"
                )
            )
        )
        response = self.tester.post('/api/v1/attendant/sales/', 
            content_type="application/json", 
            data=json.dumps(
                dict(
                    seller = "Kaleta Ivan",
                    product = "aple",
                    price = 1000,
                    quantity = 2,
                    total_cost = 2000,
                    date_sold = "12/10/2018"
                )
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_get_all_sales_records(self):
        response = self.tester.get('/api/v1/admin/sales/')
        response = self.tester.get('/api/v1/attendant/sales/')
        self.assertEqual(response.status_code, 200)
    
    