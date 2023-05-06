# Makes a user that appears in the database. This is so that we can store the information in a concise way. All infomration gotten from https://www.youtube.com/watch?v=dam0GPOAvVI&t=6290s

from appbase import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    password = db.Column(db.String(150))
    measurements = db.Column(db.PickleType)
    # goals = db.Column(db.PickleType)


