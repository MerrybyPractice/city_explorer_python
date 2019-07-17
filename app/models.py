from app import db

class Location(db.Model): 

  id = db.Column(db.Integer, primary_key=True) 
  