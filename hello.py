from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from pagedata import page_data

app = Flask(__name__)
#db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p> \n <a href='/landing'>Landing</a>"

@app.route("/landing")
def landing():
    return render_template("landing.html", competitions=page_data.competitions)

@app.route("/competitions/<string:competition>")
def competition_page(competition):
    return render_template("competition.html", comp=page_data.competitions[competition], matches=page_data.matches[competition])

#add some approut for post here
#there should be a column comp id, match id, team #, data, scout
#def addTeam():
#    #change this later
#    teamObj = placeHolderFunction()
#    for attr in dir(teamObj):
#        if not attr.startswith("__"):
            
