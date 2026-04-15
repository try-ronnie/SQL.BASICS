from __init__ import CURSOR , CONN

class Department:
    # this creates an instance of the 
    def __init__(self, name , location , id=None):
        self.id = id
        self.name = name
        self.location = location