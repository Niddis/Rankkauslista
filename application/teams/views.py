from application import app, db
from flask import render_template, request, url_for, redirect
from application.teams.models import Team
from application.results.models import Result
from application.teams.forms import TeamForm
from flask_login import login_required, current_user

@app.route("/teams", methods=["GET"])
def teams_index():
    #Jos joukkueella ei ole yhtään tulosta, joukkueiden järjestäminen 
    #tulosten perusteella ei toimi Postgresql:llä oikein. Siksi järjestäminen
    #tapahtuu tässä eikä sql-kyselyn yhteydessä.
    teams = Team.list_teams_with_points()
    for row in teams:
        if row["points"] is None:
            row["points"] = 0
    
    def sortingFunc(e):
        return e["points"]

    teams.sort(reverse=True, key=sortingFunc)
    return render_template("teams/list.html", teams = teams)

@app.route("/teams/new/")
@login_required
def teams_form():

    if current_user.isAdmin == False:
        return redirect(url_for("teams_index"))

    return render_template("teams/new.html", form = TeamForm())

@app.route("/teams", methods=["POST"])
@login_required
def teams_create():
    if current_user.isAdmin == False:
        return redirect(url_for("teams_index"))
    
    form = TeamForm(request.form)

    if not form.validate():
        return render_template("teams/new.html", form = form)

    t = Team(form.name.data)
    t.home = form.home.data

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("teams_index"))

@app.route("/teams/delete/<team_id>", methods=["POST"])
@login_required
def teams_delete(team_id):
    if current_user.isAdmin == False:
        return redirect(url_for("teams_index"))

    t = Team.query.get(team_id)

    db.session.query(Result).filter_by(team_id=team_id).delete()
    db.session.delete(t)
    db.session().commit()

    return redirect(url_for("teams_index"))

@app.route("/teams/edit/<team_id>", methods=["GET", "POST"])
@login_required
def teams_edit(team_id):
    if current_user.isAdmin == False:
        return redirect(url_for("teams_index"))

    t = Team.query.get(team_id)

    if request.method == 'GET':
        form = TeamForm()
        form.name.data = t.name
        form.home.data = t.home
        return render_template("teams/edit.html", form = form)

    form = TeamForm(request.form)

    if request.method == "POST" and form.validate():
        t.name = form.name.data
        t.home = form.home.data
        db.session().commit()
        return redirect(url_for("teams_index"))

    return render_template("teams/edit.html", form = form)
