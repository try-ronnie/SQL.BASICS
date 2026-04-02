from __init__ import CURSOR , CONN

class Oil_station:
    # intantiate instances 
    all = {}
    def __init__(self,name,reserve_litres, location , provider_id , id=None):
        self.id = id 
        self.name = name 
        self.reserve_litres = reserve_litres
        self.location = location
        self.provide_id = provider_id # this is a foreign key


    #create table oil_stations 
    @classmethod
    def create_table (cls):
        '''CREATE TABLE OIL_STATIONS '''
        sql = '''
        CREATE TABLE IF NOT EXISTS oil_stations(
        id INTEGER PRIMARY KEY , 
        name TEXT NOT NULL , 
        reserve_litres INTEGER NOT NULL CHECK(reserve_litres > 10000), 
        location TEXT NOT NULL ,
        provider_id TEXT NOT NULL,
        FOREIGN KEY (provider_id) REFERENCES provider(id)
        );
        '''
        CURSOR.execute(sql)
        CONN.commit()

    #drop the whole existing table
    @classmethod
    def drop_table (cls):
        '''DROP THE WHOLE TABLE'''
        sql = '''
            DROP TABLE IF EXISTS oil_stations ;
            '''
        CURSOR.execute(sql)
        CONN.commit()

    
    #method to save an instance to cache and persist it to the database
    def save(self):
        '''PERSIST INSTANCE TO DB AND UPDATE CAC'''
        sql = '''
        INSERT INTO oil_station(name,reserve_litres,location , provider_id) VALUES (?,?,?,?);
        '''
        self.id = CURSOR.lastrowid
        CURSOR.execute(sql , (self.name ,self,self.reserve_litres , self.location, self.provide_id))
        type(self).all[self.id] = self # this adds to the cache data to allow the returning back of the data
        CONN.commit


    #but we would want to create it automatically and push the instance to the database
    @classmethod
    def create_save(cls,name,reserve_litres,location , provider_id):
        '''INSTANLY CREATE AN INSERT WITH THE PASSED VALUES AND PERSIST IT TO THE DATABASE'''
        oil_station = cls(name , reserve_litres , location , provider_id)
        oil_station.save()#remember to save the function

    # we use self ... ince it work on the table row
    # we dont pass value since we use the instance created .... and according to the WHERE provided it adds the data
    def update_all(self):
        '''UPDATE ALL THE TABLES DATA'''
        sql = '''   
        UPDATE oil_stations
        SET name = ? , reserve_litres = ? , location = ? , provider_id
        ;
        '''
        CURSOR.execute(sql,(self.name , self.reserve_litres, self.location , self.provide_id))
        CONN.commit
        type(self).all[self.id] = self
        
    
    ##ADDING AN ALTER QUERY LATER ON


    # recieving a row from the db
    def instance_from_db(cls , row):
        
        oil_station = cls.all.get(row[0]) # this gets a whole instance from our dict using the keys that were passed on as the ids of each table row
        if oil_station:
            oil_station.name = row[1]
            oil_station.reserve_litres = row[2]
            oil_station.location = row[3]
            oil_station.provider_id = row [4]
            # here we update the memory existing in or dict cache
        else:
            # if not in cache just create its instance and push to cache
            # you dont have to carry out sql to push to cache sice its already in the database
            oil_station = cls(row[1], row[2] , row[3], row[4])
            oil_station.id = row[0]
            cls.all[oil_station.id] = oil_station
        
    
    #carrying out a simple get all data query
    def get_all (cls):
        '''GET ALL DATA FROM THE TABLE '''
        sql = '''
        SELECT * FROM oil_stations;
        '''
        oil_stations = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in oil_stations] # this retruns everything and ensure also that the cache is updated rememebr the table is the source of truth
    
    




        
        