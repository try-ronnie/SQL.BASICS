import sqlite3

CONN = sqlite3.connect()#this initializes the database connection
CURSOR = CONN.cursor()
PRAGMA foreign_keys = ON ;