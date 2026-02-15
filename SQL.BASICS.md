## prior coding knowledge is required
# LESSON 1 : BACIC SQL COMMANDS 
## sql is a klanguage used to maintain relational databases


### command : sqlite 3 creating a database
to start sql  ```sqlite3 pet_database.db``` 
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