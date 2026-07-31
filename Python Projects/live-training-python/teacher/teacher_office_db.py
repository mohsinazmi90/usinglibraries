class Employee:
    """
    Represents an employee and holds their data.
    """

    def __init__(self, emp_id, name, role, salary):
        self.emp_id = emp_id
        self.name = name
        self.role = role
        self.salary = int(salary)  # Ensure salary is stored as integer

    def to_csv_line(self):
        """
        Converts employee attribute into a single a ',' seperated line.
        """
        return f"{self.emp_id}, {self.name}, {self.role}, {self.salary}\n"


class OfficeDatabase:
    """
    Manages employee object and presents to a text file.
    """

    # CONSTRUCTOR: sets up the file name we will load from
    def __init__(self, db_filename="office_data.txt"):
        self.db_filename = db_filename

        self.employees = {}  # Dictionary to store emp_id: Employee_Object

    # METHOD: Add an employee to runtime dictionary
    def hire_employee(self, employee):
        self.employees[employee.emp_id] = employee
        print(f"Hired: {employee.name}, {employee.role}")

    # METHOD: File Write. Save dictionary data to a file
    def save_database(self):
        """
        Opens file in write mode ('w') and saves all employee data.
        """

        with open(self.db_filename, "w") as file:
            for emp in self.employees.values():  # Write each employee as a csv line
                file.write(emp.to_csv_line())

        print(f"\nSuccess: Database successfully to {self.db_filename}")

    # METHOD: File read. Loads data from file and op
    def load_databse(self):
        """
        Opens file in read mode('r') and parses employee objects.
        """

        try:
            with open(self.db_filename, "r") as file:
                self.employees.clear()  # Clear current memory before loading
                for line in file:  # Clean the line and split by commas
                    parts = line.strip().split(",")
                    if len(parts) == 4:
                        emp_id, name, role, salary = parts  # OOP instancing!

                    restore_emp = Employee(emp_id, name, role, salary)
                    self.employees[emp_id] = restore_emp
                print(
                    f"Success: Database Loaded. Restored {len(self.employees)} employees."
                )
        except FileNotFoundError:
            print("/nNotice: No Data Found. Empty Roster")

    # METHOD: Prints out the active roster
    def display_roster(self):
        print("\n--- Active Staff Roster ---")
        if not self.employees:
            print("No employees loaded in memory.")
            return

        for emp in self.employees.values():
            print(
                f"ID: {emp.emp_id}, Name: {emp.name}, Role: {emp.role}, Salary: 4{emp.salary}"
            )


# =============================
# Running the application
# =============================

# Step 1. Initialize the databse system
db = OfficeDatabase()

# Step 2. Try to load existing data. (Will say empty on first run.)
db.load_databse()

# Step 3. Hire some employees if databse is empty
if not db.employees:
    print("\n --- Populate Database ---")

emp1 = Employee("E101", "Aisha Khan", "Software Engineer", "5000")
emp2 = Employee("E102", "Zain Ali", "Project Manager", "11000")

db.hire_employee(emp1)
db.hire_employee(emp2)

db.save_database()

# Step 4: Show active roster
db.display_roster()


# class Employee:
#     """Represents an employee and holds their data."""
#     def __init__(self, emp_id, name, role, salary):
#         self.emp_id = emp_id
#         self.name = name
#         self.role = role
#         self.salary = int(salary)  # Ensure salary is stored as an integer

#     def to_csv_line(self):
#         """Converts employee attributes into a single comma-separated string line."""
#         return f"{self.emp_id},{self.name},{self.role},{self.salary}\n"


# class OfficeDatabase:
#     """Manages employee objects and persists them to a text file."""

#     # CONSTRUCTOR: Sets up the filename we will save to/load from
#     def __init__(self, db_filename="office_data.txt"):
#         self.db_filename = db_filename
#         self.employees = {}  # Dictionary to store {emp_id: Employee_Object}

#     # METHOD: Adds an employee to our runtime dictionary
#     def hire_employee(self, employee):
#         self.employees[employee.emp_id] = employee
#         print(f"Hired: {employee.name} ({employee.role})")

#     # METHOD + FILE WRITE: Saves the dictionary data to a file
#     def save_database(self):
#         """Opens file in write mode ('w') and saves all employee data."""
#         with open(self.db_filename, "w") as file:
#             for emp in self.employees.values():
#                 # Write each employee as a CSV line
#                 file.write(emp.to_csv_line())
#         print(f"\n[Success] Database successfully saved to '{self.db_filename}'.")

#     # METHOD + FILE READ: Loads data from a file and rebuilds OOP objects
#     def load_database(self):
#         """Opens file in read mode ('r'), parses lines, and spawns Employee objects."""
#         try:
#             with open(self.db_filename, "r") as file:
#                 self.employees.clear()  # Clear current memory before loading

#                 for line in file:
#                     # Clean the line and split by commas
#                     parts = line.strip().split(",")
#                     if len(parts) == 4:
#                         emp_id, name, role, salary = parts
#                         # RECREATE the Employee object (OOP instancing!)
#                         restored_emp = Employee(emp_id, name, role, salary)
#                         # Add it back to our active dictionary
#                         self.employees[emp_id] = restored_emp

#             print(f"[Success] Database loaded. Restored {len(self.employees)} employees.")
#         except FileNotFoundError:
#             print("\n[Notice] No database file found. Starting with an empty roster.")

#     # METHOD: Prints out the active roster
#     def display_roster(self):
#         print("\n--- Active Staff Roster ---")
#         if not self.employees:
#             print("No employees loaded in memory.")
#             return
#         for emp in self.employees.values():
#             print(f"ID: {emp.emp_id} | Name: {emp.name} | Role: {emp.role} | Salary: ${emp.salary:,}")


# # ====================================================================
# # RUNNING THE APPLICATION
# # ====================================================================

# # Step 1: Initialize the database system
# db = OfficeDatabase()

# # Step 2: Try to load existing data (will say empty on the first run)
# db.load_database()

# # Step 3: Hire some employees (if database is empty)
# if not db.employees:
#     print("\n--- Populate Database ---")
#     emp1 = Employee("E101", "Ayesha Khan", "Software Engineer", 95000)
#     emp2 = Employee("E102", "Zain Ali", "Product Manager", 110000)

#     db.hire_employee(emp1)
#     db.hire_employee(emp2)

#     # Save them to the text file!
#     db.save_database()

# # Step 4: Show the active roster
# db.display_roster()
