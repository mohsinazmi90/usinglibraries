# 11. `Student` class banao jisme:
# * name
# * marks
# * grade calculate karne ka method

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grades(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        else:
            return 'F'
    
    
student1 = Student("John", 85)
student2 = Student("Alice", 92)
student3 = Student("Bob", 75)

for student in [student1, student2, student3]:
    print(f"Student: {student.name}, Marks: {student.marks}, Grade: {student.calculate_grades()}")

