from application import db 

class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(50), nullable=False)
    sponsor = db.Column(db.String(50), nullable=False)
    players = db.relationship('Players', cascade="all,delete", backref='team')
    


class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(3), nullable=False)
    club = db.Column(db.String(50), nullable=False)
    height = db.Column(db.Float, nullable=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)


    


