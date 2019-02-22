from application import app, db
from flask import render_template, request, url_for, redirect
from application.results.forms import ResultForm, ResultEditRankForm, ResultEditPointsForm
from application.teams.models import Team
from application.cups.models import Cup
from application.results.models import Result
from flask_login import login_required, current_user

@app.route("/results", methods=["GET"])
def results_index():
    return render_template("results/list.html", results = Result.list_results())

@app.route("/results/new/<id>", methods=["GET"])
#@login_required
def result_form(id):
    form = ResultForm()
    form.team_name.choices = [(t.id, t.name) for t in Team.query.order_by(Team.name)]
    return render_template("results/new.html", form = form, results = Result.find_results_by_cup(id), cup = Cup.query.get(id))

@app.route("/results/team/<id>", methods=["GET"])
def result_form_for_team(id):
    return render_template("results/show.html", results = Result.find_results_by_team(id), team = Team.query.get(id))

@app.route("/results/<id>", methods=["GET","POST"])
@login_required
def results_create(id):
    c = Cup.query.get(id)
    form = ResultForm(request.form)

    if c.account_id != current_user.id:
        return redirect(url_for("result_form", id=id))
        
    form = ResultForm(request.form)
    r = Result(form.cup_id.data)
    r.cup_id = id
    r.team_id = form.team_name.data

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("result_form", id=id))

@app.route("/results/delete/<result_id>", methods=["POST"])
@login_required
def results_delete(result_id):
    r = Result.query.get(result_id)
    c = Cup.query.get(r.cup_id)

    if c.account_id != current_user.id:
        return redirect(url_for("result_form", id=c.id))
    
    db.session.delete(r)
    db.session().commit()

    return redirect(url_for("result_form", id=c.id))

@app.route("/results/edit/<result_id>", methods=["GET", "POST"])
@login_required
def results_edit_rank(result_id):
    r = Result.query.get(result_id)
    c = Cup.query.get(r.cup_id)

    if c.account_id != current_user.id:
        return redirect(url_for("result_form", id=c.id))

    form = ResultEditRankForm(obj=r)
    if request.method == "POST" and form.validate():
        r.rank = form.rank.data
        db.session().commit()
        return redirect(url_for("result_form", id=r.cup_id))

    return render_template("results/edit.html", form = form, cup = c, team = Team.query.get(r.team_id))

@app.route("/results/editpoints/<result_id>", methods=["GET", "POST"])
@login_required
def results_edit_points(result_id):
    r = Result.query.get(result_id)
    c = Cup.query.get(r.cup_id)

    if c.account_id != current_user.id:
        return redirect(url_for("result_form", id=c.id))

    form = ResultEditPointsForm(request.form)
    if request.method == "POST" and form.validate():
        r.points = form.points.data
        db.session().commit()
        return redirect(url_for("result_form", id=r.cup_id))

    return render_template("results/editPoints.html", form = form, cup = c, team = Team.query.get(r.team_id))
