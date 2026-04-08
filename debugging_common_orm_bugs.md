# Common ORM Bugs and How to Fix Them

This guide covers frequent mistakes made when working with ORM relationships.

---

## Bug 1: Wrong `instance_from_db` Class

### The Problem
```python
def find_department(self):
    from department import Department
    sql = '''
        SELECT * FROM departments
        WHERE id = ?
    '''
    row = CURSOR.execute(sql, (self.department_id,)).fetchone()
    return self.instance_from_db(row)  # ❌ WRONG
```

**Error:** `IndexError: tuple index out of range`

### Why It Happens
- You're querying the `departments` table (3 columns: id, name, location)
- But calling `self.instance_from_db()` which expects an `Employee` row (4 columns: id, name, job_title, department_id)
- When accessing `row[3]` on a 3-column row → IndexError

### The Fix
```python
return Department.instance_from_db(row) if row else None
```

Use the class whose table you queried, not `self`.

---

## Bug 2: Typo in Attribute Name

### The Problem
Inside `Employee.instance_from_db()`:
```python
employee.depatment_id = row[3]  # ❌ missing 'r'
```

Should be:
```python
employee.department_id = row[3]
```

### Why It Happens
Simple typo - `depatment_id` instead of `department_id`. Python won't catch this at compile time because it's a valid attribute name (it creates a new attribute), but the attribute won't match the actual class attribute.

---

## Bug 3: SQL Syntax Error (Trailing Comma)

### The Problem
```python
sql = '''
SELECT * FROM employees,
WHERE department_id = ?
;
'''
```

**Error:** SQL syntax error or unexpected results

### Why It Happens
- `FROM employees,` - the comma implies another table (JOIN) but nothing follows
- The semicolon before the closing backticks is unnecessary but not harmful

### The Fix
```python
sql = '''
SELECT * FROM employees
WHERE department_id = ?
'''
```

---

## When to Use `self` vs `cls` 

### Quick Rule
| Method Type | Use | Example |
|------------|-----|---------|
| Instance method | `self` | `find_department()` - operates on one specific employee |
| Class method | `cls` | `get_all()`, `find_by_id()` - operates on all objects of the type |

### More Detailed

**Use `self` when:**
- You need a specific instance's data (e.g., `self.id`, `self.department_id`)
- The method operates on one particular object
- Example: `employee.find_department()` - "find the department THIS employee belongs to"

**Use `cls` when:**
- You're creating a new instance from a database row
- The method operates on the entire collection, not one object
- Example: `Employee.instance_from_db(row)` - "create an Employee from a row"
- Example: `Department.find_by_id(1)` - "find a department by its id"

### The Memory Trick
> **"If the method needs to know WHO it is, use `self`. If it acts on the TYPE, use `cls`."**

- `self.instance_from_db()` → "who am I creating?" → ❌ Wrong (confused about the type)
- `Employee.instance_from_db()` → "create an Employee from this row" → ✅ Correct
- `department.employee_list()` → "list employees for THIS department" → ✅ Correct (uses `self` only implicitly for calling Employee's class method)

---

## Summary Checklist

- [ ] Querying `departments` table? → Use `Department.instance_from_db()`
- [ ] Querying `employees` table? → Use `Employee.instance_from_db()`
- [ ] Typing attribute names? Double-check spelling
- [ ] SQL has no trailing comma after table name
- [ ] Tuple parameter needs trailing comma only for one element: `(value,)`