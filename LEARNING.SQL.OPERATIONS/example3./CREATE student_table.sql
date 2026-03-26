
CREATE TABLE student (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL , 
age INTEGER CHECK (age > 8 AND  age < 18),
gender TEXT CHECK (gender in ('M', 'F')),
teacher_id INTEGER,
FOREIGN KEY (teacher_id) REFERENCES teacher(id) 
);
