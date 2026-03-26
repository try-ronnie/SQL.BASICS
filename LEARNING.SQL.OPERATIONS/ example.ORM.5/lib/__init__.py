#initializing the database connection using sqlite
import sqlite3

CONN = sqlite3.connect('oil_reolution') # this is a constructor since it creates an object that handles the connection to the database
CURSOR = CONN.cursor() 
#Creates a Cursor object from the connection. The cursor is used to execute SQL statements and fetch results from the database. The cursor is stored in the variable CURSOR


