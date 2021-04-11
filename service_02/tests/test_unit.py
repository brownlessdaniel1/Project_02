from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from requests_mock import mock

from application import app

class TestBase(TestCase):
    def create_app(self):           # Called at runtime.
        return app

class TestResponse(TestBase):
    def test_get_name_gen(self):
        with patch("requests.get") as r:
            r.return_value.text = "TestName"
            response = self.client.get(url_for('name_gen'))
            self.assertIn(b'{"output":"TestName"}', response.data)
