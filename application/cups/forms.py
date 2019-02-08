from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, IntegerField, validators

class CupForm(FlaskForm):
    name = StringField("Turnauksen nimi", [validators.Length(min=1)])
    start_time = StringField("Turnaus alkaa", [validators.Length(min=1)])
    end_time = StringField("Turnaus päättyy", [validators.Length(min=1)])
    points = IntegerField("Turnauksessa jaettavat pisteet")

    class Meta:
        csrf = False