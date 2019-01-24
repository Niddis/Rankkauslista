from application import db

class Joukkue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    nimi = db.Column(db.String(144), nullable=False)
    rankkausarvo = db.Column(db.Integer, nullable=False)

    def __init__(self, nimi):
        self.nimi = nimi
        self.rankkausarvo = 0

