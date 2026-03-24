## Why Use Bound Parameters in SQL Queries

Bound parameters (also called parameterized queries or prepared statements) are a crucial security and best practice feature in SQL. Here's why they're used:

### 1. Prevention of SQL Injection Attacks

**Without bound parameters (unsafe):**
```python
# User input directly concatenated into SQL string
user_input = "'; DROP TABLE providers; --"
CURSOR.execute(f"SELECT * FROM providers WHERE name = '{user_input}'")
```
This allows attackers to inject malicious SQL code.
SINCE whatever is type is connected directly to the sql query that is supposd to be carried out 
but ? acts as a parameter ....

**With bound parameters (safe):**
```python
# Parameterized query with placeholders
CURSOR.execute("SELECT * FROM providers WHERE name = ?", (user_input,))
```
The input is treated as data, not executable SQL code.

### 2. Automatic Type Handling

Bound parameters handle Python data types automatically:
- Strings are properly escaped
- Numbers are converted correctly
- `None` values become SQL `NULL`

### 3. Performance Benefits

SQLite compiles the query plan once and reuses it when parameters change, improving performance for repeated queries.

### 4. Cleaner Code

Instead of manually escaping strings and handling special characters, the database driver handles everything automatically.

### Example in Context

```python
# Instead of this:
CURSOR.execute(f"INSERT INTO providers (name, country) VALUES ('{name}', '{country}')")

# Use this:
CURSOR.execute("INSERT INTO providers (name, country) VALUES (?, ?)", (name, country))
```

### Summary

Bound parameters are essential because they:
- **Prevent SQL injection** - the primary security concern
- **Handle special characters** automatically
- **Improve performance** through query plan reuse
- **Write cleaner, more maintainable code**

This is why modern ORMs and database libraries always use parameterized queries instead of string interpolation.