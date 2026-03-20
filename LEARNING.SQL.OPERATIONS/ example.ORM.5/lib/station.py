from __init__ import CURSOR , CONN


class Station:
    def __init__ (self,name: str, capacity: int , location: str , id = None):
        self.name = name
        self.capacity = capacity
        self.location = location
    #creation of the table
    def create_table(cls):
        '''CREATING the table structure using the cls method'''
        sql = '''
        CREATE TABLE stations IF NOT EXISTS(
        id INTEGER PRIMARY KEY , 
        name TEXT NOT NULL, 
        capacity INTEGER CHECK (capacity > 1000),
        location TEXT NOT NULL
        );
        '''
        CURSOR.execute(sql)
        CONN.commit()
    def save (self):
        '''persisting already existing instances to the table'''
        sql = '''
        INSERT INTO stations (name , capacity , location)
        VALUES (?,?,?);
        '''
        CURSOR.execute(sql,(self.name , self.capacity , self.location))
        #Bound parameters don’t “clean” input — they prevent it from being interpreted as SQL at all.
#SQLite treats ? as placeholders, and:
    #Separates SQL logic from data
    # Sends the query and the data independently
    # Escapes everything properly

    # we use self.name to refer to the individual  value of the object
