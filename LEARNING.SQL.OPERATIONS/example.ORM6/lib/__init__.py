import sqlite3

CONN = sqlite3.connect('Institution.db')#this initializes the database connection
CURSOR = CONN.cursor()
CURSOR.execute("PRAGMA foreign_keys = ON;")