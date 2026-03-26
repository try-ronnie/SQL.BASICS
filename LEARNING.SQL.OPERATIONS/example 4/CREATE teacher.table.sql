CREATE TABLE teacher(
id INTEGER PRIMARY KEY , 
name TEXT NOT NULL , 
age INTEGER NOT NULL CHECK (age > 25 AND age < 65),
gender TEXT NOT NULL CHECK (gender in ('M', 'F'))
);
