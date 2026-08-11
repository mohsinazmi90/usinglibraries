import sqlite3

def run_sqlite_demo():
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    print("--- 1. RESET AND CREATE TABLE ---")
    # Drop existing table to prevent duplicates from previous runs
    cursor.execute("DROP TABLE IF EXISTS employees")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            salary REAL NOT NULL
        )
    """)
    conn.commit()
    print("Table 'employees' reset and created successfully.\n")

    print("--- 2. INSERT (CREATE) DATA ---")
    cursor.execute(
        "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
        ("Alice", "Engineering", 85000.0)
    )

    new_employees = [
        ("Bob", "Marketing", 62000.0),
        ("Charlie", "Engineering", 90000.0),
        ("Diana", "HR", 55000.0)
    ]
    cursor.executemany(
        "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
        new_employees
    )
    conn.commit()
    print("Inserted 4 records successfully.\n")

    print("--- 3. SELECT (READ) DATA ---")
    print("All Employees:")
    cursor.execute("SELECT * FROM employees")
    for row in cursor.fetchall():
        print(row)

    print("\nEngineering Department Only:")
    cursor.execute("SELECT name, salary FROM employees WHERE department = ?", ("Engineering",))
    for row in cursor.fetchall():
        print(f"Name: {row[0]}, Salary: ${row[1]:,.2f}")
    print()

    print("--- 4. UPDATE DATA ---")
    cursor.execute(
        "UPDATE employees SET salary = ? WHERE name = ?",
        (92000.0, "Alice")
    )
    conn.commit()

    cursor.execute("SELECT name, salary FROM employees WHERE name = ?", ("Alice",))
    print(f"Updated Alice's Record: {cursor.fetchone()}\n")

    print("--- 5. DELETE DATA ---")
    cursor.execute("DELETE FROM employees WHERE name = ?", ("Bob",))
    conn.commit()
    print("Deleted 'Bob' from the database.\n")

    print("--- 6. VERIFY FINAL DATABASE STATE ---")
    cursor.execute("SELECT * FROM employees")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    run_sqlite_demo()