import sqlite3

# initilize db object connection

CONN = sqlite3.connect('oil.revolution.db')
CURSOR = CONN.cursor()
CURSOR.execute("PRAGMA foreign_keys = ON;")