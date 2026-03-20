🔐 1. How do bound parameters prevent SQL injection?

This line is the key:

CURSOR.execute(sql, (self.name, self.location))


Instead of doing this (❌ dangerous):

sql = f"INSERT INTO departments (name, location) VALUES ('{self.name}', '{self.location}')"

🚨 Problem with string formatting

If a user enters something like:

name = "HR'); DROP TABLE departments; --"


Your SQL becomes:

INSERT INTO departments (name, location)
VALUES ('HR'); DROP TABLE departments; --', 'Nairobi')


💥 Boom — your table is gone.

✅ What bound parameters do instead

When you write:

CURSOR.execute(sql, (self.name, self.location))


SQLite treats ? as placeholders, and:

Separates SQL logic from data

Sends the query and the data independently

Escapes everything properly

So the database sees:

INSERT INTO departments (name, location)
VALUES (?, ?)


And then safely inserts:

"HR'); DROP TABLE departments; --"


as just a string, not executable SQL.

👉 So:

Bound parameters don’t “clean” input — they prevent it from being interpreted as SQL at all.

🤔 2. Why do we pass parameters in execute()?

Because the database driver (SQLite here) is responsible for:

Escaping dangerous characters

Handling data types correctly

Preventing SQL injection

If you embed values directly in SQL, Python is doing the work (bad idea).
If you pass them to execute(), SQLite does the work (safe).

🧠 3. Why self.name if we already know it's self?

Good question — this is about how objects work.

Inside a method like:

def save(self):


self is the whole object, not individual values.

So if you have:

department = Department("HR", "Nairobi")


Then:

self = department


To access its attributes, you must explicitly say:

self.name
self.location

⚡ Think of it like this:

self is a container:

self = {
    "id": None,
    "name": "HR",
    "location": "Nairobi"
}


So:

self → the whole object

self.name → one specific value inside it

🔁 Quick summary

Bound parameters (?):

Stop SQL injection by separating code from data

Let SQLite safely handle user input

Why in execute():

That’s where SQLite expects the values

It safely binds them to the query

Why self.name:

self is the object

You must access its attributes explicitly

💡 One small improvement for your code

Your decorator has a tiny typo:

@ classmethod   # ❌ space breaks it


Fix it:

@classmethod   # ✅
