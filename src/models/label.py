from src.extensions import db

class Label(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    __table_args__ = (db.UniqueConstraint('name', 'user_id', name='name_user_id'), )