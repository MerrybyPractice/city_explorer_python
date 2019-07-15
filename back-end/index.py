from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from pipenv.vendor.dotenv import load_dotenv
import os
import json
import requests 

load_dotenv()

'''
1. get/locations
  - need to be able to process HTTP requests, send to API, parse and utilize data that is brought back. 
  class: extend Base Http Request Handler 
    do_GET(self)  
   PATH PARSEING?  
  Instead of   
2. data parseing?  
  - class  
'''
class SimpleHttpRequestHandler(BaseHTTPRequestHandler): 
  def do_GET(self): 
    parsed_path = urlparse(self.path)
    parsed_qs = parse_qs(parsed_path.query)

    if parsed_path.path == '/locations': 

      api_key = os.getenv('GEOCODE_API_KEY')
     
      lat = parsed_qs['latitude'] 
      long = parsed_qs['longitude']

      url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{long}&key={api_key}'

      result = requests.get(url).json()
      

    if parsed_path.path == '/weather': 

      api_key = os.getenv('WEATHER_API_KEY')

      lat = parsed_qs['latitude'] 
      long = parsed_qs['longitude'] 

      url = f'https://api.darksky.net/forecast/{api_key}/{lat},{long}'
      
      result = requests.get(url).json() 

def create_server(): 
  PORT = os.getenv('PORT')
  return HTTPServer(
    ('127.0.0.1', PORT), SimpleHttpRequestHandler
  )

def run_forever(): 
  PORT = os.getenv('PORT')
  server = create_server()

  try: 
    print(f'Starting up on port', PORT)
    server.serve_forever() 
  except KeyboardInterrupt: 
    server.server_close()
    server.shutdown() 

if __name__ =='__main__': 
  run_forever()      
