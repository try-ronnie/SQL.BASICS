CREATE TABLE students(
id INTERGER PRIMARY KEY , 
name TEXt NOT NULL, 
age INTEGER NOT NULL CHECK (age > 10 AND age < 18),
gender TEXT NOT NULL CHECK (gender in ('M', 'F'))
);