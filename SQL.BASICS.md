# SQL Basics Guide

> **Prerequisites:** Prior coding knowledge is recommended

---

## Table of Contents
- [Lesson 1: Basic SQL Commands](#lesson-1-basic-sql-commands)
- [Lesson 2: Writing SQL in a Text Editor](#lesson-2-writing-sql-in-a-text-editor)
- [Lesson 3: Data Types in SQL](#lesson-3-data-types-in-sql)
- [Lesson 4: CRUD Operations](#lesson-4-crud-operations)
- [Lesson 5: String Functions & Data Cleaning](#lesson-5-string-functions--data-cleaning)

---

## Lesson 1: Basic SQL Commands

SQL is a language used to maintain relational databases.

### Creating a Database

To start working with SQLite:

```bash
sqlite3 pet_database.db
```

This creates a new database file (or opens an existing one).

### Creating a Table

When creating tables, you must define the structure including column names and data types:

```sql
CREATE TABLE cats (
  id INTEGER PRIMARY KEY,
  name TEXT,
  age INTEGER
);
```

**Key Points:**
- `CREATE TABLE` command creates a new table
- Column names are followed by their data type (TEXT, INTEGER, etc.)
- Every table should have an `id INTEGER PRIMARY KEY` column
- Primary keys are unique and auto-incrementing (start at 1)
- SQL commands are case-insensitive, but UPPERCASE for keywords is convention

### Altering a Table

Add a new column to an existing table:

```sql
ALTER TABLE cats ADD COLUMN breed TEXT;
```

Check your table structure:

```bash
.schema
```

**Note:** Altering or deleting columns in SQLite3 can be tricky and requires workarounds.

### Dropping a Table

Delete a table completely:

```sql
DROP TABLE cats;
```

Exit SQLite:

```bash
.quit
```

---

## Lesson 2: Writing SQL in a Text Editor

Instead of typing commands directly in the terminal, you can write SQL in `.sql` files and execute them.

### Workflow

1. **Create a file** with `.sql` extension (e.g., `add_column.sql`)

2. **Write your SQL command:**
   ```sql
   ALTER TABLE animals ADD COLUMN price INTEGER;
   ```

3. **Execute the file** against your database:
   ```bash
   sqlite3 animals_database.db < add_column.sql
   ```

This approach helps you:
- Keep track of your SQL code
- Reuse commands easily
- Maintain version control

---

## Lesson 3: Data Types in SQL

### Why Data Types Matter

Typing allows databases to:
- Store data efficiently
- Perform operations predictably (e.g., SUM, sorting)
- Validate and restrict data
- Prevent messy, inconsistent data

**Example Problem:**

| name     | breed              | age |
|----------|-------------------|-----|
| Maru     | Scottish Fold     | 3   |
| Hannah   | Tabby             | two |
| Lil' Bub | American Shorthair| 5.5 |

Without proper typing, operations like `SUM(age)` become unpredictable.

### SQLite Data Types

SQLite has 5 basic data type categories:

#### 1. **NULL**
Represents "no value" (like `null` in JavaScript or `None` in Python)

#### 2. **TEXT**
Any alphanumeric characters as plain text
- Names, email addresses, descriptions
- Example: `'Maru'`, `'Scottish Fold'`

#### 3. **INTEGER**
Whole numbers without decimals
- Use for: IDs, ages, counts, quantities
- Allows mathematical operations and numeric sorting
- Example: `3`, `42`, `1000`

#### 4. **REAL**
Decimal numbers (floating point)
- SQLite stores up to 15 characters
- Example: `1.3`, `2.25`, `1234.5678912345`
- Called "double precision" in other databases

#### 5. **BLOB**
Binary Large Object - stores binary data
- Not commonly used in basic operations
- Example: images, files

### Bonus: Type Compatibility

SQLite accepts common datatypes from other databases (MySQL, PostgreSQL):
- `INT` → stored as `INTEGER`
- `BOOLEAN` → stored as `INTEGER` (0 = false, 1 = true)
- `VARCHAR` → stored as `TEXT`

For more details, see the [SQLite documentation](http://www.sqlite.org/datatype3.html).

---

## Lesson 4: CRUD Operations

**CRUD** = Create, Read, Update, Delete

> 🔗 [GitHub Repository with Examples](https://github.com/try-ronnie/python-p3-sql-crud)

> ⚠️ **Remember:** All SQL commands must end with a semicolon (`;`)

---

### 1. CREATE - INSERT INTO

Add new data to a table:

```sql
INSERT INTO cats (name, age, breed) VALUES ('Maru', 3, 'Scottish Fold');
```

**Syntax:**
```sql
INSERT INTO [table_name] (column1, column2, ...) VALUES (value1, value2, ...);
```

**Key Points:**
- You don't need to specify the `id` column - it auto-increments
- Column names go in the first parentheses
- Values go in the second parentheses after `VALUES`
- This works in both terminal and `.sql` files

---

### 2. READ - SELECT FROM

Retrieve data from a table.

#### Basic Syntax

```sql
SELECT [column_names] FROM [table_name];
```

#### Select Specific Columns

```sql
SELECT name, age FROM cats;
```

#### Select All Columns (Wildcard)

```sql
SELECT * FROM cats;
```

The `*` wildcard means "all columns".

---

### Using DISTINCT

Remove duplicate rows from results:

```sql
SELECT DISTINCT name FROM cats;
```

#### Example:

**Without DISTINCT:**
```sql
SELECT name FROM cats;
```
Result:
```
LUNA
TEMBO
LUNA
GOMA
```

**With DISTINCT:**
```sql
SELECT DISTINCT name FROM cats;
```
Result:
```
LUNA
TEMBO
GOMA
```

#### DISTINCT with Multiple Columns

```sql
SELECT DISTINCT name, age FROM cats;
```

Result:
```
LUNA  - 5
TEMBO - 3
GOMA  - 12
LUNA  - 6
```

Notice: Both "LUNA" entries remain because they have different ages.

**🎯 Key Rule:**

DISTINCT removes rows where **ALL** selected column values are exactly the same.

It does NOT:
- Identify "original" rows
- Compare IDs unless you select them
- Know which record came first (unless you use `ORDER BY`)

**🧩 Mental Model:**

Think of DISTINCT as putting results in a basket and saying: "If I already saw this exact combination before, don't show it again."

---

### Using WHERE Clause

Filter results based on conditions:

```sql
SELECT * FROM [table_name] WHERE [column_name] = [value];
```

#### Examples:

```sql
-- Find a specific cat
SELECT * FROM cats WHERE name = 'Maru';

-- Find young cats
SELECT * FROM cats WHERE age < 2;

-- Find cats of a specific breed
SELECT * FROM cats WHERE breed = 'Scottish Fold';
```

**Comparison Operators:**
- `=` equal to
- `<` less than
- `>` greater than
- `<=` less than or equal to
- `>=` greater than or equal to
- `!=` or `<>` not equal to

> 💡 **Remember:** What follows `SELECT` is the column(s) to retrieve. The `WHERE` clause filters which rows to return.

---

### 3. UPDATE

Modify existing data in a table:

```sql
UPDATE [table_name] SET [column_name] = [new_value] WHERE [column_name] = [value];
```

#### Example:

```sql
UPDATE school SET name = 'John' WHERE name = 'KAMOTHO';
```

**Three Steps:**
1. Specify which table: `UPDATE school`
2. Set the new value: `SET name = 'John'`
3. Identify which row(s): `WHERE name = 'KAMOTHO'`

> ⚠️ **Warning:** Always use a `WHERE` clause! Without it, ALL rows will be updated.

---

### 4. DELETE

Remove rows from a table:

```sql
DELETE FROM [table_name] WHERE [column_name] = [value];
```

#### Example:

```sql
DELETE FROM school WHERE name = 'dj khalid';
```

> ⚠️ **Warning:** Always use a `WHERE` clause! Without it, ALL rows will be deleted.

---

## Lesson 5: String Functions & Data Cleaning

### SQLite Output Formatting

Format your query results in the terminal:

```bash
.headers on       # Show column names
.mode column      # Enable column mode
.width auto       # Auto-adjust column width
# or
.width 10, 20     # Custom column widths
```

---

### Common String Functions

#### 1. TRIM / LTRIM / RTRIM

Remove whitespace from strings:

```sql
TRIM(column)        -- removes spaces from both ends
LTRIM(column)       -- removes spaces from the left
RTRIM(column)       -- removes spaces from the right
```

**Example:**
```sql
SELECT TRIM(name) FROM school;
DELETE FROM school WHERE TRIM(name) = 'dj khalid';
```

**💡 Tip:** Check for hidden spaces:
```sql
SELECT '"' || name || '"' FROM school;
```
This wraps names in quotes so you can see extra spaces.

---

#### 2. UPPER / LOWER

Convert strings to uppercase or lowercase:

```sql
SELECT * FROM school WHERE UPPER(name) = 'DJ KHALID';
SELECT LOWER(name) FROM school;
```

Useful for case-insensitive comparisons.

---

#### 3. LENGTH

Count characters in a string:

```sql
SELECT name, LENGTH(name) FROM school;
```

Helpful for finding trailing spaces or validating data.

---

#### 4. SUBSTR

Extract part of a string:

```sql
SUBSTR(column, start, length)
```

**Example:**
```sql
SELECT SUBSTR(name, 1, 5) FROM school;
-- Returns first 5 characters
```

---

#### 5. REPLACE

Replace all occurrences of a substring:

```sql
SELECT REPLACE(name, ' ', '') FROM school;
-- Removes all spaces from names
```

---

#### 6. LIKE / GLOB

Pattern matching:

```sql
SELECT * FROM school WHERE name LIKE 'dj khalid%';
-- % = any characters after "dj khalid"
```

**Wildcards:**
- `%` - matches any sequence of characters
- `_` - matches any single character

**Examples:**
```sql
-- Names starting with 'A'
SELECT * FROM cats WHERE name LIKE 'A%';

-- Names ending with 'y'
SELECT * FROM cats WHERE name LIKE '%y';

-- Names with 'ar' anywhere
SELECT * FROM cats WHERE name LIKE '%ar%';
```

---

### Robust Data Cleaning Pattern

Combine functions for bulletproof queries:

```sql
DELETE FROM school
WHERE UPPER(TRIM(name)) = UPPER('dj khalid');
```

This pattern:
- Removes leading/trailing spaces with `TRIM()`
- Ignores case differences with `UPPER()`
- Handles inconsistent user input

**Use this approach when:**
- User input might have extra spaces
- Case sensitivity could cause issues
- Data quality is inconsistent

---

## Quick Reference

### Essential Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `CREATE TABLE` | Create new table | `CREATE TABLE cats (id INTEGER PRIMARY KEY, name TEXT);` |
| `ALTER TABLE` | Modify table structure | `ALTER TABLE cats ADD COLUMN breed TEXT;` |
| `DROP TABLE` | Delete table | `DROP TABLE cats;` |
| `INSERT INTO` | Add new data | `INSERT INTO cats (name, age) VALUES ('Maru', 3);` |
| `SELECT` | Retrieve data | `SELECT * FROM cats;` |
| `UPDATE` | Modify existing data | `UPDATE cats SET age = 4 WHERE name = 'Maru';` |
| `DELETE` | Remove data | `DELETE FROM cats WHERE age > 10;` |

### Data Types

| Type | Description | Example |
|------|-------------|---------|
| `INTEGER` | Whole numbers | `42`, `1000` |
| `TEXT` | Strings | `'Maru'`, `'Scottish Fold'` |
| `REAL` | Decimals | `3.14`, `2.5` |
| `NULL` | No value | `NULL` |
| `BLOB` | Binary data | (rarely used) |

### String Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `TRIM()` | Remove spaces | `TRIM(name)` |
| `UPPER()` | Convert to uppercase | `UPPER(name)` |
| `LOWER()` | Convert to lowercase | `LOWER(name)` |
| `LENGTH()` | Count characters | `LENGTH(name)` |
| `SUBSTR()` | Extract substring | `SUBSTR(name, 1, 5)` |
| `REPLACE()` | Replace text | `REPLACE(name, ' ', '')` |

---

## Best Practices

1. ✅ Always use `INTEGER PRIMARY KEY` for id columns
2. ✅ End all SQL commands with semicolons (`;`)
3. ✅ Use `WHERE` clauses with `UPDATE` and `DELETE` to avoid affecting all rows
4. ✅ Use `DISTINCT` to remove duplicate results
5. ✅ Use `TRIM()` and `UPPER()`/`LOWER()` for robust string comparisons
6. ✅ Write SQL in `.sql` files for reusability
7. ✅ Use meaningful table and column names
8. ✅ Choose appropriate data types for your data

---

## Additional Resources

- [SQLite Official Documentation](https://www.sqlite.org/docs.html)
- [SQLite Data Types](http://www.sqlite.org/datatype3.html)
- [SQL CRUD Operations GitHub Repo](https://github.com/try-ronnie/python-p3-sql-crud)


## LESSON 6 : QUERY MANIPULATORS

1. order by
The first query modifier we'll explore is ORDER BY. This modifier allows us to order the table rows returned by a certain SELECT statement. Here's a boilerplate SELECT statement that uses ORDER BY:
```SELECT column_name FROM table_name ORDER BY column_name ASC|DESC;```

ORDER BY justs lets us rearrange thedata according to ascending or descending order .....
```SELECT * FROM cats ORDER BY age DESC;```
This should return

id          name        age         breed       owner_id
----------  ----------  ----------  ----------  ----------
4           Moe         10          Tabby
3           Lil\' Bub   5           American S
1           Maru        3           Scottish F  1
5           Patches     2           Calico
2           Hana        1           Tabby       1

2. limits:
What if we want the oldest cat? If we want to select extremes from a database table — for example, the employee with the highest paycheck or the patient with the most recent appointment — we can use ORDER BY in conjunction with LIMIT.

LIMIT is used to determine the number of records you want to return from a dataset. For example:

```SELECT * FROM school ORDER BY age LIMIT 1;```
This part of the statement: SELECT * FROM cats ORDER BY age DESC returns all of the cats in order from oldest to youngest. Setting a LIMIT of 1 returns just the first, i.e. oldest, cat on the list.

this means by the order of age .... limit is one record so it well retain the methods
```SELECT * FROM cats ORDER BY age DESC LIMIT 2;```

3. betwee
As we've already established, being able to sort and select specific data sets is important. Continuing on with our example, let's say we urgently need to select all of the cats whose age is between 1 and 3. To create such a query, we can use BETWEEN. Here's a boilerplate SELECT statement using BETWEEN:
```SELECT column_name(s) FROM table_name WHERE column_name BETWEEN value1 AND value2;```

example used i our school.database.db
```sqlite> 
sqlite> SELECT * FROM school WHERE age BETWEEN 10 AND 20;
|dj khalid |13|east|45000
| KAMOTHO |12|EAST|75000
| kinuthia |12|EAST |23000
|scott|12|EAST|12000
|KAMAU|16|WEST|142000
```
4. NULL 
Let's say the administrator of our school.Database has found a new student. This student doesn't have a name yet, but should be added to our database right away. We can add data with missing values using the NULL keyword.

Let's insert our new student into the database. Our abandoned student has a stream, but no name or age as of yet:

INSERT INTO cats (name, age, breed) VALUES (NULL, NULL, "Tabby");

``` INSERT INTO cats (name, age, breed) VALUES (NULL, NULL, "Tabby");
```

this should return something of the sort

5. count


SQL aggregate functions are SQL statements that operate on groups of records in our database rather than individual records. For example, we can retrieve minimum and maximum values from a column, sum values in a column, get the average of a column's values, or count a number of records that meet certain conditions. You can learn more about these SQL aggregators [here](https://www.sqlclauses.com/sql+aggregate+functions) and  [here](https://zetcode.com/db/sqlite/select/)


```SELECT COUNT([column name]) FROM [table name] WHERE [column name] = [value]
```
```SELECT COUNT(owner_id) FROM cats WHERE owner_id = 1;```

5. Group by
Lastly, we'll talk about the handy aggregate function GROUP BY. Like its name suggests, it groups your results by a given column.

```SELECT breed, COUNT(breed) FROM cats GROUP BY breed;
```
This should return

breed               COUNT(breed)
------------------  ------------
American Shorthair  1
Calico              1
Scottish Fold       1
Tabby               3


Note on SELECT
We are now familiar with this syntax:

SELECT name FROM cats;
However, you may not know that this can be written like this as well:

SELECT cats.name FROM cats;
Both return:

name
----------
Maru
Hana
Lil\' Bub
Moe
Patches
SQLite allows us to explicitly state the tableName.columnName we want to select. This is particularly useful when we want data from two different tables.

Imagine we have another table called dogs with a column for the dog names:

CREATE TABLE dogs (
  id INTEGER PRIMARY KEY,
  name TEXT
);
INSERT INTO dogs (name) VALUES ("Clifford");
If we want to get the names of all the dogs and cats, we can no longer run a query with just the column name. SELECT name FROM cats,dogs; will return Error: ambiguous column name: name.

Instead, we must explicitly follow the tableName.columnName syntax.

SELECT cats.name, dogs.name FROM cats, dogs;
You may see this in the future. Don't let it trip you up.

Conclusion
SQL gives you a lot of tools for fine-grained control over how to view data from various database tables. When you start working with larger databases that have 5000 or 50,000 rows in a table instead of 5, having this level of control is crucial for accessing and analyzing data that's useful to your applications, and can help you improve your application's performance significantly by limiting the amount of data being returned.

 ####  exercise 1 : Organizing Bears Lab (CodeGrade)
 Learning Goals:
Use SQL to store data and retrieve it later on.
Use SQLite to build relational databases on your computer.
Perform CRUD operations on relational databases using SQL.


Lab Structure
This lab might seem a bit different than what you've seen before. Take a look at the file structure and read the comments to understand what each file is used for:

├── __init__.py        # designates "python-p3-organizing-bears-lab" as package
├── Pipfile
├── Pipfile.lock
├── README.md
├── lib
    ├── __init__.py    # designates "lib" as package
│   ├── create.sql     # where you CREATE your schema
│   ├── insert.sql     # where you INSERT your data
│   ├── seed.sql       # data for in-memory test database
│   ├── sql_queries.py # where you write your SELECT queries
└── testing            # all the tests
    ├── __init__.py    # designates "testing" as package
    ├── create_test.py # this tests your create.sql file
    ├── insert_test.py # this tests your insert.sql file
    ├── select_test.py # this tests the queries you write in sql_queries.py
    └── conftest.py    # configuration for pytest
This lab uses the sqlite3 module from Python's standard library to allow us to connect to a SQL database from Python. How cool is that!? We'll use this module more in the lessons to come.

A Note on Testing
Let's briefly go over what is happening in setup blocks that our tests will be using.

connection = sqlite3.connect(":memory:")

cursor = connection.cursor()

create_file = open("lib/create.sql")
create_as_string = create_file.read()
cursor.executescript(create_as_string)
Before each test, two important things happen.

First, a new in-memory database is created. Why do we do this instead of creating a database file? Let's say we run our tests and they add ten items to our database. If we did not use an in-memory store, those would be in there forever. This way, our database gets thrown out after every running of the tests. You can learn more about in-memory databases hereLinks to an external site..

Next, the test opens the .sql file, and runs the SQL code in that file in that in-memory database.

Part 1: CREATE TABLE
Get the tests in testing/create_test.py to pass by writing code in the lib/create.sql file. Your CREATE statement should look something like this:

CREATE TABLE bears (
  //columns here
);
Your columns should be the following types:

column	type
id	integer
name	text
age	integer
sex	text
color	text
temperament	text
alive	boolean
Read about SQLite3 DatatypesLinks to an external site. to determine what your insert values are going to be. Be sure to pay attention to how booleans are expressed in SQLite3.

Part 2: INSERT
Get the tests in testing/insert_test_.py to pass by writing code in the lib/insert.sql file. Input the following 8 bears (you can make up details about them, but make sex either 'M' or 'F'):

Mr. Chocolate
Rowdy
Tabitha
Sergeant Brown
Melissa
Grinch
Wendy
unnamed (refer back to how to create a record that doesn't have one value)
Part 3: SELECT
Get the tests in testing/select_test.py to pass. Note that for this section, the database will be seeded with external data from the lib/seed.sql file so don't expect it to reflect the data you added above.

Note: Since it's a Python file, write your queries as strings in the global scope in the lib/sql_queries.py file. For example, to pass the first test, your Python string should look like this:

select_all_female_bears_return_name_and_age = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    WHERE sex='F';
"""
You may be expected to use SQL statements that you're not particularly familiar with. Make sure you use the resources and Google to find the right statements.


