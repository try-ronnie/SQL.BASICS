#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb
def reset_table = 
Department.drop_table()
Department.create_table()
d1 = Department.create('finance' , 'Building 42 , A block')
print(d1)
ipdb.set_trace()

# if you want to check i you you ipdb session fo ceating the table or any sql query executuion that returns none

# CURSOR.execute("PRAGMA table_info(departments)").fetchall()