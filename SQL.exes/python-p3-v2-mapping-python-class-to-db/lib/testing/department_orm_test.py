from department import Department
from __init__ import CURSOR, CONN
import pytest


class TestDepartment:
    '''Class Department in department.py'''

    @pytest.fixture(autouse=True)
    def drop_tables(self):
        '''drop table prior to each test.'''
        CURSOR.execute("DROP TABLE IF EXISTS departments")

    def test_creates_table(self):
        '''contains method "create_table()" that creates table "departments" if it does not exist.'''

        Department.create_table()
        assert (CURSOR.execute("SELECT * FROM departments"))

    def test_drops_table(self):
        '''contains method "drop_table()" that drops table "departments" if it exists.'''

        sql = """
            CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

        Department.drop_table()

        sql_table_names = """
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='departments'
        """
        result = CURSOR.execute(sql_table_names).fetchone()
        assert (result is None)

    def test_saves_department(self):
        '''contains method "save()" that saves a Department instance to the db and assigns the instance an id.'''

        Department.create_table()
        department = Department("Payroll", "Building A, 5th Floor")
        department.save()

        sql = """
            SELECT * FROM departments
        """
        row = CURSOR.execute(sql).fetchone()
        assert ((row[0], row[1], row[2]) ==
                (department.id, department.name, department.location) ==
                (row[0], "Payroll", "Building A, 5th Floor"))

    def test_creates_department(self):
        '''contains method "create()" that creates a new row in the db using parameter data and returns a Department instance.'''

        Department.create_table()
        department = Department.create("Payroll", "Building A, 5th Floor")

        sql = """
            SELECT * FROM departments
        """
        row = CURSOR.execute(sql).fetchone()
        assert ((row[0], row[1], row[2]) ==
                (department.id, department.name, department.location) ==
                (row[0], "Payroll", "Building A, 5th Floor"))

    def test_updates_row(self):
        '''contains a method "update()" that updates an instance's corresponding db row to match its new attribute values.'''
        Department.create_table()

        department1 = Department.create(
            "Human Resources", "Building C, East Wing")
        id1 = department1.id
        department2 = Department.create("Marketing", "Building B, 3rd Floor")
        id2 = department2.id

        # Assign new values for name and location
        department2.name = "Sales and Marketing"
        department2.location = "Building B, 4th Floor"

        # Persist the updated name and location values
        department2.update()

        # assert department1 row was not updated, department1 object state not updated
        sql = """
            SELECT * FROM departments
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id1,)).fetchone()
        assert ((row[0], row[1], row[2])
                == (id1, "Human Resources", "Building C, East Wing")
                == (department1.id, department1.name, department1.location))

        # assert department2 row was updated, department2 object state is correct
        sql = """
            SELECT * FROM departments
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id2,)).fetchone()
        print(row)
        assert ((row[0], row[1], row[2])
                == (id2, "Sales and Marketing", "Building B, 4th Floor")
                == (department2.id, department2.name, department2.location))

    def test_deletes_record(self):
        '''contains a method "delete()" that deletes the instance's corresponding db row'''
        Department.create_table()

        department1 = Department.create(
            "Human Resources", "Building C, East Wing")
        id1 = department1.id
        department2 = Department.create("Marketing", "Building B, 3rd Floor")
        id2 = department2.id

        department2.delete()

        sql = """
            SELECT * FROM departments
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id1,)).fetchone()
        # assert department1 row not deleted
        assert (row)

        sql = """
            SELECT * FROM departments
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id2,)).fetchone()
        # assert department2 row is deleted
        assert (row is None)
