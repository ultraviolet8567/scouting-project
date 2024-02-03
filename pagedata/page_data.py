from flask import Flask

competitions = {}

class comp_data:
    def __init__(self, team1, team2, date, id):
        self.team1 = team1
        self.team2 = team2
        self.date = date
        self.id = id
        self.href = "/landing"
        self.caption = team1 + " vs " + team2
        global competitions
        competitions[f'{id}'] = self

exampleComp = comp_data("Ultraviolet 8567", "Some less cool team XYZA", "11/18/27", 22)
print(competitions)
    

    