from application import db
from application.models import Base
from sqlalchemy.sql import text

class Team(Base):

    name = db.Column(db.String(144), nullable=False)
    home = db.Column(db.String(144), nullable=False)

    results = db.relationship("Result", backref='team', lazy=True)

    def __init__(self, name):
        self.name = name
        self.home = "Helsinki"

    @staticmethod
    def list_teams_with_points():
        stmt = text("SELECT Team.name, Team.home, SUM(Result.points) AS points, Team.id"
                    " FROM Team"
                    " LEFT JOIN Result ON Team.id = Result.team_id"
                    " GROUP BY Team.name, Team.home, Team.id"
                    " ORDER BY points DESC")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "home":row[1], "points":row[2], "id":row[3]})

        return response

