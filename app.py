from flask import (
    abort, Flask, jsonify, redirect, render_template, request,
    session, url_for
)
from flask_sqlalchemy import SQLAlchemy
import os 

app = Flask(__name__)
app.secret_key = b'REPLACE_ME_x#pi*CO0@^z_beep_beep_boop_boop'

sqlite_uri = 'sqlite:///' + os.path.abspath(os.path.curdir) + '/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = sqlite_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User

@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/')
def fortune():
    return '<pre>' + os.system(fortune) + '</pre>'

@app.route('/cowsay/<message>/')
def cowsay(message):
    return '<pre>' + os.system(cowsay message) + '</pre>'

@app.route('/cowfortune/')
def cowfortune():
    return '<pre>' + os.system(fortune | cowsay) + '</pre>'

