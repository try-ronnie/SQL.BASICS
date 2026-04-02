from provider import Provider
import ipdb
from __init__ import CURSOR , CONN

def fill_in_providers():
    # Provider.drop_table() this ensures that the previous data table is deleted and we work on a new table
    Provider.create_save('KENOL' , 6000 , 'SUDAN')


fill_in_providers()
ipdb.set_trace()
    
