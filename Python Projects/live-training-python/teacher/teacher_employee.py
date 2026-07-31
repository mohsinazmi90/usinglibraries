from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name: str, employee_id: int):
        self.name = name
        self.id = employee_id

        # Encapsulation: Salary is protected, Bank_account is private
        self.__salary = 0.0
        self.__bank_account = "Not Set"

        # Abstract Method must be implemented by all subclasses

    @abstractmethod
    def calculate_pay(self) -> float:
        pass

    # Getter for private attribute
    def get_bank_account(self) -> str:
        return self.__bank_account

    # Setter fot private attribute
    def set_bank_account(self, account_number: str):
        if len(account_number) >= 8:
            self.__bank_account = account_number
        else:
            print("Error: Invalid Bank Account Number.")

        # A regular instance method

    def display_details(self):
        print(f"ID: {self.id}, Name: {self.name}, Account: {self.__bank_account}")


# Inheritance: Full time employee inherits from employee
class FullTimeEmployee(Employee):
    def __init__(self, name: str, employee_id: int, monthly_salary: float):
        super().__init__(name, employee_id)  # Call parent constructor

        self._salary = monthly_salary

    # Polymorphism: Overriding the astract method
    def calculate_pay(self) -> float:
        return self._salary


# Inhertance: Part time employee inherits from eomployee
class PartTimeEmployee(Employee):
    def __init__(
        self,
        name: str,
        employee_id: int,
        hourly_rate: float,
        hours_worked: float,
    ):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    # Polymorphism: Overriding the abstract method with different logic
    def calculate_pay(self) -> float:
        return self.hourly_rate * self.hours_worked


# Demonstation of the code
if __name__ == "__main__":
    print("Creating employees")

    # instantiating subclasses
    emp1 = FullTimeEmployee("Alice Smith", 101, 5000.0)
    emp2 = PartTimeEmployee("Bob Johns", 102, 25.0, 80.0)

    # Using encapsulation getters and setters/getters

    emp1.set_bank_account("US123456789")
    emp2.set_bank_account("UK987654321")

    # Creating a list to demonstrate polymorphism

    Employee = [emp1, emp2]
    print("\nProcessing Payroll")

    for emp in Employee:
        emp.display_details()
        # Polymorphism in action: The correct calculate_pay is called automatically based on the object s type
        print(f"Calculated Pay: ${emp.calculate_pay():.2f}")
        print("-" * 30)


# --- Code from Teacher ---
# from abc import ABC, abstractmethod


# # 1. ABSTRACTION: Creating an abstract base class.
# # It acts as a blueprint and cannot be instantiated directly.
# class Employee(ABC):
#     def __init__(self, name: str, employee_id: int):
#         self.name = name
#         self.id = employee_id
#         # 2. ENCAPSULATION: _salary is protected, __bank_account is private
#         self._salary = 0.0
#         self.__bank_account = "Not Set"

#     # Abstract method: Must be implemented by all subclasses
#     @abstractmethod
#     def calculate_pay(self) -> float:
#         pass

#     # Getter for private attribute
#     def get_bank_account(self) -> str:
#         return self.__bank_account

#     # Setter for private attribute
#     def set_bank_account(self, account_number: str):
#         if len(account_number) >= 8:
#             self.__bank_account = account_number
#         else:
#             print("Error: Invalid bank account number.")

#     # A regular instance method
#     def display_details(self):
#         print(f"ID: {self.id} | Name: {self.name} | Account: {self.__bank_account}")


# # 3. INHERITANCE: FullTimeEmployee inherits from Employee
# class FullTimeEmployee(Employee):
#     def __init__(self, name: str, employee_id: int, monthly_salary: float):
#         super().__init__(name, employee_id)  # Call parent constructor
#         self._salary = monthly_salary

#     # 4. POLYMORPHISM: Overriding the abstract method
#     def calculate_pay(self) -> float:
#         return self._salary


# # INHERITANCE: PartTimeEmployee inherits from Employee
# class PartTimeEmployee(Employee):
#     def __init__(
#         self, name: str, employee_id: int, hourly_rate: float, hours_worked: float
#     ):
#         super().__init__(name, employee_id)
#         self.hourly_rate = hourly_rate
#         self.hours_worked = hours_worked

#     # POLYMORPHISM: Overriding the abstract method with different logic
#     def calculate_pay(self) -> float:
#         return self.hourly_rate * self.hours_worked


# # --- Demonstration of the Code ---
# if __name__ == "__main__":
#     print("--- Creating Employees ---")
#     # Instantiating subclasses
#     emp1 = FullTimeEmployee("Alice Smith", 101, 5000.0)
#     emp2 = PartTimeEmployee("Bob Jones", 102, 25.0, 80.0)

#     # Using Encapsulation (Setters/Getters)
#     emp1.set_bank_account("US123456789")
#     emp2.set_bank_account("UK987654321")

#     # Creating a list to demonstrate Polymorphism
#     employees = [emp1, emp2]

#     print("\n--- Processing Payroll ---")
#     for emp in employees:
#         emp.display_details()
#         # Polymorphism in action: The correct calculate_pay() is called automatically based on the object type
#         print(f"Calculated Pay: ${emp.calculate_pay():.2f}")
#         print("-" * 30)
