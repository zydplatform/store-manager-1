from unittest import TestCase
from flask import json
from api.app import app
from api.app.views import users

class UsersTestCase(TestCase):

    def setUp(self):
        self.tester = app.test_client()

    def test_make_asale(self):
        response = self.tester.post('/api/v1/admin/attendants/', 
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

    