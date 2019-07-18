from http.server import BaseHTTPRequestHandler, HTTPServer
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from urllib.parse import urlparse, parse_qs
from pipenv.vendor.dotenv import load_dotenv
from models.location import Location
from models.weather import Weather
from config import Config
import os
import json
import requests 


load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db) 

@app.route('/location') 
def find_locations_data(): 
  
  query = request.values['location']
  location = Location(query)
  db.session.add(location)
  db.session.commit()
  
  return jsonify(location.data())


@app.route('/weather')
def find_weathers_data(): 
 
  query = request.values['location']
  weather = Weather(Location(query))
  db.session.add(weather)
  db.session.commit()

  return jsonify(weather.data())

from models import Locations
from models import Weathers
