# Import flask and template operators
from flask import Flask, render_template
from flask_cors import CORS

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Allow CORS on the API
CORS(app)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Import modules
from app.mod_jaml.controllers import mod_jaml as jaml_module
from app.mod_providers.controllers import mod_providers as providers_module

# Register blueprints with app
app.register_blueprint(jaml_module)
app.register_blueprint(providers_module)

# Migrate the DB
db.create_all()