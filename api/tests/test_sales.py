from unittest import TestCase
from flask import json
from api.app import app
from api.app.views import sales

class SalesTestCase(TestCase):

    def setUp(self):
        self.tester = app.test_client()

    def test_make_asale(self):
        response = self.tester.post('/api/v1/sales/', 
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
        self.assertEqual(response.status_code, 200)

    def test_get_all_sales_records(self):
        response = self.tester.get('/api/v1/sales/')
        self.assertEqual(response.status_code, 200)
    
    def test_get_one_sales_record(self):
        response = self.tester.get('/api/v1/sales/1/')
        self.assertEqual(response.status_code, 200)
    
    def test_edit_aproduct_details(self):
        response = self.tester.put('/api/v1/sales/1', 
            content_type="application/json", 
            data=json.dumps(
                dict(
                    seller = "Babale Adam",
                    product = "Carot",
                    price = 300,
                    quantity = 5,
                    total_cost = 1500,
                    date_sold = "12/10/2018"
                )
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_admin_remove_asales_record(self):
        response = self.tester.delete('/api/v1/sales/2')
        self.assertEqual(response.status_code, 200)
    