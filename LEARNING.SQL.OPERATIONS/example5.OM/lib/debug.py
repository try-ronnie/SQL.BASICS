from provider import Provider
from oil_station import Oil_station
import ipdb
from __init__ import CURSOR , CONN

def fill_in_providers():
    Provider.drop_table() # this ensures that the previous data table is deleted and we work on a new table
    Provider.create_table() # 
    Provider.create_save('RASHID.BMO' , 6000 , 'SUDAN')
    Provider.create_save('ALHUSSAIM.ORC', 150000 , 'SOMALIA')
    Provider.create_save('ALFAKIR.JRQ', 100000 , 'TANZANIA')
    Provider.create_save('DUBAJ.IPL' , 70000 , 'UGANDA')
    Oil_station.create_save('RUbis', 300000 , 'KINGONGO' , 2)
    Oil_station.create_save('OLA', 450000 , 'KIGANJO' , 1)
    Oil_station.create_save('KENOL', 560000 , 'MWIEGA' , 3)
    Oil_station.create_save('NATIONAL OIL', 300000 , 'CHAKA' , 4)
    Oil_station.create_save('', 300000 , 'KINGONGO' , 2)





fill_in_providers()
ipdb.set_trace()
    
