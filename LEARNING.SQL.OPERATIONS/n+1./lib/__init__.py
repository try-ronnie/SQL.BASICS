# import sqlite 
# initialize database connection with sqlite3 
# using CURSOR to execute sql commnads to the data base 

import sqlite3

CONN = sqlite3.connect('groceries.db')
CURSOR = CONN.cursor()# returns cursor object that handles our sql
CURSOR.execute("PRAGMA foreign_keys = ON;")
