from application import db
from application.models import Base

class Cup(Base):

    name = db.Column(db.String(144), nullable=False)
    start_time = db.Column(db.String(144), nullable=False)
    end_time = db.Column(db.String(144), nullable=False)
    points = db.Column(db.Integer, nullable=False)

    results = db.relationship("Result", backref='cup', lazy=True)

    def __init__(self, name):
        self.name = name
        self.start_time = '2019-01-01 13:00:00'
        self.end_time = '2019-01-01 20:00:00'
        self.points = 100