#!/usr/bin/env python3

import sqlite3

from sql_queries import (
    select_all_female_bears_return_name_and_age,
    select_all_bears_names_and_orders_in_alphabetical_order,
    select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest,
    select_oldest_bear_and_returns_name_and_age,
    select_youngest_bear_and_returns_name_and_age,
)

connection = sqlite3.connect(":memory:")

cursor = connection.cursor()

create_file = open("lib/create.sql")
create_as_string = create_file.read()
cursor.executescript(create_as_string)

insert_file = open("lib/seed.sql")
insert_as_string = insert_file.read()
cursor.executescript(insert_as_string)

class TestSelectAllFemaleBearsReturnNameAndAge:
    '''select_all_female_bears_return_name_and_age in sql_queries.py'''

    def test_selects_females_and_returns_name_and_age(self):
        '''selects all of the female bears and returns their name and age.'''
        result = cursor.execute(select_all_female_bears_return_name_and_age)
        assert(result.fetchall() == [
            ("Tabitha", 6),
            ("Melissa", 13),
            ("Wendy", 6)
        ])

class TestSelectAllBearsNamesAndOrdersInAlphabeticalOrder:
    '''select_all_bears_names_and_orders_in_alphabetical_order in sql_queries.py'''

    def test_selects_all_bears_names_and_orders_alphabetically(self):
        '''selects all of the bears names and orders them in alphabetical order.'''
        result = cursor.execute(select_all_bears_names_and_orders_in_alphabetical_order)
        assert(result.fetchall() == [
            (None,),
            ("Grinch",),
            ("Melissa",),
            ("Mr. Chocolate",),
            ("Rowdy",),
            ("Sergeant Brown",),
            ("Tabitha",),
            ("Wendy",)
        ])

class TestSelectAllBearsNamesAndAgesThatAreAliveAndOrderYoungestToOldest:
    '''select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest in sql_queries.py'''

    def test_selects_all_bears_names_and_ages_that_are_alive_and_orders_youngest_to_oldest(self):
        '''selects all of the bears names and ages that are alive and order them from youngest to oldest.'''
        result = cursor.execute(select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest)
        assert(result.fetchall() == [
            ("Grinch", 2),
            ("Tabitha", 6),
            ("Wendy", 6),
            ("Rowdy", 10),
            ("Melissa", 13),
        ])

class TestSelectOldestBearAndReturnNameAndAge:
    '''select_oldest_bear_and_returns_name_and_age in sql_queries.py'''

    def test_selects_oldest_bear_and_returns_name_and_age(self):
        '''selects the oldest bear and returns its name and age.'''
        result = cursor.execute(select_oldest_bear_and_returns_name_and_age)
        assert(result.fetchall() == [
            ("Mr. Chocolate", 20,),
        ])

class TestSelectYoungestBearAndReturnNameAndAge:
    '''select_youngest_bear_and_returns_name_and_age in sql_queries.py'''

    def test_selects_youngest_bear_and_returns_name_and_age(self):
        '''selects the youngest bear and returns its name and age.'''
        result = cursor.execute(select_youngest_bear_and_returns_name_and_age)
        assert(result.fetchall() == [
            ("Grinch", 2,),
        ])