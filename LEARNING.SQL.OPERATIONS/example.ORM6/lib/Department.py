from __init__ import CURSOR , CONN

class Department:
    all = {}
    # this creates an instance of the class
    def __init__(self, name , location , id=None):
        self.id = id
        self.name = name
        self.location = location
    
    def __repr__(self):
        return (f'<department_id : {self.id} , name : {self.name} , location :{self.location} >')
    
    #this methods creates the departments table with the required collumns
    @classmethod
    def create_table(cls):
        '''this creates a new table with the required columns'''
        sql ='''
                CREATE TABLE departments(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                location TEXT NOT NULL
                )
            '''
        CURSOR.execute(sql) # this runs the sql command
        CONN.commit()# this ensures that the changes made are commited to the 

    #we then need a method to commit the instances to the table 
    def save(self):
        '''this method persists already made instances to the table'''
        sql = '''
        INSERT INTO departments (name , location) VALUES (?,?)
        '''
        CURSOR.execute(sql,(self.name , self.location))
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self # this saves the instance into our cache memory
        CONN.commit()
    
    @classmethod
    def create_save(cls, name , location):
        '''this immediately creates an instance and saves it to the table '''
        instance = cls(name , location )
        instance.save() # we use save the instance method to commit it to the database 

    @classmethod
    def drop_table(cls):
        '''deletes the entire departments table with included data'''
        sql = '''
        DROP TABLE IF EXISTS departments
        '''
        CURSOR.execute(sql)
        CONN.commit()
    
    def update_data(self):
        '''this updates the row according to the current instance's name and locaation(attributes)'''
        sql = '''
            UPDATE departments
            SET name = ?, location = ?
            WHERE id = ?
            '''
        CURSOR.execute(sql, (self.name, self.location, self.id))
        type(self).all[self.id] = self # this is to save it to the cache
        CONN.commit()
    
    def alter_data(self):
        pass

    @classmethod
    def instance_from_db(cls , row):
        instance = cls.all.get(row[0])
        if instance:
            instance.name = row[1]
            instance.location = row[2]
        else:
            # if the row is not in the class cache we need to create its instance and save it to the cach
            instance = Department(row[1] ,row[2])
            instance.id = row[0]
            Department.all[row[0]] = instance
        return instance
    
    @classmethod
    def get_all (cls):
        '''RETURNS ALL RECORDS FROM THE DB'''
        sql = '''
        SELECT * FROM departments
        '''
        rows = CURSOR.execute(sql).fetchall() # this returns all the rows fetched
        return [cls.instance_from_db(row) for row in rows]
