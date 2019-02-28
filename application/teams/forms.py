from flask_wtf import FlaskForm
from wtforms import StringField, validators

class TeamForm(FlaskForm):
    name = StringField("Joukkueen nimi", [validators.Length(min=3, max=20)])
    home = StringField("Kotipaikka", [validators.Length(min=3, max=20)])

    class Meta:
        csrf = False