from flask import Flask
from flask import render_template
from pagedata import page_data

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p> \n <a href='/landing'>Landing</a>"

@app.route("/landing")
def landing():
    return render_template("landing.html", competitions=page_data.competitions)

@app.route("/competitions/<string:competition>")
def competition_page():
    return render_template("competition.html")

