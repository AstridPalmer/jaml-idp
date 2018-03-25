import unittest
import json
import datetime
import base64
import json

from app.mod_jaml.models import Jaml
from app.mod_jaml.controllers import mod_jaml

from flask import Flask

app = Flask(__name__)

app.register_blueprint(mod_jaml)

class Test_Jaml(unittest.TestCase):

    def setUp(self):
        '''
        Sets up testing
        '''
        self.app = app.test_client()

    def test_jaml_request(self):
        '''
        Tests the jaml request
        '''

        req = {
            'client_id': 'localhost',
            'request_instance': str(datetime.datetime.utcnow()),
            'assertion_endpoint': 'http://localhost:5000/jaml/consume',
        }

        encoded_request = base64.b64encode(bytes(json.dumps(req), 'utf-8')).decode('utf-8')

        self.assertEqual(Jaml.jaml_request(encoded_request), req)

        with self.assertRaises(TypeError):
            Jaml.jaml_request(req)

        req = 'testtesttest'

        with self.assertRaises(UnicodeDecodeError):
                Jaml.jaml_request(req)

    def test_validate_jaml_request(self):
        '''
        Tests the valid Jaml
        '''

        req = {
            'client_id': 'localhost',
            'request_instance': str(datetime.datetime.utcnow()),
            'assertion_endpoint': 'http://localhost:5000/jaml/consume',
        }

        self.assertTrue(Jaml.validate_jaml_request(req))

        req = {
            'client_id': 'localhost',
            'request_instance': str(datetime.datetime.utcnow() - datetime.timedelta(minutes=5)),
            'assertion_endpoint': 'http://localhost:5000/jaml/consume',
        }

        self.assertFalse(Jaml.validate_jaml_request(req))

    def test_time_in_range(self):
        '''
        Tests the date range function
        '''

        time = datetime.datetime.utcnow()

        self.assertTrue(Jaml.time_in_range(time))

        time = datetime.datetime.utcnow() - datetime.timedelta(minutes=3)

        self.assertFalse(Jaml.time_in_range(time))

    def test_jaml_response(self):
        '''
        Tests the Jaml response
        '''

        username = 'test'

        encoded_response = Jaml.jaml_response(username)

        self.assertTrue('name_id' in json.loads(base64.b64decode(encoded_response).decode('utf-8')))
        self.assertTrue('response_instance' in json.loads(base64.b64decode(encoded_response).decode('utf-8')))