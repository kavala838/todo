from src.extensions import db 
from src.models.task import Task

class Workspace(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    tasks = db.relationship('Task', backref='workspace', cascade="all, delete-orphan")
    __table_args__ = (db.UniqueConstraint('name', 'user_id', name='name_user_id'),)