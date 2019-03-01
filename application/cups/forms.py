from flask_wtf import FlaskForm
from application.cups.models import Cup
from wtforms import StringField, DateTimeField, IntegerField, validators, ValidationError

class CupForm(FlaskForm):
    name = StringField("Turnauksen nimi", [validators.Length(min=3, max=20)])
    start_time = DateTimeField("Turnaus alkaa", description='Anna muodossa VVVV-KK-PP TT:MM:SS')
    end_time = DateTimeField("Turnaus päättyy", description='Anna muodossa VVVV-KK-PP TT:MM:SS')
    points = IntegerField("Turnauksessa jaettavat pisteet", [validators.NumberRange(min=0, max=500, message="pisteiden pitää olla vähintään 0 ja korkeintaan 500")])

    def validate_name(self, name):
        cup = Cup.query.filter_by(name=name.data).first()
        if cup is not None:
            raise ValidationError("Tämä turnaus on jo olemassa.")
    
    class Meta:
        csrf = False
