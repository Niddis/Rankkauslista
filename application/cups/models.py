from application import db
from application.models import Base
from sqlalchemy.sql import text

class Cup(Base):

    name = db.Column(db.String(144), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    points = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    results = db.relationship("Result", backref='cup', lazy=True)

    def __init__(self, name):
        self.name = name
        self.start_time = '2019-01-01 13:00:00'
        self.end_time = '2019-01-01 20:00:00'
        self.points = 100

    @staticmethod
    def list_cups_with_teams():
        stmt = text("SELECT Cup.name, Cup.start_time, Cup.end_time, Cup.points, COUNT(Result.team_id)"
                    " FROM Cup"
                    " LEFT JOIN Result ON Cup.id = Result.cup_id"
                    " WHERE Cup.start_time >= CURRENT_TIMESTAMP"
                    " GROUP BY Cup.name, Cup.start_time, Cup.end_time, Cup.points"
                    " ORDER BY Cup.start_time")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "start":row[1], "end":row[2], "points":row[3], "teams":row[4]})

        return response