# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')

# App URL
APP_URL = 'http://localhost:5000'

# Secret Key
SECRET_KEY = 'CSxqRoVlIHcAVXUzMom4tGdAAfCqTk+A'