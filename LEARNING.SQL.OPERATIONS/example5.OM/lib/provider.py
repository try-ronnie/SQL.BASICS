from __init__ import CURSOR , CONN

class Provider:
    #cache
    all = {}
    def __init__(self, name , capacity , country , id= None):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.country = country

    @classmethod
    def create_table(cls):
        '''CREATE PROVIDER TBALE '''
        sql = '''
            CREATE TABLE IF NOT EXISTS providers(
            id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL, 
            capacity INTEGER CHECK (capacity > 5000),
            country TEXT CHECK (country in ('SUDAN','SOMALIA','TANZANIA','UGANDA'))
            );
            '''
        CURSOR.execute(sql)
        CONN.commit()
    
    #persist provider instances to the table and update dache memory instance id
    def save (self):
        ''' PESIST BOTH DB AND CACHE , DB AS SOUCE OF TUTH'''
        sql = '''
            INSERT INTO providers (name, capacicty , name) VAALUES (?,?,?);
            '''
        CURSOR.execute(sql ,(self.name , self.capacity , self.country))
        self.id = CURSOR.lastrowid # give the id so that you can piush with the correct id to cache
        type(self).all[self.id] = self # store persisted value to cache 
    
    @classmethod
    def drop_table (cls):
        sql