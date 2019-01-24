from flask import render_template, request, redirect, url_for
from application import app, db
from application.joukkueet.models import Joukkue

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/joukkueet/new/")
def joukkueet_form():
    return render_template("joukkueet/new.html")

@app.route("/joukkueet", methods=["POST"])
def joukkueet_create():
    j = Joukkue(request.form.get("nimi"))

    db.session().add(j)
    db.session().commit()

    return redirect(url_for("joukkueet_index"))

@app.route("/joukkueet", methods=["GET"])
def joukkueet_index():
    return render_template("joukkueet/list.html", joukkueet = Joukkue.query.all())

@app.route("/joukkueet/<joukkue_id>", methods=["POST"])
def joukkueet_increase_ra(joukkue_id):
    j = Joukkue.query.get(joukkue_id)
    j.rankkausarvo += 1
    db.session().commit()

    return redirect(url_for("joukkueet_index"))
