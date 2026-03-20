from __init__ import CURSOR , CONN


class Station:
    def __init__ (self,name: str, capacity: int , location: str , id = None):
        self.name = name
        self.capacity = capacity
        self.location = location
    #creation of the table
    def create_table(cls):
        '''CREATING the table structure using the cls method'''
        