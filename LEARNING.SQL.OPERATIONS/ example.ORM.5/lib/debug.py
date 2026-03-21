import station 
from __init__ import CURSOR , CONN
from station import Station
import ipdb 

def reset_table_with_data ():
    Station.drop_table()
    Station.create_table()
    d2 = Station.create_save('Rubis' , 12000 , 'Nairobi')


reset_table_with_data()
ipdb.set_trace()

