CREATE TABLE students(
id INTEGER PRIMARY KEY , 
name TEXT NOT NULL, 
age INTEGER NOT NULL CHECK (age > 10 AND age < 18),
gender TEXT NOT NULL CHECK (gender in ('M', 'F'))
);