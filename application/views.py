from flask import render_template
from application import app
from application.cups.models import Cup

@app.route("/")
def index():
    return render_template("index.html", cups = Cup.list_cups_with_teams())