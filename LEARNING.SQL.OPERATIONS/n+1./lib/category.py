from __init__ import CONN , CURSOR

class Category:
    # create an instance of category
    def __init__(self,name,id = None):
        self.name = name 
    
    # create a table to map the instances to 
    @classmethod 
    def create_table (cls):
        '''CREATE CATEGORIES TABLE IN WHICH CATEGORY INSTANCES ARE PERSISTED'''
        sql = '''
            CREATE TABLE IF NOT EXISTS categories(
            id INTEGER PRIMARY KEY ,
            name TEXT NOT NULL 
            );
            '''
        CURSOR.execute(sql)
        CONN.commit()

    #create a method that persits instances to the table made
    def save (self):
        '''PERSITS AN INSTANCE OF THE CATEGORY CLASS TO THE TABLE'''
        sql = '''INSERT INTO categories (name) VALUES (?);'''
        
        CURSOR.execute(sql, (self.name,)) # bound parameter to ?, remember to leave a trailing comma so python can know its a tuple not a string to ierate over 
        self.id = CURSOR.lastrowid  # gives the id to the instance 
        CONN.commit()


    
    # create ametho that creates an instance and persists the instance to the table 
    @classmethod
    def create_save(cls , name):
        '''CREATE AND PERSIST THE CREATED VALUE TO THE DATABASE'''
        category = cls(name) # this creates an instance of category with the passed parameter during the function call ... since it is required and it operates on the class level
        category.save()
        CONN.commit()
    

    # create a method to drop the whole table 
    @classmethod
    def drop_table(cls):
        ''' DROP THE TABLE CATEGORY'''
        sql = '''
            DROP TABLE IF EXISTS categories ;
            '''
        CURSOR.execute(sql)
        CONN.commit()
    # we update anything that only exists in the table meaning it has to have an id 
    # in which we use the id to 
    def update_table(self):
        ''' UPDATE THE TABLE ROW'''
        sql = '''
            UPDATE TABLE categories ,
            SET name = (?),
            WHERE id = (?)
            '''
        CURSOR.execute(sql,(self.id , self.name))
        CONN.commit()