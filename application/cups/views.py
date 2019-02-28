from application import app, db
from flask import render_template, request, url_for, redirect
from application.cups.models import Cup
from application.results.models import Result
from application.cups.forms import CupForm, CupEditForm
from flask_login import login_required, current_user


@app.route("/cups", methods=["GET"])
def cups_index():
    cups = Cup.query.all()

    return render_template("cups/list.html", cups = cups)

@app.route("/cups/new/")
@login_required
def cups_form():
    return render_template("cups/new.html", form = CupForm())

@app.route("/cups", methods=["POST"])
@login_required
def cups_create():
    form = CupForm(request.form)

    if not form.validate():
        return render_template("cups/new.html", form = form)

    c = Cup(form.name.data)
    c.start_time = form.start_time.data
    c.end_time = form.end_time.data
    c.points = form.points.data
    c.account_id = current_user.id
    db.session().add(c)
    db.session().commit()

    return redirect(url_for("cups_index"))

@app.route("/cups/delete/<cup_id>", methods=["POST"])
@login_required
def cups_delete(cup_id):
    c = Cup.query.get(cup_id)

    if c.account_id != current_user.id and current_user.isAdmin == False :
        return render_template("cups/list.html", cups = Cup.query.all(), error = 'Sinulla ei ole oikeuksia poistaa tätä turnausta')

    db.session.query(Result).filter_by(cup_id=cup_id).delete()
    db.session.delete(c)
    db.session().commit()

    return redirect(url_for("cups_index"))

@app.route("/cups/edit/<cup_id>", methods=["GET", "POST"])
@login_required
def cups_edit(cup_id):
    c = Cup.query.get(cup_id)

    if c.account_id != current_user.id and current_user.isAdmin == False:
        return render_template("cups/list.html", cups = Cup.query.all(), error = 'Sinulla ei ole oikeuksia muokata tätä turnausta')

    if request.method == 'GET':
        form = CupForm()
        form.name.data = c.name
        form.start_time.data = c.start_time
        form.end_time.data = c.end_time
        form.points.data = c.points
        return render_template("cups/edit.html", form = form)
    
    form = CupForm(request.form)

    if request.method == "POST" and form.validate():
        c.name = form.name.data
        c.start_time = form.start_time.data
        c.end_time = form.end_time.data
        c.points = form.points.data
        db.session().commit()
        return redirect(url_for("cups_index"))

    return render_template("cups/edit.html", form = form)
