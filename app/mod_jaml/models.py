# JAML Class
import base64
import json
import datetime

from app.mod_providers.models import Provider

class Jaml():
    @staticmethod
    def jaml_request(request_string):
        '''
        Handles the JAML request

        Parameters
        ----------
        request_string: string
            The JAML request encoded in b64

        Returns
        -------
        request: dict
            dictionary containing the jaml request params
        '''

        try:
            json_request = base64.b64decode(bytes(request_string, 'utf-8'))
        except TypeError as e:
            print(e)
            raise TypeError

        return json.loads(json_request)

    @staticmethod
    def validate_jaml_request(jaml_request):
        '''
        Validates the Jaml request is valid

        Parameters
        ----------
        jaml_request: dict
            Dictionary containing the Jaml request parameters
        
        Returns
        ------
        valid: boolean
            If the Jaml request is valid
        '''

        provider = Provider.query.filter_by(client_id=jaml_request['client_id']).first()

        if provider is None:
            return False

        if provider.assertion_endpoint != jaml_request['assertion_endpoint']:
            return False

        if not Jaml.time_in_range(datetime.datetime.strptime(jaml_request['request_instance'], '%Y-%m-%d %H:%M:%S.%f')):
            return False

        return True

    @staticmethod
    def time_in_range(time):
        '''
        Validates that the time is within a sanity range

        Paramters
        ---------
        time: time
            The time to validate

        Returns
        -------
        valid: boolean
            If the time is within a 1 min range
        '''

        if time <= datetime.datetime.utcnow() - datetime.timedelta(minutes=1):
            return False
        elif time >= datetime.datetime.utcnow() + datetime.timedelta(minutes=1):
            return False
        
        return True

    @staticmethod
    def jaml_response(username):
        '''
        Encodes the jaml response.

        Paramters
        ---------
        username: string
            the username or nameid of the user

        Returns
        -------
        encoded_data: string
            Base64 encoded Jaml reponse
        '''

        data = {
            'name_id': username,
            'response_instance': str(datetime.datetime.utcnow()),
        }

        encoded_data = base64.b64encode(bytes(json.dumps(data), 'utf-8')).decode('utf-8')

        return encoded_data

class User():
    @staticmethod
    def login(username, password):
        '''
        THIS IS A PLACEHOLDER METHOD.
        ADD CUSTOM AUTHENTICATOR METHOD.
        '''

        if username == 'test' and password == 'test':
            return True
        else:
            return False

        @staticmethod
        def validate_user(username):
            if username == 'test':
                return True

            return False
        

