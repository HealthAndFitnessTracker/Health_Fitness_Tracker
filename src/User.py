# Makes a user that appears in the database. This is so that we can store the information in a concise way. All infomration gotten from https://www.youtube.com/watch?v=dam0GPOAvVI&t=6290s

from appbase import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    password = db.Column(db.String(150))
    measurements = db.Column(db.PickleType)
    # weight = db.Column(db.Integer)
    # chest = db.Column(db.Integer)
    # chest_height = db.Column(db.Integer)
    # left_arm = db.Column(db.Integer)
    # left_arm_height = db.Column(db.Integer)
    # right_arm = db.Column(db.Integer)
    # right_arm_height = db.Column(db.Integer)
    # stomach = db.Column(db.Integer)
    # stomach_height = db.Column(db.Integer)
    # hips = db.Column(db.Integer)
    # hips_height = db.Column(db.Integer)
    # left_thigh = db.Column(db.Integer)
    # left_thigh_height = db.Column(db.Integer)
    # right_thigh = db.Column(db.Integer)
    # right_thigh_height = db.Column(db.Integer)
    # measurements = db.Column(db.array)


