from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PlayersForm(FlaskForm):
    name = StringField('Name of Player', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    submit = SubmitField('Add player')

class TeamForm(FlaskForm):
    team_name = StringField('Name of New Team', validators=[DataRequired()])
    sponsor = StringField('Name of New Sponsor', validators=[DataRequired()])
    submit = SubmitField('Done') 
