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
  
  return jsonify(location.data())


@app.route('/weather')
def find_weathers_data(): 
 
  query = request.values['location']
  weather = Weather(Location(query))

  return jsonify(weather.data())


#-------------------------------------------------

# class SimpleHttpRequestHandler(BaseHTTPRequestHandler): 
#   def do_GET(self): 

#     parsed_path = urlparse(self.path)
#     parsed_qs = parse_qs(parsed_path.query)

#     if parsed_path.path == '/locations' and parsed_qs.get('data'): 

#       api_key = os.getenv('GEOCODE_API_KEY')
     
#       lat = parsed_qs['latitude'] 
#       long = parsed_qs['longitude']

#       url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{long}&key={api_key}'

#       result = requests.get(url).json()
      

#     if parsed_path.path == '/weather': 

#       api_key = os.getenv('WEATHER_API_KEY')

#       lat = parsed_qs['latitude'] 
#       long = parsed_qs['longitude'] 

#       url = f'https://api.darksky.net/forecast/{api_key}/{lat},{long}'
      
#       result = requests.get(url).json() 

# def create_server(): 
#   PORT = os.getenv('PORT')
#   return HTTPServer(
#     ('127.0.0.1', PORT), SimpleHttpRequestHandler
#   )

# def run_forever(): 
#   PORT = os.getenv('PORT')
#   server = create_server()

#   try: 
#     print(f'Starting up on port', PORT)
#     server.serve_forever() 
#   except KeyboardInterrupt: 
#     server.server_close()
#     server.shutdown() 

# if __name__ =='__main__': 
#   run_forever()      
