from flask import Flask

competitions = {}

class comp_data:
    def __init__(team1, team2, date, id):
        self.team1 = team1
        self.team2 = team2
        self.date = date
        self.id = id
        global competitions
        competitions[f'{id}'] = self
    

    