from application import db
from application.models import Base
from sqlalchemy.sql import text

class Joukkue(Base):

    name = db.Column(db.String(144), nullable=False)
    home = db.Column(db.String(144), nullable=False)

    results = db.relationship("Result", backref='joukkue', lazy=True)

    def __init__(self, name):
        self.name = name
        self.home = "Helsinki"

    @staticmethod
    def list_teams_with_points():
        stmt = text("SELECT Joukkue.name, Joukkue.home, SUM(Result.points) AS points"
                    " FROM Joukkue"
                    " LEFT JOIN Result ON Joukkue.id = Result.joukkue_id"
                    " GROUP BY Joukkue.name"
                    " ORDER BY points DESC")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "home":row[1], "points":row[2]})

        return response

