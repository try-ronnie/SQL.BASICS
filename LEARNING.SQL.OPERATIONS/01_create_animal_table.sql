CREATE TABLE animals (
id INTERGER PRIMARY KEY,
name TEXT ,
age INTERGER ,
breed TEXT,
alive BOOLEAN NOT NULL CHECK (alive IN (0,1)));

```# BOOLEAN is -indicates that we store these vales as true or false 