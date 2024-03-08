from src.extensions import db 
from src.models.label import Label

task_label=db.Table('task_label', db.Column('task_id', db.Integer, db.ForeignKey('task.id')), db.Column('label_id', db.Integer, db.ForeignKey('label.id')))

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    workspace_id=db.Column(db.Integer, db.ForeignKey('workspace.id'))
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    labels= db.relationship('Label', secondary=task_label, backref='tasks')
    created_datetime=db.Column(db.DateTime)
    deadline_datetime=db.Column(db.DateTime)
    is_done=db.Column(db.Boolean, default=False)