from application import db
from application.models import Base

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable= False)
    password = db.Column(db.String(144), nullable=False)
    isAdmin = db.Column(db.Boolean, nullable=False)

    cups = db.relationship("Cup", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.isAdmin = False

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True