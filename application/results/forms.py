from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators, SelectField, HiddenField

class ResultForm(FlaskForm):
    cup_name = SelectField("Turnauksen nimi")
    joukkue_name = SelectField("Joukkueen nimi")

    class Meta:
        csrf = False