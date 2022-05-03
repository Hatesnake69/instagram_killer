from flask_login import UserMixin

from app import db, manager


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    
class Comment(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('users', lazy=True))
    # date_created = db.Column(DateTime(timezone=True), server_default=func.now())
    
    def __init__(self, text, user_id):
        self.body = text
        self.user_id = user_id

    def __repr__(self):
        return '<Comment %r>' % self.id

@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
