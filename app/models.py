from .flask_app import db

class Locations(db.Model): 

  id = db.Column(db.Integer, primary_key=True) 
  formatted_query = db.Column(db.String(256), unique=True)
  search_query = db.Column(db.String(500))
  latitude = db.Column(db.Float())
  longitude = db.Column(db.Float())

  def seralize(self): 
    return { 
      'formatted_query' : self.formatted_query,
      'search_query' : self.search_query, 
      'latitude' : self.latitude, 
      'longitude' : self.longitude
    }

class Weathers(db.Model): 

  id = db.Column(db.Integer, primary_key=True) 
  forecast = db.Column(db.Text())
  time = db.Column(db.DateTime(), unique=True)

  def searlize(self): 
    return{ 
      'forecast' : self.forecast,
      'time' : self.time
    }
