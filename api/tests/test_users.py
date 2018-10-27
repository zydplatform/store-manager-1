from unittest import TestCase
from flask import json
from api.app import app
from api.app.views import users

class UsersTestCase(TestCase):

    def setUp(self):
        self.tester = app.test_client()

    def test_make_asale(self):
        response = self.tester.post('/api/v1/attendants/', 
            content_type="application/json", 
            data=json.dumps(
                dict(
                    id_number = "A/2018/005",
                    attendant_name = "Babale Adam",
                    attendant_username = "A/2018/005",
                    attendant_password = "A/2018/005"
                )
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_get_all_registered_attendants(self):
        response = self.tester.get('/api/v1/attendants/')
        self.assertEqual(response.status_code, 200)
    
    def test_get_aspecific_attendant_details(self):
        response = self.tester.get('/api/v1/attendants/1/')
        self.assertEqual(response.status_code, 200)
    
    def test_edit_aspecific_attendant_details(self):
        response = self.tester.put('/api/v1/attendants/1', 
            content_type="application/json", 
            data=json.dumps(
                dict(
                    id_number = "A/2018/024",
                    attendant_name = "Mutesi Surea",
                    attendant_username = "A/2018/024",
                    attendant_password = "A/2018/024"
                )
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_admin_delete_aspecific_attendant(self):
        response = self.tester.delete('/api/v1/attendants/2')
        self.assertEqual(response.status_code, 200)
    