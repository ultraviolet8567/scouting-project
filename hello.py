from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from pagedata import page_data
import os

app = Flask(__name__)
db = SQLAlchemy(app)
env_config = os.getenv("APP_SETTINGS", "config.Config")
app.config.from_object(env_config)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p> \n <a href='/landing'>Landing</a>"

@app.route("/landing")
def landing():
    return render_template("landing.html", competitions=page_data.competitions)

@app.route("/competitions/<string:competition>")
def competition_page(competition):
    return render_template("competition.html", comp=page_data.competitions[competition], matches=page_data.matches[competition])

@app.route("/matches/<string:competition>/<string:match>")
def match_page(competition, match):
    return render_template("match.html", match=page_data.matches[competition][match], compID=competition, matchID=match)

#add some approut for post here
#there should be a column comp id, match id, team #, data, scout
@app.route("outdata/<string:competition>/<string:match>")
def addTeam(competition, match):
    #change this later
    compId = competition
    matchID = match
    teamNum = request.form.get('teamNum')
    scout = request.form.get('scout')
    extraData = request.form.get('extraData')
    team = {
        "compId" : compId,
        "matchID" : matchID,
        "teamNum" : teamNum,
        "scout" : scout,
        "extraData" : extraData
    }
    db.session.add(team)
    db.session.commit()
    
    

