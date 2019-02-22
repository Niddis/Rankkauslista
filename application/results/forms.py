from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators, SelectField, ValidationError, HiddenField
from application.results.models import Result
from application.cups.models import Cup

class ResultForm(FlaskForm):
    cup_id = HiddenField()
    cup_name = SelectField("Turnauksen nimi")
    team_name = SelectField("Joukkueen nimi")

    class Meta:
        csrf = False

class ResultEditRankForm(FlaskForm):
    cup_id = HiddenField()
    rank = IntegerField("Sijoitus", [validators.NumberRange(min=0, message="sijoituksen pitää olla vähintään 0")])

    def validate_rank(self, rank):
        findResult = Result.query.filter_by(rank=rank.data, cup_id=self.cup_id.data).first()
        if findResult is not None:
            raise ValidationError("Sama sijoitus ei voi olla kahdella eri joukkueella")

    class Meta:
        csrf = False

class ResultEditPointsForm(FlaskForm):
    points = IntegerField("Pisteet", [validators.NumberRange(min=0, message="pisteiden pitää olla vähintään 0")])

    class Meta:
        csrf = False