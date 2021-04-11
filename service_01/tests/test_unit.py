  
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from requests_mock import mock

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    def test_name(self):
        with patch("requests.get") as r:
            r.return_value.text = "TestName"
            response = self.client.get(url_for('home'))
            self.assertIn(b'{"output":"TestName"}', response.data)

        with mock() as m:
            m.get("http://service_02:5001/name_gen", json={'output': 'TestName'})
            response = self.client.get(url_for("home"))
            self.assertIn(b"TestName", response.data)

    def test_colour(self):
        with patch("requests.get") as g:
            g.return_value.text = "TestColour"
            response = self.client.get(url_for("home"))
            self.assertIn(b"TestColour", response.data)

    def test_statement(self):
        with patch("requests.post") as p:
            p.return_value.text = "TestName likes TestColour"
            response = self.client.get(url_for("home"))
            self.assertIn(b"TestName likes TestColour", response.data)
    
    def test_previous_statements(self):
        with patch("requests.post") as p:
            p.return_value.text = "{1: ['TestName', 'TestColour', 'TestName likes TestColour']}"
            response = self.client.get(url_for("home"))
            self.assertIn(b"TestName likes TestColour", response.data)
