from flask import request, Flask, jsonify, abort
import json
from flask_sqlalchemy import SQLAlchemy
from config import Config
from os import environ

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

DENSITY_KEY = environ.get('DENSITY_KEY')

halls = ['ferris', 'johnjay', 'jjs', 'hewitt', 'diana']

@app.route('/home', methods=['GET'])
def home():
    data = json.load(open('home.json'))
    return data

@app.route('/hall/<string:hallname>', methods=['GET'])
def hall_menu(hallname):
    data = [ json.load(open(hall + '.json')) for hall in halls ]
    if hallname in halls:
        return data[halls.index(hallname)]
    return abort(404)