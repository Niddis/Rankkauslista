from application import db
from application.models import Base
from sqlalchemy.sql import text

class Result(Base):

    joukkue_id = db.Column(db.Integer, db.ForeignKey('joukkue.id'))
    cup_id = db.Column(db.Integer, db.ForeignKey('cup.id'))
    rank = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, nullable=False)

    def __init__(self, cup_id):
        self.cup_id = cup_id
        self.rank = 0
        self.points = 0

    @staticmethod
    def list_results():
        stmt = text("SELECT Joukkue.name, Cup.name, Result.rank, Result.points, Result.id"
                    " FROM Joukkue, Result, Cup"
                    " WHERE Joukkue.id = Result.joukkue_id"
                    " AND Result.cup_id = Cup.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"joukkue":row[0], "cup":row[1], "rank":row[2], "points":row[3], "id":row[4]})

        return response
