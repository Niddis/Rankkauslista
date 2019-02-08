from application import app, db
from flask import render_template, request, url_for, redirect
from application.results.forms import ResultForm
from application.joukkueet.models import Joukkue
from application.cups.models import Cup
from application.results.models import Result
from flask_login import login_required

@app.route("/results", methods=["GET"])
def results_index():
    return render_template("results/list.html", results = Result.list_results())

@app.route("/results/new/", methods=["GET"])
@login_required
def result_form():
    form = ResultForm()
    form.cup_name.choices = [(c.id, c.name) for c in Cup.query.order_by(Cup.name)]
    form.joukkue_name.choices = [(j.id, j.name) for j in Joukkue.query.order_by(Joukkue.name)]
    return render_template("results/new.html", form = form)

@app.route("/results/", methods=["POST"])
@login_required
def results_create():
    form = ResultForm(request.form)

    r = Result(form.cup_name.data)
    r.joukkue_id = form.joukkue_name.data

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("results_index"))

@app.route("/results/delete/<result_id>", methods=["POST"])
@login_required
def results_delete(result_id):
    r = Result.query.get(result_id)
    db.session.delete(r)
    db.session().commit()

    return redirect(url_for("results_index"))

@app.route("/results/incpoints/<result_id>", methods=["POST"])
@login_required
def results_inc_points(result_id):
    r = Result.query.get(result_id)
    r.points += 1
    db.session().commit()

    return redirect(url_for("results_index"))

@app.route("/results/decpoints/<result_id>", methods=["POST"])
@login_required
def results_dec_points(result_id):
    r = Result.query.get(result_id)
    r.points -= 1
    db.session().commit()

    return redirect(url_for("results_index"))

@app.route("/results/incrank/<result_id>", methods=["POST"])
@login_required
def results_inc_rank(result_id):
    r = Result.query.get(result_id)
    r.rank += 1
    db.session().commit()

    return redirect(url_for("results_index"))

@app.route("/results/decrank/<result_id>", methods=["POST"])
@login_required
def results_dec_rank(result_id):
    r = Result.query.get(result_id)
    r.rank -= 1
    db.session().commit()

    return redirect(url_for("results_index"))