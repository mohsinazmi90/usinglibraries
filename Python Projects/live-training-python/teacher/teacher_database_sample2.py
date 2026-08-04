import sqlite3

def run_sqlite_demo(db_name):
    # -> USE THIS TO CREATE DB IN MEMORY INSTEAD OF A FILE IN HARDDISK
    # conn = sqlite3.connect(":memory:") 
    
    # 1. CONNECT TO DATABASE (CREATES FILE IF DOESNT EXIST OR USE: 'MEMORY' FOR TEMPORARY -ram DB.)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # CAN USE THIS COMMAND BELOW IN CASE MULTIPLE ENTRIES ARE BEING GENERATED UPON EVERY RUN
    # cursor.execute("DROP TABLE IF EXISTS EMPLOYEES")
    
    # CREATE A TABLE
    print("---- 1. CREATE TABLE ----")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS EMPLOYEES (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            salary REAL NOT NULL
            )
    """)
    conn.commit()
    print("TABLE 'EMPLOYEES' CREATED SUCCESSFULLY.\n")
    
    print("---- 2. INSERT (CREATE) DATA ----")
    # SINGLE INSERT 
    cursor.execute("INSERT INTO EMPLOYEES(name, department, salary) VALUES(?,?,?)", ("Alice", "Engineering", 85000.00))
    
    # BULK INSERT USING LIST
    new_employees = [("Bob", "Marketing", 62000.00), ("Charlie", "Engineering", 92000.0), ("Diana", "HR", 55000.0)]
    cursor.executemany("INSERT INTO EMPLOYEES(name, department, salary) VALUES(?,?,?)", new_employees)
    
    # COMMIT CHANGES INTO DATABASE
    conn.commit()
    print("INSERTED 4 RECORDS SUCCESSFULLY\n")
    
    # READ DATA FROM DATABSE
    print("---- 3. SELECT READ DATA ----")
    
    # FETCH ALL RECORDS
    print("ALL EMPLOYEES:")
    cursor.execute("SELECT * FROM EMPLOYEES")
    
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
    
    # FETCH WITH FILTER/PARAMETER MATCHING
    print("\nENGINEERING DEPARTMENT ONLY.")
    
    # SELECTED ALL ROWS WHERE ENGINEERING IS THE DEPARTMENT
    cursor.execute("SELECT name, salary FROM employees WHERE department = ?", ("Engineering",))
    
    # ENGINEERING ROWS ONLY
    eng_rows = cursor.fetchall()
    for row in eng_rows:
        print(f"Name: {row[0]}, Salary: ${row[1]:.2f}")
    
    # UPDATE DATA IN DATABSE
    print("\n---- 4. UPDATE DATA ----")
    
    # GIVE ALICE A RAISE USING UPDATE SQL QUERY
    cursor.execute("UPDATE EMPLOYEES SET salary = ? WHERE name = ?", (92000.0, "Alice"))
    
    # COMMIT CHANGES TO DATABASE
    conn.commit()
    
    # VERIFY UPDATE
    cursor.execute("SELECT * FROM EMPLOYEES WHERE name is ?", ("Alice",))
    
    updated_alice = cursor.fetchone()
    # print(f"Updated Alice's Salary: ${updated_alice}:.2f\n")
    print(f"Updated Alice's Salary: ${updated_alice[3]:.2f}\n")
    
    
    
    print("---- 5. DELETE DATA ----")
    
    
    # CLOSE
    cursor.close()
    conn.close()
    
run_sqlite_demo("company.db")


