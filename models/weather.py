import requests
import os
from datetime import datetime

WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')

class Weather: 

  def __init__(self, location):
      self.saved_data = None
      self.location = location

  def data(self): 
    if not self.saved_data: 
      self.saved_data = requests.get(f'https://api.darksky.net/forecast/{WEATHER_API_KEY}/{self.location.data()["latiude"]},{self.location.data()["longitude"]}').json()
    return [{'forecast': i['summary'],'time': self.get_day_from_epoch(i['time'])} for i in self.saved_data['daily']['data']]
    
  def get_day_from_epoch(self, epoch_time_stamp):
    return datetime.utcfromtimestamp(epoch_time_stamp).strftime("%A %B %d, %Y")
