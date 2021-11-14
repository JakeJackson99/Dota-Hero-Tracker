from flask.helpers import url_for
import requests
from flask import render_template, request, redirect
from app import app
from app.utility import match_results

BASE_URL = "https://api.opendota.com/api"

results = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        steam32_id = request.form['steam32_id']
        hero_id = request.form['hero_id']

        return redirect(url_for('hero_data', steam32_id=steam32_id, hero_id=hero_id))
    else:
        heroes = requests.get(f"{BASE_URL}/heroes").json()
        return render_template("index.html", heroes=heroes)


@app.route("/hero_data/<steam32_id>/<hero_id>")
def hero_data(steam32_id, hero_id):
    results = match_results(steam32_id, hero_id)

    return render_template("hero.html")


@app.route('/get_data')
def get_data():
    if results:
        return results

    return redirect(url_for('index', message="Empty results list; please input data"))  
