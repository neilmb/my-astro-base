import os

from flask import Flask, escape
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def home():
    
    app_str = escape(repr(app))
    db_str = escape(repr(db))
    return "App {} is alive using db {}.".format(app_str, db)
