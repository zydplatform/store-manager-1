from unittest import TestCase
from flask import json
from api.app import app
from api.app.views import sales

class TestSalesCase(TestCase):

    def setUp(self):
        self.tester = app.test_client()
        self.login_response = self.tester.post("api/v1/auth/login", 
            data = json.dumps({
                "email": "admin@api.com", 
                "password": "admin"
            }), 
            content_type="application/json"
        )
        self.token = json.loads(self.login_response.data) 

    def test_make_asale(self):
        response = self.tester.post('/api/v1/sales', 
            content_type="application/json", 
            headers=dict(Authorization='Bearer '+ self.token), 
            data=json.dumps(
                dict(
                    product = 1,
                    quantity = 3
                )
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_get_all_sales_records(self):
        response = self.tester.get('/api/v1/sales', 
            headers=dict(Authorization='Bearer '+ self.token), 
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
    
    def test_get_one_sales_record(self):
        response = self.tester.get('/api/v1/sales/1', 
            headers=dict(Authorization='Bearer '+ self.token), 
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
    