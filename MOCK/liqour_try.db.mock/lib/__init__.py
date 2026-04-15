import sqlite3


CONN = sqlite3.connect('liqour_store.db') # initiliaze the connection to the database 
CURSOR = CONN.cursor() 
CURSOR.execute("PRAGMA foreign_keys = ON ;") # TURNS ON THE FOREGIN KEYS ...... NOT TO SURE ABOYT IT THO