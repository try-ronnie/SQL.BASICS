## Why `cls` is Referred to as "Table" and `self` as "Row"

In this ORM (Object-Relational Mapping) pattern used in [`provider.py`](LEARNING.SQL.OPERATIONS/ example.ORM.5/lib/provider.py), the terminology reflects the mapping between Python objects and database structures:

### `cls` (Class) = Table
- The **class itself** represents a **database table**
- Class methods (decorated with `@classmethod`) operate on the table level
- When you call `Provider.create()`, `cls` refers to the `Provider` table in the database
- Operations like creating tables, inserting records, or querying all records use `cls` because they deal with the entire table

### `self` (Instance) = Row
- Each **instance** of the class represents a **single row** in the database table
- Instance attributes (`self.name`, `self.country`, etc.) map to **column values**
- When you create a `Provider` object, you're essentially creating a database row with specific values

### Example from the Code

```python
class Provider:
    def __init__(self, name:str, country:str, capacity:int, price_charge:int, id=None):
        self.name = name      # → 'name' column value for a specific row
        self.country = country  # → 'country' column value for a specific row
        self.capacity = capacity  # → 'capacity' column value for a specific row
        self.price_charge = price_charge  # → 'price_charge' column value
```

- **One Provider object** = **One row** in the `providers` table
- **Provider class** = **The entire table structure**

This pattern allows you to work with Python objects instead of writing raw SQL, making database interactions more Pythonic and object-oriented.