from Measurements import Measurements
from Goals import Goals

class Profile():
    def __init__(self, Username:str, Goals:Goals(), Measurements:Measurements()):
        self.username = Username
        self.goals = Goals
        self.measurements = Measurements

test = Profile