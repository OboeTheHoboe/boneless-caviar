from flask_login import UserMixin
from . import db

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    telefono_1 = db.Column(db.String(50))
    telefono_2 = db.Column(db.String(50))
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))