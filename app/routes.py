from flask.helpers import url_for
import requests
from flask import render_template, request, redirect
from app import app

BASE_URL = "https://api.opendota.com/api"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        heroes = requests.get(f"{BASE_URL}/heroes").json()
        return render_template("index.html", heroes=heroes)
    else:
        steam32_id = request.form['steam32_id']
        hero_id = request.form['hero_id']

        return redirect(url_for('hero_data', steam32_id=steam32_id, hero_id=hero_id))


@app.route("/hero_data/<steam32_id>/<hero_id>")
def hero_data(steam32_id, hero_id):
    return {"steam32_id": steam32_id, "hero_id": hero_id}
