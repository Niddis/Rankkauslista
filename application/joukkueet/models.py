from application import db

class Joukkue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    nimi = db.Column(db.String(144), nullable=False)
    kotipaikka = db.Column(db.String(144), nullable=False)
    perustettu = db.Column(db.String(144), nullable=False)
    rankkauspisteet = db.Column(db.Integer, nullable=False)
    rankkausarvo = db.Column(db.Integer, nullable=False)

    def __init__(self, nimi, kotipaikka, perustettu):
        self.nimi = nimi
        self.kotipaikka = kotipaikka
        self.perustettu = perustettu
        self.rankkauspisteet = 0
        self.rankkausarvo = 0

