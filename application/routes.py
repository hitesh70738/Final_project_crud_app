from application import app, db
from application.models import Players, Teams
from application.forms import TeamForm, PlayersForm
from flask import render_template, request, redirect, url_for

@app.route("/")
@app.route("/home")
def home():
    all_teams = Teams.query.all()
    output = ""
    return render_template("index.html", title = "Home", all_teams=all_teams)   

@app.route('/create', methods=["GET","POST"])
def create():
    form = TeamForm() 
    if request.method == "POST":
        new_team=Teams(team_name=form.team_name.data, sponsor=form.sponsor.data) 
        db.session.add(new_team)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html", title="Create a Team", form=form)

@app.route('/add/<int:id>', methods=["GET","POST"])
def add(id):
    form = PlayersForm()
    all_players = Players.query.filter_by(team_id=id).all()
    isLimitReach = len(all_players) >= 5
    if request.method == "POST" and len(all_players) < 5:
        new_player = Players(name=form.name.data, position=form.position.data, team_id=id, club=form.club.data, height=form.height.data if form.height.data else None)
        db.session.add(new_player)
        db.session.commit()
        return redirect(url_for("add", id=id))
    return render_template("player.html", title = "Add Players", form=form, all_players=all_players, isLimitReach=isLimitReach)



@app.route('/update/<int:id>', methods=["GET","POST"])
def update(id):
    form = TeamForm()
    teams = Teams.query.filter_by(id=id).first()
    if request.method == "POST":
        teams.team_name = form.team_name.data
        teams.sponsor = form.sponsor.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("update.html", form=form, title="Updated Team", teams=teams)


@app.route('/delete/<int:id>', methods=["GET", "POST"])
def delete(id):
    first_team = Teams.query.filter_by(id=id).first()
    db.session.delete(first_team)
    db.session.commit()
    return redirect(url_for("home"))



#@app.route("/add/<name>")
#def add(name):
#    new_player = Players(name=name)
#    db.session.add(new_player)
#    db.session.commit()
#    return "Added new player"

#@app.route('/read')
#def read():
#    all_players = Players.query.all()
#    player_string = "-->"
#    for player in all_players:
#        player_string += " " + player.name
#    return player_string




#@app.route('/update/<name>')
#def update(name):
#    first_player = Players.query.first()
#    first_player.name = name
#    db.session.commit()
#    return first_player.name    




