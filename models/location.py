
import requests
import os

GEOCODE_API_KEY = os.environ.get('GEOCODE_API_KEY')

class Location: 
  def __init__(self, query):
    self.saved_data = None
    self.query = query
  
  def data(self):
    if not self.saved_data:
      self.saved_data = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={self.query}&key={GEOCODE_API_KEY}').json()
    response = {
      'formatted_query': self.saved_data['results'][0]['formatted_address'],
      'search_query' : self.query,
      'latiude' : self.saved_data['results'][0]['geometry']['location']['lat'], 
      'longitude' : self.saved_data['results'][0]['geometry']['location']['lng']
    }
    return response

  def seralize(self): 
    return { 
      'formatted_query' : self.formatted_query,
      'search_query' : self.search_query, 
      'latitude' : self.latitude, 
      'longitude' : self.longitude
    }

  def seralize_query(self, query): 
    return{
      'search_query' : query
    }
