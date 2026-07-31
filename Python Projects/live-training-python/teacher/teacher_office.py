class Employee:
    """
    Represents an individual employee in the office.
    """

    # --- 1. THE CONSTRUCTOR METHOD ---
    def __init__(self, emp_id: str, emp_name: str, role: str, salary: float):

        # --- INSTANCE, VARIABLE(ATTRIBUTES) ---
        # The store the unique state of each individual employee
        self.emp_id = emp_id  # Attribute: Unique String ID
        self.emp_name = emp_name  # Attribute: String Name
        self.role = role  # Attribute: String Job Title
        self.salary = salary  # Attribute: Numeric Salary Value
        self.performance_score = 5.0  # Attribute: Default Float Rating

    # --- 2. INSTANCE METHOD (Action) ---
    def give_raise(self, amount):
        """
        Modifies the salary attribute of this employee
        """

        # 'Amount' IS A LOCAL VARIABLE (Only Exists Inside This Method)
        if amount > 0:
            self.salary += amount  # Accessing and changing the 'Salary' attribute
            return True
        return False

    # --- 3. INSTANCE METHOD (Action) ---
    def update_performance(self, new_score):
        """
        Modifies the performance_score of this employee
        """

        # 'New_Score' IS A LOCAL VARIABLE
        if 0.0 <= new_score <= 10.0:
            self.performance_score = new_score  # Modifying attribute
            return True
        return False


class Office:
    """
    MANAGES THE DATA FOR ALL EMPLOYEES AND BUDGET DETAILS.
    """

    # --- 1. THE CONSTRUCTOR METHOD ---
    def __init__(self, office_name: str):
        # -------------------------------
        # INSTANCE VARIABLES (ATTRIBUTES)
        # -------------------------------
        self.office_name = office_name  # ATTRIBUTE: STRING OFFICE_NAME
        self.employees = {}  # ATTRIBUTE: DICTIONARY

    ### --- 2. INSTANCE METHOD (ACTION) ---
    def hire_employee(self, employee):
        """
        ADD AN EMPLOYEE OBJECT TO THE EMPLOYEE DIRECTORY.
        """

        # 'EMPLOYEE' IS A LOCAL VARIABLE CONTAINING AN EMPLOYEE OBJECT
        if employee.emp_id not in self.employees:
            self.employees[employee.emp_id] = employee  # MODIFYING DICTIONARY ATTRIBUTE
            print(f"Hired: {employee.emp_name} as a {employee.role}.")
        else:
            print(f"Error: {employee.emp_id} already exists!")

    # --- 3. INSTANCE METHOD (CALCULATION) ---
    def calculate_monthly_payroll(self):
        """
        CALCULATES PAYROLL USING EMPLOYEE ATTRIBUTE.
        """

        # 'TOTAL_ANNUAL_SALARY' IS A LOCAL VARIABLE
        total_annual_salary = sum(emp.salary for emp in self.employees.values())
        return round(total_annual_salary / 12, 2)  # RETURNS ROUNDED TOTAL ANNUAL SALARY

    # --- 4. OUTPUT ---
    def display_roster(self):
        """
        PRINTS OUT THE CURRENT ROSTER INFORMATION.
        """

        print(f"\n--- {self.office_name} Staff ---")

        if not self.employees:
            print("No Employees Currently Hired.")
            return

        for emp in self.employees.values():
            # READING ATTRIBURES FROM EACH EMPLOYEE OBJECT

            print(
                f"ID: {emp.emp_id}, Name: {emp.emp_name}, Role: {emp.role}, Salary: ${emp.salary}, Rating: {emp.performance_score}/10"
            )


# ===================
# GLOBAL VARIABLE (VARIABLES CREATED OUTSIDE CLASSES IN THE MAIN PROGRAM)
# ===================

tech_hub = Office("Silicone Lahore Tech Hub")  # GLOBAL OBJECT VARIABLE

# GLOBAL OBJECT VARIABLE POINTING TO THE EMPLOYEE TO EMPLOYEES INSTANCES
emp1 = Employee("E101", "Aisha Khan", "Software Engineer", 96000.00)
emp2 = Employee("E102", "Zain Ali", "Product Manager", 110000.00)

tech_hub.hire_employee(emp1)
tech_hub.hire_employee(emp2)
emp1.update_performance(8.0)
tech_hub.display_roster()
