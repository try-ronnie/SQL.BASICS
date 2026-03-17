CREATE TABLE student (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL , 
age INTEGER CHECK (age > 8 AND  age < 18,
gender TEXT CHECK (gender in ('M', 'F')
);
