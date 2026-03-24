#initializing the database connection using sqlite
import sqlite3

CONN = sqlite3.connect('oil_reolution')
CURSOR = CONN.cursor()

