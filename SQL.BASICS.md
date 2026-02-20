## prior coding knowledge is required
# LESSON 1 : BACIC SQL COMMANDS 
## sql is a klanguage used to maintain relational databases


### command : sqlite 3 creating a database
to start sql  ```sqlite3 pet_database.db```  (this is just like creating the file) .... it then means that you are going to work on that database
then we need to create a table format indie the db file .... 
SQLite expects us to include at least some definition of the structure of this table as well. In other words, when we create database tables, we need to specify some column names, along with the type of data we are planning to store in each column. More on data types later.
```
CREATE TABLE cats (
  id INTEGER PRIMARY KEY,
  name TEXT,
  age INTEGER
);
```
Let's break down the above code:

Use the CREATE TABLE command to create a new table called "cats".
Include a list of column names along with the type of data they will be storing. TEXT means we'll be storing plain old text, INTEGER means we'll store a number. Note that the use of capitalization is arbitrary, but it is a convention to help separate the SQL commands from the names we make up for our tables and columns.
Every table we create, regardless of the other column names and data types, should be defined with an id INTEGER PRIMARY KEY column, including the integer data type and primary key designation. Our SQLite database tables must be indexed by a number. We want each row in our table to have a number, which we'll call "id", just like in an Excel spreadsheet. Numbering our table rows makes our data that much easier to access, update, and organize. SQLite comes with a data type designation called "Primary Key". Primary keys are unique and auto-incrementing, meaning they start at 1 and each new row automatically gets assigned the next numeric value. 

### command 2 : **Alter Table**
Let's say that, after creating a database and creating a table to live inside that database, we decide we want to add or remove a column. We can do so with the ALTER TABLE statement.

Let's say we want to add a new column, breed, to our cats table:

```ALTER TABLE cats ADD COLUMN breed TEXT;```

Let's check out our schema now:
```
sqlite> .schema
CREATE TABLE cats (
  id INTEGER PRIMARY KEY,
  name TEXT,
  age INTEGER,
  breed TEXT ## new coulmn made ....
);
```
Notice that the ALTER statement isn't here, but instead SQLite has updated our original CREATE statement. The schema reflects the current structure of the database, which is reflected as the CREATE statement necessary to create that structure.

Unfortunately, altering a column name and/or deleting a column can be tricky in SQLite3. There are workarounds, however. We're not going to get into that right now, but you can explore...

command 3 : DROPPING A TABLE
practically just deleting a table 

Deleting a table is very simple:

```DROP TABLE cats;```
And that's it! You can exit out of the sqlite prompt with the .quit command.


FLOW: sqlite3 <database.db>
      create table with the info required


### LESSON 2 :  WRITING SQL IN A TEXT EDITOR

SQL is a programming language like any other, so we can write SQL in our text editor and execute it. This allows us to keep better track of our SQL code, including the SQL statements that create tables and query data from those tables.

To write SQL in our text editor and execute that SQL against a specific database, we'll create files in our text editor that have the .sql extension. These files will contain valid SQL code. Then, we can execute these files against our database in the command line. We'll take a look at this process together in the following code along.


create a file with the **.sql** extension

then the same commands used in the terminal can be written in those files separately ... there should be a file to ADD A COLUMN using the command 
```
ALTER TABLE animals ADD COLUMN price INTERGER
```
the above code is then stored in an SQL file with a name like *add_column.sql*

example in SQL TEXT EDITING  the concept is that you use a file with the pre-written SQL command instead of typing every single time in  the terminal then inorder to use it 

then in the terminal ...
with the premade databse inorder to put the file in action
:
```
sqlite3 animals._database.db < add_colum.sql
```
hence the file will get a new column according to the details passed in the file


### LESSON 4 ; WHY DO DATA TYPES MATTER IN SQL

We've learned that when we create a table, we need to include a name for it as well as define at least one column. We define columns in a CREATE statement by including a name and a datatype to let SQLite know the kind of data we will be storing there. The practice of explicitly declaring a type is known as "typing."

Why is it important that we use typing in our database? Simply put, typing allows us to exercise some level of control over our data. Typing not only informs our database of the kind of data we plan to store in a column, but it also restricts it. For instance, look at the age column below in our cats table. What do we mean by age? What if we had this:


name	  breed	                   age
Maru	  Scottish Fold	            3
Hannah	  Tabby	                    two
Lil' Bub  American Shorthair	    5.5


Did we intend age to be represented as a whole number, a word, or a decimal? If we asked you to add up the ages of all the cats you could simply convert the 'two' to 2 in your head, but your database can't do that. It doesn't have that ability, because the logic involved in converting a word into a number would be dense and inefficient. What about different languages? What about different spellings? Capitalization, typos, or different hyphenation conventions? These are just some reasons this might start to get crazy. In other words, because databases are designed to store large amounts of data, they are very concerned with storing, accessing, and acting upon that data as efficiently and normally as possible.

Typing gives us the ability to perform all kinds of operations with predictable results. For instance, the ability to perform math operations like SUM — i.e. summing integers — doesn't just depend on everything being an integer of some sort but would also expect it. If you tried, for example, to SUM all of the cats in the above table, SQLite would actually attempt to convert, or cast, their type to something it can SUM. It would try to convert anything it can to an INTEGER and ignore alpha characters. This can lead to real problems. Without typing, our data might get complicated and messy, and it would be difficult to ask the database questions about large sets of data.]

#### DATATYPES 
Different database systems also have different datatypes available, which are important and useful to know whenever you are dealing with those systems. SQLite is a good starting point to learn about datatypes because it only has five basic categories of datatypes; they are:
> NULL In a database, NULL represents "no value", like null in JavaScript or None in Python.
>TEXT Any alphanumeric characters which we want to represent as plain text. The body of this paragraph is text. Your name is text. Your email address is a piece of text. Your height, weight, and age, however, are probably not.
>INTEGER  Anything we want to represent as a whole number. If it's a number and contains no letter or special characters or decimal points then we should store it as an integer. If we use it to perform math or create a comparison between two different rows in our database, then we definitely want to store it as an integer. If it's just a number, it's generally not a bad idea to store it as an integer. You might never add two house address numbers together, but you might want to sort them numerically. For example, in the preceding case you might want to get the biggest number and not the longest piece of text.
>REAL Anything that's a plain old decimal like 1.3 or 2.25. SQLite will store decimals up to 15 characters long. You can store 1.2345678912345 or 1234.5678912345, but 1.23456789123456789 would only store 1.2345678912345. In other database systems this is called 'double precision.'

With these three types in hand, we are going to be able to work our way through the next several topics, and this whole typing concept is going to quickly become second nature for you.


>BLOBYou may encounter the BLOB datatype while you're Googling or doing any further reading on SQLite. For now, we will not use BLOB. It is generally used for holding binary data.

##### BONUS ON SQL LITE 
>increase its compatibility with other database engines (e.g. mySQL or PostgreSQL), SQLite allows the programmer to use other common datatypes outside of the four mentioned above. We can refer to TEXT INTEGER REAL BLOB as datatype "categories". All other common datatypes are lumped into one of the four existing datatypes recognized by SQLite.
>For example, INT is a common datatype used outside of SQLite. SQLite won't complain if you define a column as an INT datatype. It will simply lump it into the INTEGER category and store it as such.
>Boolean values are also stored as integers (0 for false, 1 for true).
>To accommodate this, SQLite has a pretty complicated system of categorizing datatypes that involves Storage Classes, Type Affinities, and Datatypes. For a deeper dive, check out the [documentation](http://www.sqlite.org/datatype3.)

### LESSON 5 CRUD OPERATIOS IN SQL
create, Read , update and delete actions in database


this done in [github.repo](https://github.com/try-ronnie/python-p3-sql-crud#)

these are the actions :
    1. INSERT INTO 
      ```INSERT INTO cats (name, age, breed) VALUES ('Maru', 3, 'Scottish Fold');```
> We use the INSERT INTO command, followed by the name of the table to which we    want to add data. Then, in parentheses, we put the column names that we will be filling with data. This is followed by the VALUES keyword, which is accompanied by a parentheses
>Important: Note that we didn't specify the "id" column name or value. Since we created the cats table with an "id" column whose type is INTEGER PRIMARY KEY, we don't have to specify the id column values when we insert data. Primary Key columns are auto-incrementing. As long as you have defined an id column with a data type of INTEGER PRIMARY KEY, a newly inserted row's id column will be automatically given the correct value.
>THIS COMMAND CAN SRTILL BE USED IN FILE WITH SQL LANGUAGE


> ### REMEMBER that for sql command we must end all of them with semicolons 
    2. SELECT FROM :
    ```SELECT [names of columns we are going to select] FROM [table we are selecting from]```
    SELECT column FROM

    We specify the names of the columns we want to SELECT and then tell SQL the table we want to select them FROM.

We want to select all the rows in our table, and we want to return the data stored in any and all columns in those rows. To do this, we could pass the name of each column explicitly.

For the rest of this code along, you can run the SQL commands one of two ways, depending on your preference.

You can either open the database using the sqlite3 CLI, and run the SQL commands from the terminal:  sqlite3 pets_database.db

Depending on which examples to use we can use this it it should return the respective columns the user had selected ... 
A faster way to get data from every column in our table is to use a special selector, known commonly as the 'wildcard' selector *. The * selector means: "Give me all the data from all the columns for all of the cats" Using the wildcard, we can SELECT all the data from all of the columns in the cats table like this:
```SELECT * FROM cats;```

>SELECT name, age FROM cats;
Top-Tip: If you have duplicate data (for example, two cats with the same name) and you only want to select unique values, you can use the DISTINCT keyword. For example:

SELECT DISTINCT name FROM cats;


so if we wrote 
SELECT name FROM cats;

and it returned :  
        LUNA 
        TEMBO 
        LUNA 
        GOMA 

If we wanted no repetitive name sin our listings .... 
SELECT DISTINCT name FROM cats ;

hen the result would be :
        LUNA 
        TEMBI
        GOMA

but if we used 
SELECT DISTINCT name , age FROM cats ;
      LUNA - 5 
      TEMBO -3
      GOMA -12
      LUNA - 6

not that this time select doesnt remove 'LUNA' since both have different ages hence it differentiates them 
but if the had the same age then they would both be removed and takenin as one since both are duplicates according to the colums that were selected 
🎯 Key Rule

DISTINCT means:

"Remove rows where all selected column values are exactly the same."

It does NOT:

Identify “original” rows

Compare IDs unless you select them

Know which record came first (unless you use ORDER BY)

🧩 Simple Mental Model

Think of DISTINCT like this:

It puts the results in a basket and says:

"If I already saw this exact value before, don’t show it again."

That’s it.

***Selecting Based on Conditions: The WHERE Clause***
What happens when we want to retrieve a specific table row? For example the row that belongs to Maru? Or to retrieve all the baby cats who are younger than two years old? We can use the WHERE keyword to select data based on specific conditions. Here's an example of a boilerplate SELECT statement using a WHERE clause.

its a conditional that only returns the values in the tbale that meet the requirement:

``` SELECT * FROM [table name] WHERE [Column-anme]= [some value ];```
meaning that every value from the column selected should be return only if they meet the condition (of some value)
We can also use comparison operators, like < or > to select specific data. Let's give it a shot. Use the following statement to select the young cats:

>***ALWAYS REMEMBER WHT FOLLOWS SELECT IS THE COLUMN TO BE RETRIEVED FOR CHECKING***


3. UPDATE 
a boiler plate update state ments looks like this
```UPDATE [table name] SET [column name] = [new value] WHERE [column name] = [value];```
The UPDATE statement uses a WHERE clause to grab the row you want to update. It identifies the table name you are looking in and resets the data in a particular column to a new value.

this isnt quite heavy , we just eed to know that ,
we say UPDATE (table) and set the value you want to give 
where the condtion is that in that column the value that we want to change

update -> set new value  from the coum name -> where the column had the old value ;

SO when we update We say :
  1. which table (```UPDATE school```)
  2.  set the column where the value whill be plced , so we have to name the column then value to be set i it (```SET name = "value"```)
  3. then we introduce where ... cause ofc where the previous value was .... the column name and the value
  (```WHERE name = "KAMOTHO```)




4. DELETE
A boilerplate DELETE statement looks like this:
``` DELETE FROM [table name] WJERE [column name] = [value]```

in the case of wanting to eliminate whitespaces in our table when getting the data or we maybe we want to get values but we cant since the user included white spaces 

``` DELETE FROM shcool WHERE TRIM(name) = 'dj khalid'```
this ensures athat we trima ny white spaces that come along 

💡 Tip: You can check if there are hidden spaces by doing
SELECT '"' || name || '"' FROM school;
It will wrap the name in quotes so you can see extra spaces clearly.
1. TRIM / LTRIM / RTRIM

Purpose: Remove whitespace (or other characters) from strings.

Syntax:

TRIM(column)        -- removes spaces from both ends
LTRIM(column)       -- removes spaces from the left/start
RTRIM(column)       -- removes spaces from the right/end


Example:

SELECT TRIM(name) FROM school;
DELETE FROM school WHERE TRIM(name) = 'dj khalid';

2. UPPER / LOWER

Purpose: Convert strings to uppercase or lowercase. Useful when your data has inconsistent casing.

Example:

SELECT * FROM school WHERE UPPER(name) = 'DJ KHALID';
SELECT LOWER(name) FROM school;

3. LENGTH

Purpose: Count the number of characters in a string.

Example:

SELECT name, LENGTH(name) FROM school;
-- Can help find hidden trailing spaces

4. SUBSTR

Purpose: Extract part of a string.

Syntax: SUBSTR(column, start, length)

Example:

SELECT SUBSTR(name, 1, 5) FROM school;
-- Will return first 5 characters

5. REPLACE

Purpose: Replace all occurrences of a substring with another substring.

Example:

SELECT REPLACE(name, ' ', '') FROM school;
-- Removes all spaces from names

6. LIKE / GLOB

Purpose: Pattern matching.

Example:

SELECT * FROM school WHERE name LIKE 'dj khalid%';
-- % = any characters after "dj khalid"

Quick Combo for Cleaning Names

If you want to delete rows ignoring extra spaces and case:

DELETE FROM school
WHERE UPPER(TRIM(name)) = UPPER('dj khalid');


This is a robust pattern because it ignores hidden spaces and casing issues.
