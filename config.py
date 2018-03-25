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

SECRET_KEY = "\x8d\xfa9\x16\xff\xa92\x97\x11f\xd7\xc2w\xa4\x1e\x86\xa8\x16~\xffJ/s\x1d"