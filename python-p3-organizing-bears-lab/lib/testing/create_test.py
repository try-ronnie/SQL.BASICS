#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect(":memory:")

cursor = connection.cursor()

sql_file = open("lib/create.sql")
sql_as_string = sql_file.read()
cursor.executescript(sql_as_string)

class TestCreate:
    '''Statement in create.sql'''

    def test_creates_bears_with_name_column(self):
        '''creates a table "bears" with a column "name".'''
        assert(cursor.execute("SELECT name FROM bears;"))

    def test_creates_bears_with_age_column(self):
        '''creates a table "bears" with a column "age".'''
        assert(cursor.execute("SELECT age FROM bears;"))

    def test_creates_bears_with_sex_column(self):
        '''creates a table "bears" with a column "sex".'''
        assert(cursor.execute("SELECT sex FROM bears;"))

    def test_creates_bears_with_color_column(self):
        '''creates a table "bears" with a column "color".'''
        assert(cursor.execute("SELECT color FROM bears;"))

    def test_creates_bears_with_temperament_column(self):
        '''creates a table "bears" with a column "temperament".'''
        assert(cursor.execute("SELECT temperament FROM bears;"))

    def test_creates_bears_with_alive_column(self):
        '''creates a table "bears" with a column "alive".'''
        assert(cursor.execute("SELECT alive FROM bears;"))

    def test_creates_bears_with_id_pk(self):
        '''creates a table "bears" with a primary key "id".'''
        columns = [column for column in cursor.execute("PRAGMA table_info(bears);")]
        assert(columns[0][1] == "id")
