from src.extensions import db 
from flask_login import UserMixin
from src.models.workspace import Workspace
from src.models.label import Label
from src.models.task import Task

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    workspaces= db.relationship('Workspace', backref='user')
    labels= db.relationship('Label', backref='user')
    tasks = db.relationship('Task', backref='user')