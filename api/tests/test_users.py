from unittest import TestCase
from flask import json
from api.app import app
from api.app.views import users

class TestUsersCase(TestCase):

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

    def test_register_user(self):
        response = self.tester.post('/api/v1/auth/signup', 
            content_type="application/json", 
            headers=dict(Authorization='Bearer '+ self.token), 
            data=json.dumps(
                dict(
                    full_name = "Testing User",
                    email = "admin@test.com",
                    password = "testing"
                )
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_get_all_registered_users(self):
        response = self.tester.get('/api/v1/users', 
            headers=dict(Authorization='Bearer '+ self.token)
        )
        self.assertEqual(response.status_code, 200)
    
    def test_get_aspecific_user_details(self):
        response = self.tester.get('/api/v1/users/1', 
            headers=dict(Authorization='Bearer '+ self.token)
        )
        self.assertEqual(response.status_code, 200)
    
    def test_edit_aspecific_user_details(self):
        response = self.tester.put('/api/v1/users/1', 
            content_type="application/json", 
            headers=dict(Authorization='Bearer '+ self.token), 
            data=json.dumps(
                dict(
                    full_name = "Testing User",
                    email = "admin@test.com",
                    password = "testing",
                    admin = "True"
                )
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_admin_delete_aspecific_user(self):
        response = self.tester.delete('/api/v1/users/2', 
            headers=dict(Authorization='Bearer '+ self.token)
        )
        self.assertEqual(response.status_code, 200)
