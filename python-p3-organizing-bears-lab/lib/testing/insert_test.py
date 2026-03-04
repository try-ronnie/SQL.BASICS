#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect(":memory:")

cursor = connection.cursor()

create_file = open("lib/create.sql")
create_as_string = create_file.read()
cursor.executescript(create_as_string)

insert_file = open("lib/insert.sql")
insert_as_string = insert_file.read()
cursor.executescript(insert_as_string)

class TestInsert:
    '''Statement in insert.sql'''

    def test_inserts_eight_bears_into_table(self):
        '''inserts 8 bears into bears table.'''
        result = cursor.execute("SELECT COUNT(*) FROM bears;")
        assert(result.fetchall()[0][0] == 8)

    def test_has_unnamed_bear(self):
        '''inserts one unnamed bear into bears table.'''
        result = cursor.execute("SELECT COUNT(*) FROM bears WHERE name IS NULL;")
        assert(result.fetchall()[0][0] == 1)
    