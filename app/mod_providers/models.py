# Providers Module
from app import db

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.String(100), default=db.func.current_timestamp())
    date_modified = db.Column(db.String(100), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    active = db.Column(db.Boolean, default=True)

class Provider(Base):

    __tablename__ = 'Providers'

    name = db.Column(db.String(100), nullable=False)
    client_id = db.Column(db.String(100), nullable=False)
    assertion_endpoint = db.Column(db.String(255), nullable=False)