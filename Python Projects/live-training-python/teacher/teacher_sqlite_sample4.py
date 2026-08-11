import sqlite3

def run_sqlites_demo():
    # CONNECT TO AN IN-MEMORY DATABASE (USE 'COMPANY FOR A PERSISTENT FILE')
    conn = sqlite3.connect(":memory:")
    
    # CONFIGURE CONNECTION TO RETURN ROWS AS DICTIONARY-LIKE OBJECTS
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    try:
        # ENABLE FOREIGN KEY SUPPORT (DISABLED BY DEFAULT IN SQLITE)
        cursor.execute("PRAGMA FOREIGN_KEYS = ON")
        
        # ==============================
        # 1. CREATE TABLES (SCHEMA SETUP)
        # ==============================
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS DEPARTMENTS (
            department_id INTEGER PRIMARY KEY AUTOINCREMENT,
            department_name TEXT NOT NULL UNIQUE
                )
            """)
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS EMPLOYEES (
                employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                hire_date DATE DEFAULT CURRENT_DATE,
                salary REAL CHECK (salary > 0),
                department_id INTEGER, 
                FOREIGN KEY (department_id) REFERENCES DEPARTMENTS (department_id) ON DELETE SET NULL
                )
            """)
        
        print("--- TABLES CREATED SUCCESSFULLY ---")
        
        # ==============================
        # 2. INSERT DATA (CREATE)
        # ==============================
        
        # INSERT SINGLE RECORD
        cursor.execute("INSERT INTO DEPARTMENTS (department_name) VALUES (?)", ("Engineering",))
        
        # INSERT MULTIPLE RECORDS USING EXECUTEMANY
        departments = [("Human Resources",), ("Marketing",), ("Finance",)]
        cursor.executemany("INSERT INTO DEPARTMENTS (department_name) VALUES (?)", departments)
    
        employees = [
                ("Alice", "Smith", "alice.smith@example.com", 85000.00, 1),
                ("Bob", "John", "bob.john@example.com", 62000.00, 2),
                ("Ali", "Shah", "ali.shah@example.com", 92000.00, 1),
                ("Sara", "Khan", "sara.khan@example.com", 75000.00, 3),
                ("Evan", "Wright", "evan.wright@example", 50000.00, 4),
            ]
        cursor.executemany("INSERT INTO EMPLOYEES (first_name, last_name, email, salary, department_id) VALUES (?, ?, ?, ?, ?)", employees)
        
        # UBCERT INSERT OR REPLACE ON CONFLICT
        cursor.execute("""
            INSERT INTO departments (department_id, department_name) 
            VALUES (?, ?) ON CONFLICT(department_id) DO UPDATE SET 
            department_name = excluded.department_name
            """, (4, "Financial Operations"))
        
        print("--- INITIAL DATA INSERTED ---")
        
        # ==============================
        # 3. QUERY DATA (READ)
        # ==============================
        
        # FETCH SINGLE ROW
        cursor.execute("SELECT * FROM EMPLOYEES WHERE employee_id = ?", (1,))
        emp = cursor.fetchone()
        print(f"\nSINGLE RECORD: {emp['first_name']} {emp['last_name']} - ${emp['salary']}")
        
        # JOIN WITH AGGREGATION AND FILTERATION
        cursor.execute("""
                        SELECT 
                        d.department_name, 
                        COUNT (e.employee_id) AS TOTAL_EMPLOYEES,
                        AVG (e.salary) AS AVG_SALARY
                       FROM departments d
                       LEFT JOIN employees e ON d.department_id = e.department_id
                       GROUP BY d.department_name
                       HAVING avg_salary > 60000
                       ORDER BY avg_salary DESC;
                       """)
    except sqlite3.Error as e:
        print(e)
        
if __name__ == "__main__":
    run_sqlites_demo()