# 16–20. Short coding:
# * Even/odd checker
# * Largest of two numbers
# * Sum of 1–10
# * Simple calculator
# * Student grade calculator

# * Even/odd checker
x = int(input("Enter a number: "))
if x % 2 == 0:
    print(f"{x} is even.")
else:
    print(f"{x} is odd.")    
    
# * Largest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print(f"{a} is larger than {b}.")
elif b > a:
    print(f"{b} is larger than {a}.")
else:
    print(f"{a} and {b} are equal.")   

# * Sum of 1–10
sum_1_to_10 = sum(range(1, 11))
print(f"The sum of numbers from 1 to 10 is: {sum_1_to_10}")

# * Simple calculator
def simple_calculator():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero."
    else:
        return "Error: Invalid operator."

    return f"The result of {num1} {operator} {num2} is: {result}"

print(simple_calculator())

# * Student grade calculator
def student_grade_calculator():
    print("Student Grade Calculator")
    score = float(input("Enter the student's score (0-100): "))

    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    return f"The student's grade is: {grade}"

print(student_grade_calculator())

