CREATE TABLE bears(
id INTEGER PRIMARY KEY,
name TEXT , 
age INTEGER,
sex TEXT, 
color TEXT,
temperament TEXT , 
alive BOOLEAN NOT NULL CHECK(alive IN (0,1)));

/*-- 🎯 So Why Use Both?

-- Because:
-- BOOLEAN = meaning + type behavior
-- CHECK (0,1) = safety enforcement (especially in weak DBs like SQLite)
-- 🏆 The Deep Truth
-- If your DB properly supports BOOLEAN (like PostgreSQL):
-- You don’t even need:
-- CHECK (alive IN (0,1))
-- Because it already enforces true/false.
-- That CHECK is mostly used when the DB doesn’t truly enforce boolean.
*/