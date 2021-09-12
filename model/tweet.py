from db.Connection import db
class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    userId = db.Column(db.Integer)
    message = db.Column(db.String(100))