from unittest.mock import patch
from flask_testing import TestCase
from flask import url_for
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class testData(TestBase)

