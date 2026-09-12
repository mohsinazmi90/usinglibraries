# Python Object-Oriented Programming

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = (first + "." + last + "@company.com").lower()
    
    def fullname(self):
        return f"{self.last}, {self.first}"

        

employee1 = Employee("Mohsin", "Azmi", 50000)
employee2 = Employee("test", "user", 60000)

print(employee1.fullname())
