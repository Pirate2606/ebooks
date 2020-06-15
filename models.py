import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


###############################
###### SETUP APP ##############
###############################

app = Flask(__name__)
app.config['SECRET_KEY'] = "topsecret"


###############################
###### SETUP database #########
###############################

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


###############################
###### SETUP Models ###########
###############################

class Books(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key = True)
    semester = db.Column(db.Integer)
    subject = db.Column(db.String(128))
    name = db.Column(db.String(200), unique = True, index = True)
    author = db.Column(db.String(128))

    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __repr__(self, name, author):
        return f"{self.name} by {self.author}"

class Users(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(128))
    name = db.Column(db.String(200))
    message = db.Column(db.String(200))
    ip = db.Column(db.String(100))

    def __init__(self, email, name, message, ip):
        self.name = name
        self.email = email
        self.message = message
        self.ip = ip

    def __repr__(self, name, email):
        return f"{name} : {email}"


class Blacklist(db.Model):

    __tablename__ = "blacklist"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(128))
    ip = db.Column(db.String(100))


# class Request(db.Model):
#
#     __tablename__ = "requests"
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(128))
#     email = db.Column(db.String(200))
#     semester = db.Column(db.Integer)
#     branch = db.Column(db.String(100))
#     subject = db.Column(db.String(100))
#     book = db.Column(db.String(200))
