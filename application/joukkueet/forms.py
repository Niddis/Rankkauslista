from flask_wtf import FlaskForm
from wtforms import StringField, validators

class JoukkueForm(FlaskForm):
    name = StringField("Joukkueen nimi", [validators.Length(min=3)])

    class Meta:
        csrf = False