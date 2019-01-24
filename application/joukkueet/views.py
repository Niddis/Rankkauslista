from application import app
from flask import render_template, request

@app.route("/joukkueet/new/")
def joukkueet_form():
    return render_template("joukkueet/new.html")

@app.route("/joukkueet", methods=["POST"])
def joukkueet_create():
    print(request.form.get("nimi"))

    return "hello world!"
    