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

## 🗄️ Lesson 1: Basic SQL Commands

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

**Key Points:** 🚀
- `CREATE TABLE` command creates a new table
- Column names followed by data types (e.g., `TEXT`, `INTEGER`)
- Always include `id INTEGER PRIMARY KEY` (auto-increments from 1)
- Keywords in UPPERCASE by convention (case-insensitive)
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

**💡 SQLite Tip:** Altering/dropping columns is limited; use `CREATE TABLE AS SELECT` for complex changes.

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

## ✏️ Lesson 2: Writing SQL in a Text Editor

Instead of typing commands directly in the terminal, you can write SQL in `.sql` files and execute them.

### 📝 Workflow

1. **Create** `.sql` file (e.g., `add_column.sql`)
2. **Write** SQL:
   ```sql
   ALTER TABLE animals ADD COLUMN price INTEGER;
   ```
3. **Run**: `sqlite3 animals_database.db < add_column.sql`

**Benefits:** Version control, reusability, easier debugging. 🛠️

---

## 🔤 Lesson 3: Data Types in SQL

### Why Data Types Matter

Typing allows databases to:
- Store data efficiently
- Perform operations predictably (e.g., SUM, sorting)
- Validate and restrict data
- Prevent messy, inconsistent data

**Example Problem:**

| name       | breed              | age |
|------------|-------------------|-----|
| Maru       | Scottish Fold     | 3   |
| Hannah     | Tabby             | two |
| Lil' Bub   | American Shorthair| 5.5 |

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

**More:** [SQLite Datatypes](https://www.sqlite.org/datatype3.html)

---

## ➕➡️📖✏️🗑️ Lesson 4: CRUD Operations

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
UPDATE school SET name = 'John' WHERE UPPER(TRIM(name)) = 'KAMOTHO';
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
DELETE FROM school WHERE UPPER(TRIM(name)) = 'DJ KHALID';
```

> ⚠️ **Warning:** Always use a `WHERE` clause! Without it, ALL rows will be deleted.

---

## ✂️ Lesson 5: String Functions & Data Cleaning

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
DELETE FROM school WHERE TRIM(name) = 'DJ KHALID';
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
SELECT * FROM school WHERE UPPER(TRIM(name)) = 'DJ KHALID';
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
SELECT * FROM school WHERE name LIKE 'DJ KHALID%';
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
WHERE UPPER(TRIM(name)) = 'DJ KHALID';
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
| `AVG(column)` | Average |
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

---

## Lesson 7: SQL JOINS

So far you've been working with one table at a time. But real databases are made of **multiple related tables** — and that's where JOINs come in.

A JOIN lets you pull data from two or more tables in a single query, by linking them through a shared column — usually a foreign key.

Before we dive in, let's look at the tables we'll be using throughout this lesson. These come straight from your `example 4` folder.

### The Tables We're Working With

**students table** — created in `CREATE students.table.sql`:

```sql
CREATE TABLE students(
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER NOT NULL CHECK (age > 10 AND age < 18),
  gender TEXT NOT NULL CHECK (gender IN ('M', 'F'))
);
```

**teacher table** — created in `CREATE teacher.table.sql`:

```sql
CREATE TABLE teacher(
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER NOT NULL CHECK (age > 25 AND age < 65),
  gender TEXT NOT NULL CHECK (gender IN ('M', 'F'))
);
```

**students_teachers (join table)** — created in `CREATE join_table.sql`:

```sql
CREATE TABLE students_teachers(
  student_id INTEGER NOT NULL,
  teacher_id INTEGER NOT NULL
);
```

This middle table is called a **join table** (also known as a bridge table or associative table). It doesn't hold names or ages — it just holds relationships. It says: "student with id X is linked to teacher with id Y."

**Data inserted** — from `INSERT students_values.sql`, `INSERT teacher_values.sql`, `INSERT join_table_data.sql`:

```sql
-- students
INSERT INTO students (name, age, gender) VALUES
  ('bob', 15, 'M'), ('dogo', 15, 'F'), ('Tabitha', 17, 'F'),
  ('Tindo', 17, 'M'), ('Matata', 12, 'M'), ('jamaml', 15, 'M'),
  ('Joe', 11, 'M'), ('George', 14, 'M'), ('rose', 16, 'F'),
  ('Maria', 17, 'F'), ('Maggie', 17, 'F');

-- teachers
INSERT INTO teacher (name, age, gender) VALUES
  ('Kamotho', 45, 'M'), ('Kinuthia', 46, 'M'),
  ('Muthoni', 55, 'F'), ('Rachel', 35, 'F');

-- relationships (who teaches who)
INSERT INTO students_teachers (student_id, teacher_id) VALUES
  (8, 1), (9, 3), (10, 2), (10, 1);
```

So looking at the join table data:
- Student 8 (George) is taught by Teacher 1 (Kamotho)
- Student 9 (rose) is taught by Teacher 3 (Muthoni)
- Student 10 (Maria) is taught by Teacher 2 (Kinuthia) AND Teacher 1 (Kamotho) — she has **two** teachers
- Students 1–7 and 11 have **no teacher assigned** — they exist in the students table but have no row in students_teachers
- Teacher 4 (Rachel) has **no students assigned** — she exists in the teacher table but has no row in students_teachers

> This is intentional. Real databases always have gaps like this. Some students haven't been assigned yet. Some teachers are new. JOINs are how you decide what to do with those gaps.

This is the exact setup that makes JOINs interesting. Keep this data in mind as we go through each join type — you'll see how each one handles these gaps differently.

---

### Why JOINs Exist

Imagine you want to answer: *"What are the names of the students taught by Kamotho?"*

The `students` table has names. The `teacher` table has Kamotho. The `students_teachers` table connects them. No single table has all the information — you need to JOIN them.

Without JOINs, you'd have to run multiple queries and manually match the results in your head or in code:

```sql
-- Step 1: find Kamotho's id
SELECT id FROM teacher WHERE name = 'Kamotho';
-- returns: 1

-- Step 2: find student_ids linked to teacher 1
SELECT student_id FROM students_teachers WHERE teacher_id = 1;
-- returns: 8, 10

-- Step 3: find names for those student ids
SELECT name FROM students WHERE id IN (8, 10);
-- returns: George, Maria
```

That's 3 separate queries. JOINs collapse all of that into one.

---

### The JOIN Family — Overview

Here are all the JOIN types we'll cover:

| JOIN Type | What it returns | Includes unmatched left? | Includes unmatched right? |
|---|---|---|---|
| `INNER JOIN` | Only rows with a match in BOTH tables | No | No |
| `LEFT JOIN` | All rows from the left table + matched rows from the right | Yes | No |
| `RIGHT JOIN` | All rows from the right table + matched rows from the left | No | Yes |
| `FULL OUTER JOIN` | All rows from both tables, matched where possible | Yes | Yes |
| `CROSS JOIN` | Every combination of rows from both tables | N/A | N/A |
| `SELF JOIN` | A table joined to itself | Depends on join type used | Depends on join type used |

SQLite supports INNER JOIN, LEFT JOIN, CROSS JOIN, and SELF JOIN natively. RIGHT JOIN and FULL OUTER JOIN can be simulated using LEFT JOIN with table order swapped or UNION.

---

### 1. INNER JOIN

An INNER JOIN returns only the rows where there is a **matching value in both tables**. If a row in the left table has no match in the right table (or vice versa), it is completely excluded from the result.

Think of it as the **intersection** — only what both tables agree on. Like a Venn diagram where you only care about the overlapping middle part.

**Syntax:**

```sql
SELECT table1.column, table2.column
FROM table1
INNER JOIN table2
ON table1.shared_column = table2.shared_column;
```

**Your example** — from `SELECT student_of_tch3.sql`:

```sql
SELECT students.name, students.id
FROM students
INNER JOIN students_teachers
ON students.id = students_teachers.student_id
WHERE students_teachers.teacher_id = 1;
```

Let's break this down line by line:

- `SELECT students.name, students.id` — we want the student's name and id
- `FROM students` — start from the students table (this is the **left** table)
- `INNER JOIN students_teachers` — join it with the students_teachers table (the **right** table)
- `ON students.id = students_teachers.student_id` — the link: match rows where the student's id equals the student_id in the join table
- `WHERE students_teachers.teacher_id = 1` — filter: only keep rows where the teacher is Kamotho (id = 1)

**Result:**

```
name    id
------  --
George  8
Maria   10
```

Only George (id 8) and Maria (id 10) have a row in `students_teachers` with `teacher_id = 1`. Everyone else is excluded — including students with no teacher at all.

**Another example** — get all students and their teachers (no WHERE filter):

```sql
SELECT students.name, teacher.name
FROM students
INNER JOIN students_teachers ON students.id = students_teachers.student_id
INNER JOIN teacher ON students_teachers.teacher_id = teacher.id;
```

Result:

```
students.name  teacher.name
-------------  ------------
George         Kamotho
rose           Muthoni
Maria          Kinuthia
Maria          Kamotho
```

Notice: bob, dogo, Tabitha, Tindo, Matata, jamaml, Joe, Maggie — all excluded. They have no entry in `students_teachers`. Rachel (teacher) is also excluded — she has no students.

That's INNER JOIN: **strict, no gaps, only confirmed matches**.

> **Key rule:** If either side of the ON condition is NULL or has no match, that row is dropped entirely. INNER JOIN is the most restrictive join — it only keeps rows that exist in both tables.

---

### 2. LEFT JOIN (also called LEFT OUTER JOIN)

A LEFT JOIN returns **all rows from the left table**, and the matched rows from the right table. If a row in the left table has no match in the right table, it still appears in the result — but the columns from the right table will be `NULL`.

Think of it as: *"Give me everything from the left, and attach whatever you can find from the right. If you can't find anything, just leave it blank (NULL)."*

**Syntax:**

```sql
SELECT table1.column, table2.column
FROM table1
LEFT JOIN table2
ON table1.shared_column = table2.shared_column;
```

**Example using your tables** — get all students and their teacher (if they have one):

```sql
SELECT students.name, students.id, teacher.name AS teacher_name
FROM students
LEFT JOIN students_teachers ON students.id = students_teachers.student_id
LEFT JOIN teacher ON students_teachers.teacher_id = teacher.id;
```

Result:

```
name     id   teacher_name
-------  ---  ------------
bob      1    NULL
dogo     2    NULL
Tabitha  3    NULL
Tindo    4    NULL
Matata   5    NULL
jamaml   6    NULL
Joe      7    NULL
George   8    Kamotho
rose     9    Muthoni
Maria    10   Kinuthia
Maria    10   Kamotho
Maggie   11   NULL
```

Every student shows up. The ones with no teacher get `NULL` in the `teacher_name` column. Maria appears twice because she has two teachers.

**When to use LEFT JOIN:**
- When you want to see all records from one table regardless of whether they have a match
- When you want to find records with **no match** (unassigned students, orphaned records, etc.)

**Finding students with NO teacher assigned:**

```sql
SELECT students.name, students.id
FROM students
LEFT JOIN students_teachers ON students.id = students_teachers.student_id
WHERE students_teachers.student_id IS NULL;
```

Result:

```
name     id
-------  --
bob      1
dogo     2
Tabitha  3
Tindo    4
Matata   5
jamaml   6
Joe      7
Maggie   11
```

This is a very common pattern — LEFT JOIN + `WHERE right_table.column IS NULL` to find records that have **no relationship**. It's sometimes called an **anti-join** or **exclusion join**.

The logic: after the LEFT JOIN, any student with no match in `students_teachers` will have `NULL` in the `students_teachers.student_id` column. Filtering for `IS NULL` gives you exactly those students.

---

### 3. RIGHT JOIN (also called RIGHT OUTER JOIN)

A RIGHT JOIN is the mirror image of a LEFT JOIN. It returns **all rows from the right table**, and the matched rows from the left table. If a row in the right table has no match in the left table, it still appears — with `NULL` for the left table's columns.

**Syntax:**

```sql
SELECT table1.column, table2.column
FROM table1
RIGHT JOIN table2
ON table1.shared_column = table2.shared_column;
```

> **SQLite note:** SQLite does not natively support RIGHT JOIN. You can achieve the same result by swapping the table order and using a LEFT JOIN instead. This is not a limitation in practice — every RIGHT JOIN can be rewritten as a LEFT JOIN by putting the "right" table first.

**Example** — get all teachers and their students (if they have any):

```sql
-- Standard SQL (works in MySQL, PostgreSQL)
SELECT students.name AS student_name, teacher.name AS teacher_name
FROM students_teachers
RIGHT JOIN teacher ON students_teachers.teacher_id = teacher.id
LEFT JOIN students ON students_teachers.student_id = students.id;
```

**SQLite equivalent** (swap tables, use LEFT JOIN):

```sql
SELECT students.name AS student_name, teacher.name AS teacher_name
FROM teacher
LEFT JOIN students_teachers ON teacher.id = students_teachers.teacher_id
LEFT JOIN students ON students_teachers.student_id = students.id;
```

Result:

```
student_name  teacher_name
------------  ------------
George        Kamotho
Maria         Kamotho
rose          Muthoni
Maria         Kinuthia
NULL          Rachel
```

Rachel appears even though she has no students — her `student_name` is `NULL`. That's the RIGHT JOIN behaviour: the right table (teacher) is fully preserved.

**When to use RIGHT JOIN:**
- When you want all records from the right table regardless of matches
- Finding teachers with no students, products with no orders, categories with no items, etc.
- In practice, most developers just flip the table order and use LEFT JOIN — same result, more widely supported

---

### 4. FULL OUTER JOIN

A FULL OUTER JOIN returns **all rows from both tables**. Where there's a match, the columns are filled in. Where there's no match on either side, `NULL` fills the gaps.

Think of it as LEFT JOIN + RIGHT JOIN combined — you get everything, matched or not. In a Venn diagram, this is the entire circle — both sides plus the overlap.

**Syntax:**

```sql
SELECT table1.column, table2.column
FROM table1
FULL OUTER JOIN table2
ON table1.shared_column = table2.shared_column;
```

> **SQLite note:** SQLite does not support FULL OUTER JOIN directly. You simulate it using `LEFT JOIN` combined with `UNION` and another `LEFT JOIN` with tables swapped. The `UNION` keyword merges the two result sets and removes duplicate rows automatically.

**SQLite simulation:**

```sql
-- All students with their teachers (LEFT side)
SELECT students.name AS student_name, teacher.name AS teacher_name
FROM students
LEFT JOIN students_teachers ON students.id = students_teachers.student_id
LEFT JOIN teacher ON students_teachers.teacher_id = teacher.id

UNION

-- All teachers with their students (RIGHT side — catches unmatched teachers)
SELECT students.name AS student_name, teacher.name AS teacher_name
FROM teacher
LEFT JOIN students_teachers ON teacher.id = students_teachers.teacher_id
LEFT JOIN students ON students_teachers.student_id = students.id;
```

Result:

```
student_name  teacher_name
------------  ------------
bob           NULL
dogo          NULL
Tabitha       NULL
Tindo         NULL
Matata        NULL
jamaml        NULL
Joe           NULL
George        Kamotho
rose          Muthoni
Maria         Kinuthia
Maria         Kamotho
Maggie        NULL
NULL          Rachel
```

Every student and every teacher appears. Unmatched students get `NULL` for teacher. Rachel (unmatched teacher) gets `NULL` for student.

**When to use FULL OUTER JOIN:**
- Auditing — find all unmatched records on both sides at once
- Data reconciliation between two datasets
- Merging two tables where either side may have records the other doesn't
- Reporting dashboards where you need to show all entities regardless of activity

---

### 5. CROSS JOIN

A CROSS JOIN returns the **Cartesian product** of two tables — every row from the left table is combined with every row from the right table. No `ON` condition is needed because you're not matching anything — you're combining everything.

If table A has 11 rows and table B has 4 rows, a CROSS JOIN gives you 11 × 4 = **44 rows**.

The name "Cartesian product" comes from mathematics — it's the set of all ordered pairs from two sets. In SQL terms: every possible pairing.

**Syntax:**

```sql
SELECT table1.column, table2.column
FROM table1
CROSS JOIN table2;
```

**Example** — pair every student with every teacher:

```sql
SELECT students.name AS student, teacher.name AS teacher
FROM students
CROSS JOIN teacher;
```

This gives you 11 students × 4 teachers = **44 rows**. Every possible student-teacher pairing.

```
student   teacher
--------  --------
bob       Kamotho
bob       Kinuthia
bob       Muthoni
bob       Rachel
dogo      Kamotho
dogo      Kinuthia
... (44 rows total)
```

**When to use CROSS JOIN:**
- Generating all possible combinations (e.g., scheduling, seating arrangements)
- Creating test data
- Building a matrix of options (sizes × colors, students × subjects)
- Generating a calendar grid (days × time slots)

> ⚠️ **Warning:** CROSS JOIN on large tables can produce enormous result sets. 1000 rows × 1000 rows = 1,000,000 rows. Use with care.

---

### 6. SELF JOIN

A SELF JOIN is when a table is joined **to itself**. This sounds strange at first, but it's useful when rows in a table have a relationship with other rows in the same table.

To do a self join, you use table aliases — you give the same table two different names so SQL can tell them apart. Without aliases, SQL wouldn't know which "students" you mean when you write `students.id = students.id`.

**Syntax:**

```sql
SELECT a.column, b.column
FROM table_name AS a
INNER JOIN table_name AS b
ON a.shared_column = b.related_column;
```

**Example** — find all pairs of students who are the same age:

```sql
SELECT a.name AS student1, b.name AS student2, a.age
FROM students AS a
INNER JOIN students AS b
ON a.age = b.age
WHERE a.id < b.id;
```

The `WHERE a.id < b.id` prevents duplicates — without it you'd get (bob, dogo) AND (dogo, bob), plus each student paired with themselves. The `<` ensures each pair only appears once, and a student is never paired with themselves.

Result (partial):

```
student1  student2  age
--------  --------  ---
bob       dogo      15
bob       jamaml    15
dogo      jamaml    15
Tabitha   Tindo     17
Tabitha   Maria     17
Tabitha   Maggie    17
Tindo     Maria     17
Tindo     Maggie    17
Maria     Maggie    17
```

**Another real-world use case** — imagine a table of employees where each row has a `manager_id` that references another employee's `id` in the same table:

```sql
SELECT e.name AS employee, m.name AS manager
FROM employees AS e
LEFT JOIN employees AS m ON e.manager_id = m.id;
```

**When to use SELF JOIN:**
- Hierarchical data (employees and their managers, categories and subcategories)
- Finding duplicate or related records within the same table
- Comparing rows within the same table
- Finding students/employees/items that share a common attribute (same age, same department, same price)

---

### 7. The JOIN Table Pattern (Many-to-Many Relationships)

Your `students_teachers` table is a perfect example of a **join table** — the standard way to model a many-to-many relationship in SQL.

The relationship here is: one student can have many teachers, and one teacher can have many students. You can't store that in just two tables without repeating data. The join table solves this cleanly.

**Why not just add a `teacher_id` column to the students table?**

Because Maria has TWO teachers. If you added `teacher_id` to the students table, you'd need two rows for Maria — duplicating her name, age, and gender. That's messy and inconsistent. The join table keeps each entity in one place and only stores the relationship separately.

Here's the same pattern from your `python-p3-creating-join-tables` folder:

```sql
-- from create_join_table.sql
CREATE TABLE cat_owners(
  cat_id INTEGER,
  owner_id INTEGER
);
```

And the query to find the owner of cat 3:

```sql
-- from SELECT owners_name of cat 3.sql
SELECT owner.name
FROM owner
INNER JOIN cat_owners
ON owner.id = cat_owners.owner_id
WHERE cat_owners.cat_id = 3;
```

Same pattern as your school database — just cats and owners instead of students and teachers. The logic is identical:
1. Start from the table you want data from (`owner`)
2. JOIN through the join table (`cat_owners`)
3. Filter by the id you're looking for (`cat_id = 3`)

This 3-step mental model works for any many-to-many JOIN query you'll ever write.

---

### 8. Using Table Aliases in JOINs

As your queries get longer, typing full table names repeatedly gets tedious. SQL lets you use **aliases** — short nicknames for tables — using the `AS` keyword (or just a space).

```sql
-- Without aliases
SELECT students.name, teacher.name
FROM students
INNER JOIN students_teachers ON students.id = students_teachers.student_id
INNER JOIN teacher ON students_teachers.teacher_id = teacher.id;

-- With aliases (much cleaner)
SELECT s.name AS student_name, t.name AS teacher_name
FROM students AS s
INNER JOIN students_teachers AS st ON s.id = st.student_id
INNER JOIN teacher AS t ON st.teacher_id = t.id;
```

Both queries return the same result. The aliased version is easier to read and write, especially with 3+ table joins.

> **Convention:** Single-letter aliases (`s`, `t`, `st`) are common for short queries. For complex queries with many tables, use more descriptive aliases like `stud`, `tchr` to keep things readable.

---

### 9. Joining More Than Two Tables

You're not limited to two tables. You can chain as many JOINs as you need. Each JOIN adds another table to the query.

**Example** — get student names, their teacher names, and filter to only female teachers:

```sql
SELECT s.name AS student, t.name AS teacher, t.gender
FROM students AS s
INNER JOIN students_teachers AS st ON s.id = st.student_id
INNER JOIN teacher AS t ON st.teacher_id = t.id
WHERE t.gender = 'F';
```

Result:

```
student  teacher   gender
-------  -------   ------
rose     Muthoni   F
```

Only rose is taught by a female teacher (Muthoni). Maria's teachers are Kamotho and Kinuthia — both male — so she doesn't appear.

---

### 10. JOIN with Aggregate Functions

You can combine JOINs with aggregate functions like `COUNT`, `GROUP BY`, etc.

**Example** — count how many students each teacher has:

```sql
SELECT t.name AS teacher, COUNT(st.student_id) AS student_count
FROM teacher AS t
LEFT JOIN students_teachers AS st ON t.id = st.teacher_id
GROUP BY t.id, t.name;
```

Result:

```
teacher   student_count
--------  -------------
Kamotho   2
Kinuthia  1
Muthoni   1
Rachel    0
```

Rachel shows up with 0 because we used LEFT JOIN — she has no students but we still want her in the result. If we used INNER JOIN, Rachel would be excluded entirely.

**Example** — count how many teachers each student has:

```sql
SELECT s.name AS student, COUNT(st.teacher_id) AS teacher_count
FROM students AS s
LEFT JOIN students_teachers AS st ON s.id = st.student_id
GROUP BY s.id, s.name;
```

Result:

```
student   teacher_count
--------  -------------
bob       0
dogo      0
Tabitha   0
Tindo     0
Matata    0
jamaml    0
Joe       0
George    1
rose      1
Maria     2
Maggie    0
```

---

### 11. The `tableName.columnName` Notation

You already saw this in Lesson 6 — but it becomes **essential** in JOINs. When two tables have a column with the same name (like both having an `id` column), SQL needs you to be explicit about which one you mean.

```sql
-- This is ambiguous and will cause an error:
SELECT id, name FROM students INNER JOIN teacher ON students.id = teacher.id;
-- Error: ambiguous column name: id

-- This is explicit and correct:
SELECT students.id, students.name, teacher.name
FROM students
INNER JOIN teacher ON students.id = teacher.id;
```

Always use `table.column` notation in JOIN queries to avoid ambiguity errors.

---

### 12. Visual Summary — Which JOIN to Use?

```
  students table          students_teachers          teacher table
  (11 rows)               (4 rows)                   (4 rows)

  bob      (1)                                        Kamotho  (1)
  dogo     (2)                                        Kinuthia (2)
  Tabitha  (3)                                        Muthoni  (3)
  Tindo    (4)                                        Rachel   (4)
  Matata   (5)
  jamaml   (6)            (8,1)  (9,3)
  Joe      (7)            (10,2) (10,1)
  George   (8) ---------->
  rose     (9) ---------->
  Maria    (10) --------->
  Maggie   (11)
```

| Question | JOIN to use |
|---|---|
| Only students who have a teacher? | `INNER JOIN` |
| All students, show teacher if they have one | `LEFT JOIN` (students on left) |
| All teachers, show students if they have any | `LEFT JOIN` (teacher on left) or `RIGHT JOIN` |
| All students AND all teachers, matched where possible | `FULL OUTER JOIN` (or UNION in SQLite) |
| Every possible student-teacher pairing | `CROSS JOIN` |
| Students who share the same age | `SELF JOIN` |

---

### Quick Reference — JOIN Syntax

```sql
-- INNER JOIN
SELECT s.name, t.name
FROM students s
INNER JOIN students_teachers st ON s.id = st.student_id
INNER JOIN teacher t ON st.teacher_id = t.id;

-- LEFT JOIN
SELECT s.name, t.name
FROM students s
LEFT JOIN students_teachers st ON s.id = st.student_id
LEFT JOIN teacher t ON st.teacher_id = t.id;

-- FULL OUTER JOIN (SQLite simulation)
SELECT s.name, t.name FROM students s
LEFT JOIN students_teachers st ON s.id = st.student_id
LEFT JOIN teacher t ON st.teacher_id = t.id
UNION
SELECT s.name, t.name FROM teacher t
LEFT JOIN students_teachers st ON t.id = st.teacher_id
LEFT JOIN students s ON st.student_id = s.id;

-- CROSS JOIN
SELECT s.name, t.name
FROM students s
CROSS JOIN teacher t;

-- SELF JOIN
SELECT a.name, b.name
FROM students a
INNER JOIN students b ON a.age = b.age
WHERE a.id < b.id;
```

---

### Best Practices for JOINs

1. ✅ Always use `table.column` notation to avoid ambiguity
2. ✅ Use aliases (`AS s`, `AS t`) to keep long queries readable
3. ✅ Choose LEFT JOIN over INNER JOIN when you need to preserve unmatched rows
4. ✅ Use a join table for many-to-many relationships
5. ✅ Combine JOINs with `WHERE`, `GROUP BY`, and aggregate functions for powerful queries
6. ✅ Be careful with CROSS JOIN on large tables — the result set grows fast
7. ✅ In SQLite, simulate RIGHT JOIN by swapping table order with LEFT JOIN
8. ✅ In SQLite, simulate FULL OUTER JOIN using `LEFT JOIN ... UNION ... LEFT JOIN`
8. ✅ In SQLite, simulate FULL OUTER JOIN using `LEFT JOIN ... UNION ... LEFT JOIN`