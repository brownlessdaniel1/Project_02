from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_get_colour_gen(self):
        with patch("requests.get") as r:
            r.return_value.text = "TestColour"
            response = self.client.get(url_for('colour_gen'))
            self.assertIn(b'{"output":"TestColour"}', response.data)
