from __init__ import CURSOR, CONN

class Department:
    @ classmethod
    def create_table(cls):
        """creating  a new table """
        sql = """
            CREATE TABLE IF NOT EXISTS departments(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL ,
            location TEXT);
            """
        CURSOR.execute(sql)
        CONN.commit()
    @classmethod
    def drop_table(cls):
        """drop a full table """
        sql = """
            DROP TABLE IF EXISTS departments;
            """
        CURSOR.execute(sql)
        CONN.commit()

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"
    def save (self):
        '''INSERT VALUE INTO THE TABLE ROW'''
        sql = '''
            INSERT INTO departments (name , location) VALUES (?,?)
            ;
            '''
        CURSOR.execute(sql , (self.name , self.location))
        CONN.commit()
        self.id = CURSOR.lastrowid
    @classmethod
    def create(cls , name , location):
        '''DIRECTLY ADDING CREATED OBJECTS TO THE TABLE '''
        department = cls(name, location)
        department.save()
        return department
    
# # # so when we want to create an instance and put it to the table directly we need a new method:
# #     in this case we use method create ()
# #         -save () is different in that :
#             1. we need to first create an instance of the department class
#             2. then inside the save code we use an insert sql query that persists the data into the table 
#       in the case we want to make this one step 

#     we use the create ():
#          1. we use the class to make the instances ... 
#         2, this is a class method since no value of an object is instatiadted yet ... so we use the cls() to refer to the --init-- to create the instance in the method
#         3. since we created the save that carries the sql query to pesists the object into the table we use it inside the create method code 
#         4. then we return the object ... we do this just to show what was created and persisted to the table



#  note that we use CURSOR to give the values to be putin to the table in such a manner to avoid SQL INJECTION