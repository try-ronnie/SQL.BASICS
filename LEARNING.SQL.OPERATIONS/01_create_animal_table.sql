CREATE TABLE animals (
id INTERGER PRIMARY KEY,
name TEXT ,
age INTERGER ,
breed TEXT,
alive BOOLEAN NOT NULL CHECK (alive IN (0,1)));

```# BOOLEAN is -indicates that we store these values as true or false 
 logic not null  - ensures that all rows have a value of whther its is dead or alive .... so its a yes or no occasion... 
CHECK (alive IN (0,1))
CHECK ....--- is a constraint too ... its ensures that only the values that satisfy the conditon are allowed in 
   -----> (alive In (0,1))  -- this is the condtion being checked right...
   alive - is the column we are refering to 
   IN -> means " must be one of "
   (0,1) -> allowed values 0 , 1  
   
   
   🧠 So why use CHECK if it's BOOLEAN?

Some databases (like SQLite) don’t have a true boolean type.
They treat BOOLEAN as INTEGER.

So this:

CHECK (alive IN (0,1))

Makes sure the column behaves like a real boolean:

0 = FALSE

1 = TRUE

2 ❌ not allowed

5 ❌ not allowed