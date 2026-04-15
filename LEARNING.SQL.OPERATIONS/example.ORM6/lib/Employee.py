from __init__. import CURSOR , CONN

class Employee:
    all = {} # cache

    #this creates an instance of the employee class
    def __init__(self, name , job_title , department_id , id = None):
        self.id = id 
        self.name = name
        self.job_title = job_title
        self.department_id = department_id

    @classmethod
    def save(self):
        '''PERSIST CURRENT INSTANCE TO THE DATABASE'''
        sql = '''
        INSERT INTO employees (name , job_title , department_id)
        VALUES (?,?,?)
        '''
        CURSOR.execute(sql, (self.name, self.job_title , self.department_id))
        self.id = CURSOR.lastrowid # give the instance an id 
        type(self).all[self.id] = self #update cache with the id as the key
        CONN.commit()
   
   
    
