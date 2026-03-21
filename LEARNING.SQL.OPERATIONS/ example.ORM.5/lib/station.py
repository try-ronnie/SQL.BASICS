from __init__ import CURSOR , CONN


class Station:
    all = {}
    def __init__ (self,name: str, capacity: int , location: str , id = None):
        self.name = name
        self.capacity = capacity
        self.location = location
    #creation of the table
    @classmethod
    def create_table(cls):
        '''CREATING the table structure using the cls method'''
        sql = '''
        CREATE TABLE IF NOT EXISTS stations(
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
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all(self.id) = self
        # When you use self in an instance method, self refers to the specific instance of the class. Therefore, type(self) returns the class that the instance belongs to. 
        # so in this cse type(self) = Station then we can notate into it 
        #Bound parameters don’t “clean” input — they prevent it from being interpreted as SQL at all.
#SQLite treats ? as placeholders, and:
    #Separates SQL logic from data
    # Sends the query and the data independently
    # Escapes everything properly

    # we use self.name to refer to the individual  value of the object
    @classmethod
    def create_save (cls , name ,capacity,location):
        '''Create an instance of station and persist it to the table directly'''
        department = cls(name,capacity,location)
        department.save()
        return department
    
    @classmethod
    def drop_table(cls):
        '''drop the entire tation table'''
        sql = '''
            DROP TABLE IF EXISTS stations;
            '''
        CURSOR.execute(sql) 
        CONN.commit()

    

