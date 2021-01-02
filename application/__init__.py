from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy 
#from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:1234@34.105.208.208/crud_app"
app.config["SECRET_KEY"] = "asdasda"
db = SQLAlchemy(app)

from application import routes 