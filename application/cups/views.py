from application import app, db
from flask import render_template, request, url_for, redirect
from application.cups.models import Cup
from application.cups.forms import CupForm


@app.route("/cups", methods=["GET"])
def cups_index():
    return render_template("cups/list.html", cups = Cup.query.all())

@app.route("/cups/new/")
def cups_form():
    return render_template("cups/new.html", form = CupForm())

@app.route("/cups", methods=["POST"])
def cups_create():
    form = CupForm(request.form)

    if not form.validate():
        return render_template("cups/new.html", form = form)

    c = Cup(form.name.data)
    c.start_time = form.start_time.data
    c.end_time = form.end_time.data
    c.points = form.points.data

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("cups_index"))

