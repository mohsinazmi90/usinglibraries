# 11. Function for number factorial calculate.
# 12. List mein se duplicate values remove karo.
# 13. Dictionary mein students aur marks store karke highest scorer ﬁnd karo.
# 14. CSV ﬁle create karke 5 students ka data save karo.
# 15. JSON ﬁle mein student information write/read karo.

# 11. Function for number factorial calculate.
def factorial(n):  
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
fact_num = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {fact_num} is: {factorial(fact_num)}")
    
# 12. List and us mein se duplicate values remove karo.
my_list = [1, 2, 3, 2, 4, 1, 5]

def remove_duplicates(input_list):
    return list(set(input_list))

removed_duplicates = remove_duplicates(my_list)
print("List after removing duplicates using function:", removed_duplicates)


# 13. Dictionary mein students aur marks store karke highest scorer ﬁnd karo.
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eva": 88
}
highest_scorer = max(students, key=students.get)
print(f"The highest scorer is {highest_scorer} with a score of {students[highest_scorer]}.")

# 14. CSV ﬁle create karke 5 students ka data save karo.
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Score"])
    for name, score in students.items():
        writer.writerow([name, score])
        
# 15. JSON ﬁle mein student information write/read karo.
import json

student_info = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}   

with open("student_info.json", "w") as json_file:
    json.dump(student_info, json_file)  
    
with open("student_info.json", "r") as json_file:
    data = json.load(json_file)
    print("Student Information from JSON file:", data)
    



