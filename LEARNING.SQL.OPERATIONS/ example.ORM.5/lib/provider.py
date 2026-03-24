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
    @classmethod
    def create_table(cls):
        ''' CREATING THE PROVIDER TABLE STRUCTURE'''
        sql = '''
            CREATE TABLE IF NOT EXISTS PROVIDER (
            id INTERGER PRIMARY KEY,
            name TEXT NOT NULL ,
            country TEXT NOT NULL CHECK(country in ('UGANDA','ETHIOPIA','TANZANIA','SUDAN')),
            capacity integer NOT NULL CHECK (capacity > 15000),
            price_charge integer;
            )
            '''
        CURSOR.execute(sql)
        CONN.commit()
    
    # this persists **an instance that is already made** to the table
    # bound prmeters
    # we use self since this method takes a class instances(self) then persists it to the table
    def save (self):
        ''' PERSISTS AN ALREADY MADE INSTANCE TO THE TABLE'''
        sql = '''
        INSERT INTO provider (name , country ,capacity , price_charge) VALUES (?,?,?,?);
        '''
        CURSOR.execute(sql,(self.name,self.country,self.capacity, self.price_charge))
        CONN.commit()
    
    @classmethod
    def Update_value(cls):
        '''UPDATES VALUE IN A TABLE ROW'''
        sql = '''
        UPDATE TABLE provider 
        '''


    