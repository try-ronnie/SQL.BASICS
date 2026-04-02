from __init__ import CURSOR , CONN

class Provider:
    #cache
    all = {}
    def __init__(self, name:str , capacity:int , country , id= None):
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


    @classmethod
    def create_save(cls, name ,capacity , country):
        '''CREATE AN INSTANCE AND SAVE IT DIRECTLY TO THE TABLE'''
        provider = cls(name , capacity , country)
        provider.save() # remember that our save function carries out the giving of the id and caching 
    #practically this function just creates an instance of the cls with values paassed into it which ... we use cls to create the instance ... since creation f instances happen at hte cls level
    
    
    
    
    #persist provider instances to the table and update dache memory instance id
    def save (self):
        ''' PESIST BOTH DB AND CACHE , DB AS SOUCE OF TUTH'''
        sql = '''
            INSERT INTO providers (name, capacicty , name) VAALUES (?,?,?);
            '''
        CURSOR.execute(sql ,(self.name , self.capacity , self.country))
        self.id = CURSOR.lastrowid # give the id so that you can piush with the correct id to cache
        type(self).all[self.id] = self # store persisted value to cache 
    
    #drops the whole data in the table and the table its self
    @classmethod
    def drop_table (cls):
        '''DOP THE WHOLE '''
        sql = '''   
            DROP TABLE IF EXISTS providers;
            '''
        CURSOR.execute(sql)
        CONN.commit()

    #updating data in a table row  ... we use th update ... remember its a row  ... hence we use self
    def update_full_stats(self):
        '''UPDATE TABLE according to the current instance'''
        sql = ''' 
        UPDATE providers,
        SET name = ? , capacity = ? , country = ?
        WHERE id = ?
        '''
        CURSOR.execute(sql , (self.name ,self.capacity ,self.country, self.id))
        type(self).all[self.id] = self # remember to keep the cache updated to the latest table values 
        CONN.commit()


    #cache reloader
    # this function recieves a single row fetched from the table as a list containing the data
    # we then need to update the cache accordingly 

    @classmethod
    def instance_from_db(cls , row):
        '''recieves row from db ... uses this to update the memory in cache for faster retrun queries'''
        provider = cls.all.get[row[0]] # checks if the row exists ... we use the id as key 
        if provider: # if the value returns is in the dict / cache
            provider.name = row[1]
            provider.capactiy = row[2]
            provider.country = row[3] 
            # ensure that the values in the dict match the ones in the db.... the db is the source of truth
        else: # if None is returned ... meaning the value is not a dit ... this is a falsy so it runs else
            # if the value is not there but is located in the db we should create an instance and save it to the dict as cachd 
            provider = cls(row[1], row[2] , row[3]) # use the values from row (the single list /row from the db) ... remember what gets values from where ... 
            provider.id = row[0]
            cls.all[row[0]] = provider
        return provider
    

    # most of these from here are just COMPLE SELECT METHODS 

    @classmethod
    def get_all(cls):
        ''''''
        sql = '''
            SELECT * FROM providers;
            '''
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows] # when retrieving remmber to update eache row in our cache

    @classmethod
    def find_by_id(cls , id):
        '''find privider from dbt by id'''
        sql = '''
        SELECT * FROM providers,
        WHERE id = ?;
        '''
        id_row = CURSOR.execute(sql , (id,)).fetchone()
        return cls.instance_from_db(id_row) if id_row else None 
    @classmethod
    def find_by_name(cls,name) :
        '''FIND A VALUE BY NAME FROM THE DATABAE'''
        sql = ''' 
            SELECT * FROM providers,
            WHERE name = ?;
            '''
        row_by_name = CURSOR.execute(sql , (name,)).fetchone()#this retruns a list of the tuple choosen from our table that fit the constraints 
        return cls.instance_from_db(row_by_name) if row_by_name else None # run the method to cache the value and ensure that cache memory is upto date
    @classmethod
    def  all_high_capacity (cls):
        '''RETURN ALL HIGH CAPACITY'''
        sql = '''
            SE;ECT * FROM providers ,
            WHERE capacity > 50000 ;
            '''
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]  if rows else None
    
    @classmethod
    def all_mid_capacity(cls):
        ''''''
        sql = '''
            SELECT * FROM providers,
            WHERE capacity > 30000 AND capacty < 5000;
            '''
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db]
    # in gaining info from the db also remember to catch or during updating ... always rmember to catch where data is involved 

