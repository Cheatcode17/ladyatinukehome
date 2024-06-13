from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class User(db.Model):
    user_id=db.Column(db.Integer, autoincrement=True,primary_key=True)
    fullname=db.Column(db.String(20),nullable=True)
    phone =db.Column(db.String(200),nullable=True)
    message=db.Column(db.String(250),nullable=True)


class ContactUs(db.Model):
    user_id=db.Column(db.Integer, autoincrement=True,primary_key=True)
    fullname=db.Column(db.String(20),nullable=True)
    email=db.Column(db.String(200),nullable=True)
    message=db.Column(db.String(250),nullable=True)

class Admin(db.Model):
    admin_id=db.Column(db.Integer, autoincrement=True,primary_key=True)
    admin_username=db.Column(db.String(20),nullable=True)
    admin_pwd=db.Column(db.String(200),nullable=True)