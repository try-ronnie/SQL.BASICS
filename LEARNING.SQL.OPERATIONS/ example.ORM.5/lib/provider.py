# creating a class provider ands its table and ways to relate data from the table and back to the class
from __init__ import CONN , CURSOR
class Provider :
    #initialize the instance
    #remember to put the id so that the classes can be mapped to the tables with primary keys 
    def __init__(self , name:str , country:str, capacity:int , price_charge:int, id = None):
        self.name = name 
        self.country = country
        self.capacity = capacity
        self.price_charge = price_charge
        # no self.id = id since python doesnt know how to make the next id unique ... thats sqlite3 's work 
    
    # we want to create the table using the class and connect it to the database 
    # we use cls 
    
    def create_table():

    