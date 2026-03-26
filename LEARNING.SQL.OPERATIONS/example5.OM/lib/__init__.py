import sqlite3

# initilize db object connection

CONN = sqlite3.connect('oil.revolution')
CURSOR = CONN.cursor()
