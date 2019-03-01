from flask_wtf import FlaskForm
from application.teams.models import Team
from wtforms import StringField, validators, ValidationError

class TeamForm(FlaskForm):
    name = StringField("Joukkueen nimi", [validators.Length(min=3, max=20)])
    home = StringField("Kotipaikka", [validators.Length(min=3, max=20)])

    def validate_name(self, name):
        team = Team.query.filter_by(name=name.data).first()
        if team is not None:
            raise ValidationError("Tämä joukkue on jo olemassa.")
    
    class Meta:
        csrf = False

class TeamEditForm(FlaskForm):
    name = StringField("Joukkueen nimi", [validators.Length(min=3, max=20)])
    home = StringField("Kotipaikka", [validators.Length(min=3, max=20)])

    class Meta:
        csrf = False