import ipdb
from __init__ import CURSOR , CONN
from Department import Department

def department_data_debug():
    Department.drop_table() # drop any existing table to start with clean records
    Department.create_table()# create table
    Department.create_save('Security office' , '2nd floor')
    Department.create_save('Hospitatily office' , '1st floor')

department_data_debug()
ipdb.set_trace()