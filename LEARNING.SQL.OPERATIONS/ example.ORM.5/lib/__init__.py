import sqlite3

CONN = sqlite3.connect('station.db')
CURSOR = CONN.cursor()

# to allow the initializing or connecting of a class with the database sqlite3 gives use methods to carry it out

#sqlite3 .connect .... - this is the function that ensures connection to the databas
#CURSOR => this is th method that allows execution of sql queries in our current connection to the database 
