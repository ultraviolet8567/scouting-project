from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

competitions = {}
matches = {}

class comp_data:
    def __init__(self, caption, date, id):
        self.date = date
        self.id = id
        self.href = f'/competitions/{id}'
        self.caption = caption
        global competitions
        competitions[f'{id}'] = self
        matches[f'{id}'] = {}


exampleComp = comp_data("Week Zero", "11/18/27", 22)
exampleComp2 = comp_data("Middle of Nowhere Day 1", "11/11/11", 23)

class match_data:
    def __init__(self, team1, team2, time, compID, id):
        self.team1 = team1
        self.team2 = team2
        self.time = time
        self.compID = compID
        self.id = id
        matches[f'{compID}'][f'{id}'] = self