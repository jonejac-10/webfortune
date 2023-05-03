from flask import (
    abort, Flask, jsonify, redirect, render_template, request,
    session, url_for
)
from flask_sqlalchemy import SQLAlchemy
import os 
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/')
def fortune():
    output = subprocess.check_output(['fortune']).decode()
    return '<pre>' + output + '</pre>'

@app.route('/cowsay/<message>/')
def cowsay(message):
    output = subprocess.check_output(['cowsay', message]).decode()
    return '<pre>' + output + '</pre>'

@app.route('/cowfortune/')
def cowfortune(): 
    text = subprocess.check_output(['fortune']).decode()
    output = subprocess.check_output(['cowsay', text]).decode() 
    return '<pre>' + output + '</pre>'
    
