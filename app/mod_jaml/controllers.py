# Import flask dependencies
from flask import Blueprint, request, jsonify, Response, redirect, render_template, make_response

# Import app for config
from app import app

# Import Models
from app.mod_jaml.models import Jaml
from app.mod_jaml.models import User
from app.mod_providers.models import Provider

# Import from py library
import base64
import json
import datetime

mod_jaml = Blueprint('jaml', __name__, url_prefix='/jaml')

@mod_jaml.route('/', methods=['GET'])
def jaml():
    jaml_req = request.args.get('JAMLRequest')

    try:
        jaml_dict = Jaml.jaml_request(jaml_req)

        if request.cookies.get('user'):
            return render_template('login.html', url=jaml_dict['assertion_endpoint'], JAMLReponse=Jaml.jaml_response(request.cookies.get('user')))
    except TypeError as e:
        print(e)
        return render_template('error.html')

    if Jaml.validate_jaml_request(jaml_dict):
        return render_template('index.html', client_id=jaml_dict['client_id'])
    else:
        return render_template('error.html')

@mod_jaml.route('/login', methods=['POST'])
def login():

    try:
        provider = Provider.query.filter_by(client_id=request.form['client_id']).first()

        if provider is None:
            raise Exception

        if User.login(request.form['username'], request.form['password']):
            resp = make_response(render_template('login.html', url=provider.assertion_endpoint, JAMLReponse=Jaml.jaml_response(request.form['username'])))
            resp.set_cookie('user', request.form['username'])
            return resp
        
        raise Exception
    except Exception as e:
        print(e)
        return render_template('error.html')

@mod_jaml.route('/initiated', methods=['GET'])
def initiated():
    req = {
        'client_id': 'localhost',
        'request_instance': str(datetime.datetime.utcnow()),
        'assertion_endpoint': app.config['APP_URL'] + '/jaml/consume',
    }

    return redirect(app.config['APP_URL'] + '/jaml/?JAMLRequest=' + base64.b64encode(bytes(json.dumps(req), 'utf-8')).decode('utf-8'), code=302)

@mod_jaml.route('/consume', methods=['POST'])
def consume():

    data = request.form['JAMLReponse']

    data = base64.b64decode(data).decode('utf-8')

    return "consume jaml"

