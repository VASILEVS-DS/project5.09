from flask_login import UserMixin
from app import db, manager


class User(db.Model, UserMixin):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    fullname = db.Column(db.String(50), nullable=False)

    def __init__(self, email, password, fullname):
        self.email = email
        self.password = password
        self.fullname = fullname

    def __repr__(self):
        return f""

@manager.user_loder
def load_user(user_id):
    return User.query.get(user_id)