  
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from requests_mock import mock

from application import app, db
from application.routes import Animals

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///")
        return app
    
    def setUp(self):
        db.create_all()
        test_colour_statement_1 = Colour_Statement(name="Dan", colour="Green", statement="Dan likes Green!")
        db.session.add(test_colour_statement_1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponse(TestBase): 
    def test_generate_statement(self):
        with patch("requests.post") as r:
            r.return_value.text = {"name":"TestName", "colour":"TestColour"}
            response = self.client.get(url_for('generate_statement'))
            self.assertIn(b'{"output": "TestName likes TestColour!"}', response.data)

    def test_record_statement(self):
        with patch("requests.post") as r:
            r.return_value.text = '{"name":"TestName", "colour":"TestColour", "statement":"TestName likes TestColour!"}' 
            response = self.client.get(url_for('record_statement'))
            self.assertIn(b'{1: ["TestName", "TestColour", "TestName likes TestColour!"]}', response.data)
