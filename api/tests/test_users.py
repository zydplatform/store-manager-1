from unittest import TestCase
from flask import json
from api.app import app
from api.app.views import users

class UsersTestCase(TestCase):

    def setUp(self):
        self.tester = app.test_client()

    def test_make_asale(self):
        response = self.tester.post('/api/v1/users/', 
            content_type="application/json", 
            data=json.dumps(
                dict(
                    id_number = "A/2018/005",
                    full_name = "Babale Adam",
                    username = "A/2018/005",
                    password = "A/2018/005"
                )
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_get_all_registered_users(self):
        response = self.tester.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)
    
    def test_get_aspecific_user_details(self):
        response = self.tester.get('/api/v1/users/1/')
        self.assertEqual(response.status_code, 200)
    
    def test_edit_aspecific_user_details(self):
        response = self.tester.put('/api/v1/users/1', 
            content_type="application/json", 
            data=json.dumps(
                dict(
                    id_number = "A/2018/024",
                    full_name = "Mutesi Surea",
                    username = "A/2018/024",
                    password = "A/2018/024"
                )
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_admin_delete_aspecific_user(self):
        response = self.tester.delete('/api/v1/users/2')
        self.assertEqual(response.status_code, 200)
    