CREATE TABLE bears(
id PRIMARY KEY INTERGER,
name TEXT , 
age INTEGER,
sex TEXT, 
color TEXT,
temperament TEXT , 
alive BOOLEAN NOT NULL CHECK(alive IN (0,1));

-- 🎯 So Why Use Both?

-- Because:
-- BOOLEAN = meaning + type behavior
-- CHECK (0,1) = safety enforcement (especially in weak DBs like SQLite)
-- 🏆 The Deep Truth
-- If your DB properly supports BOOLEAN (like PostgreSQL):
-- You don’t even need:
-- CHECK (alive IN (0,1))
-- Because it already enforces true/false.
-- That CHECK is mostly used when the DB doesn’t truly enforce boolean.
-- 🧠 Backend Dev Level Insight
-- You just stumbled onto something important:
-- Database types are not just about storage —
-- they’re about data meaning and system behavior.
-- That’s how senior engineers think.