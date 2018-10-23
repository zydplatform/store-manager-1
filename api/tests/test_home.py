from unittest import TestCase
from api.app import app
from api.app.views import main

class AppTestCase(TestCase):

    def setUp(self):
        self.tester = app.test_client()

    def test_home(self):
        response = self.tester.get('/api/v1/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome To The Store Manager System API Version 1", response.data)