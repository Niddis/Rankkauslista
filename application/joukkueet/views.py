from application import app, db
from flask import render_template, request, url_for, redirect
from application.joukkueet.models import Joukkue
from application.joukkueet.forms import JoukkueForm
from flask_login import login_required

@app.route("/joukkueet", methods=["GET"])
def joukkueet_index():
    return render_template("joukkueet/list.html", joukkueet = Joukkue.list_teams_with_points())

@app.route("/joukkueet/new/")

def joukkueet_form():
    return render_template("joukkueet/new.html", form = JoukkueForm())

@app.route("/joukkueet", methods=["POST"])

def joukkueet_create():
    form = JoukkueForm(request.form)

    if not form.validate():
        return render_template("joukkueet/new.html", form = form)

    j = Joukkue(form.name.data)
    j.home = form.home.data

    db.session().add(j)
    db.session().commit()

    return redirect(url_for("joukkueet_index"))
