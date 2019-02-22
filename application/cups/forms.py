from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, IntegerField, validators

class CupForm(FlaskForm):
    name = StringField("Turnauksen nimi", [validators.Length(min=1)])
    start_time = DateTimeField("Turnaus alkaa", description='Anna muodossa VVVV-KK-PP TT:MM:SS')
    end_time = DateTimeField("Turnaus päättyy", description='Anna muodossa VVVV-KK-PP TT:MM:SS')
    points = IntegerField("Turnauksessa jaettavat pisteet", [validators.NumberRange(min=0, message="pisteiden pitää olla vähintään 0")])

    class Meta:
        csrf = False

class CupEditForm(FlaskForm):
    start_time = DateTimeField("Turnaus alkaa", description='Anna muodossa VVVV-KK-PP TT:MM:SS')
    end_time = DateTimeField("Turnaus päättyy", description='Anna muodossa VVVV-KK-PP TT:MM:SS')
    points = IntegerField("Turnauksessa jaettavat pisteet", [validators.NumberRange(min=0, message="pisteiden pitää olla vähintään 0")])
    
    class Meta:
        csrf = False