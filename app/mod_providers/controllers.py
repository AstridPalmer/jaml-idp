# Import flask dependencies
from flask import Blueprint, request, jsonify, Response, redirect

# Import Models
from app.mod_providers.models import Provider

mod_providers = Blueprint('providers', __name__, url_prefix='/providers')

@mod_providers.route('/', methods=['GET'])
def providers():
    return "Testing"
