from __init__ import CONN , CURSOR 


class Item:
    # creates an instance of the item class
    def __init__(self,name:str,category_id:int,id = None):
        self.name = name 
        self.category_id = category_id
    

    #create items table in where we shall persist items to the table 
    @classmethod
    def create_table (cls):
        '''CREATE ITEMS TABLE'''
        sql = '''
            CREATE TABLE IF NOT EXISTS items(
            id INTEGER PRIMARY KEY ,
            name TEXT NOT NULL,
            category_id INTEGER CHECK(category_id in (1,2,3,4)), 
            FOREIGN KEY (category_id) REFERENCES categories(id)
            );
            '''
        CURSOR.execute(sql)
        CONN.commit()
    # save instance to the table
    # also gives the instances id's using the CURSOR command 
    def save(self):
        '''PERSIST AN ALREADY MADE INSTANCE OF ITEMS'''
        sql = '''
            INSERT INTO items (name,category_id) VALUES (?,?);
            '''
        
        CURSOR.execute(sql, (self.name , self.category_id))

        self.id = CURSOR.lastrowid
        CONN.commit() 
    
    #drop the whole table
    @classmethod
    def drop_table(cls):
        '''DROP THE ITEMS TABLE'''
    sql ='''
    DROP TABLE IF EXISTS items;
    '''
    CURSOR.execute(sql)
    CONN.commit()

    # method that creates an instanance and persists the data to the table directly
    @classmethod
    def create_save(cls,name , category_id):
        '''TAKES THE CLASS , CREATES INSTANCE AND PERSITS TO THE TABLE IMMEDIATELY'''
        item_instance = cls(name , category_id)
        item_instance.save()
        CONN.commit()
        
        
    
    
    #remember to work on values already in the table mean we work with self ...
    #