import ipdb
from __init__ import CURSOR , CONN
from item import Item
from category import Category

def debug_database ():
    
    Category.drop_table()
    Category.create_table()
    Item.drop_table()
    Item.create_table()

    Category.create_save('FRUITS')
    Category.create_save('DAIRY')
    Category.create_save('VEGETABLES')

    Item.create_save('APPLE',1)
    Item.create_save('MILK',2)
    Item.create_save('CABBAGE',3)
    Item.create_save('nduma' , 3)

debug_database()
ipdb.set_trace()



