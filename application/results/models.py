from application import db
from application.models import Base
from sqlalchemy.sql import text

class Result(Base):

    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    cup_id = db.Column(db.Integer, db.ForeignKey('cup.id'))
    rank = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, nullable=False)

    def __init__(self, cup_id):
        self.cup_id = cup_id
        self.rank = 0
        self.points = 0

    @staticmethod
    def list_results(sorter):
        orderByColumn = "cname, rank ASC"

        # sqlalchemy ei hyväksy paramsia ORDER BY:lle
        if sorter == "points":
            orderByColumn = "points DESC, rank ASC"
        elif sorter == "tname":
            orderByColumn = "tname, rank ASC"
        elif sorter == "rank":
            orderByColumn = "rank ASC, points DESC"
        

        stmt = text("SELECT Team.name AS tname, Cup.name AS cname, Result.rank AS rank, Result.points AS points"
                    " FROM Team, Result, Cup"
                    " WHERE Result.rank != 0"
                    " AND Team.id = Result.team_id"
                    " AND Result.cup_id = Cup.id"
                    " ORDER BY " + orderByColumn)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"team":row[0], "cup":row[1], "rank":row[2], "points":row[3]})

        return response

    @staticmethod
    def list_teams_that_are_not_in_results_of_particular_cup(id):
        stmt = text("SELECT Team.id, Team.name FROM Team WHERE id NOT IN "
                    "(SELECT Team.id FROM Team, Result "
                    "WHERE Result.cup_id = :id AND Team.id = Result.team_id)").params(id=id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response
    
    @staticmethod
    def find_results_by_cup(id):
        stmt = text("SELECT Team.name, Result.rank, Result.points, Result.id, Cup.account_id"
                    " FROM Team, Result, Cup"
                    " WHERE Cup.id = :id"
                    " AND Team.id = Result.team_id"
                    " AND Result.cup_id = Cup.id"
                    " ORDER BY Result.rank").params(id=id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"team":row[0], "rank":row[1], "points":row[2], "rid":row[3], "aid":row[4]})

        return response

    @staticmethod
    def find_results_by_team(id):
        stmt = text("SELECT Cup.name, Result.rank, Result.points, Result.id, Cup.account_id"
                    " FROM Team, Result, Cup"
                    " WHERE (Team.id = :id AND Result.rank != 0)"
                    " AND Team.id = Result.team_id"
                    " AND Result.cup_id = Cup.id").params(id=id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"cup":row[0], "rank":row[1], "points":row[2], "rid":row[3], "aid":row[4]})

        return response

