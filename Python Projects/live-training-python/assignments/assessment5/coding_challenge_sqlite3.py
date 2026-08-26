# 14. SQLite3 database banao jisme:
# * Student ID
# * Name
# * Marks
# * Grade
# aur *insert, update, delete, search* operations perform karo.

import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Drop the table if it already exists
cursor.execute("DROP TABLE IF EXISTS PETSHOP")

# Create a table for students
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    marks INTEGER NOT NULL,
                    grade TEXT NOT NULL)''')


# Function to calculate grade based on marks
def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'
    
# Function to insert a new student record
def insert_student(name, marks):
    grade = calculate_grade(marks)
    cursor.execute("INSERT INTO students (name, marks, grade) VALUES (?, ?, ?)", (name, marks, grade))
    conn.commit()
    print(f"Inserted student: {name}, Marks: {marks}, Grade: {grade}")
    
# Function to update an existing student record
def update_student(student_id, name=None, marks=None):
    if name is not None:
        cursor.execute("UPDATE students SET name = ? WHERE student_id = ?", (name, student_id))
    if marks is not None:
        grade = calculate_grade(marks)
        cursor.execute("UPDATE students SET marks = ?, grade = ? WHERE student_id = ?", (marks, grade, student_id))
    conn.commit()
    print(f"\nUpdated student ID: {student_id}")
    
# Function to delete a student record
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
    conn.commit()
    print(f"Deleted student ID: {student_id}")
    
# Function to search for a student record
def search_student(student_id):
    cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
    student = cursor.fetchone()
    if student:
        print(f"Student ID: {student[0]}, Name: {student[1]}, Marks: {student[2]}, Grade: {student[3]}")
    else:
        print(f"\nNo student found with ID: {student_id}")
        
# Example usage:
insert_student("John Doe", 85)
insert_student("Alice Smith", 92)
insert_student("Bob Johnson", 75)
insert_student("Charlie Brown", 60)

search_student(1)
update_student(1, marks=88)
search_student(1)
delete_student(2)

# Close the database connection
cursor.close()
conn.close()