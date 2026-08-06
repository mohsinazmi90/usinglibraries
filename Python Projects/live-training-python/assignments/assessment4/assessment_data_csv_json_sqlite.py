# Part D: Advanced Programming (30 Marks)
#  1.⁠ ⁠Create a CSV file containing student records and read all records.
#  2.⁠ ⁠Create a JSON file for employee information and load the data back into Python.
#  3.⁠ ⁠Create an SQLite3 database named ⁠ students.db ⁠, create a table, insert three records, 
# and display them using SELECT 

import csv
import json
import sqlite3
import pandas as pd
from datetime import datetime


def to_csv_and_json(list_of_people: list):
    df = pd.DataFrame(list_of_people)
    df.to_csv("output_pandas.csv", index=False)
    df.to_json("output_pandas.json", index=False, indent=4, orient="records")
    
data = {
    "Name": [
        "Alice",
        "Bob",
        "Charlie",
    ],
    "Age": [
        28,
        34,
        22,
    ],
    "City": [
        "New York",
        "San Francisco",
        "France",
    ],
}

# USE METHOD ABOVE TO CREATE CSV AND JSON FILES WITH PANDAS
to_csv_and_json(data)

# READ FROM CSV AND JSON FILES
def read_csv_file(filename):
    with open(filename, "r") as f:
        csv_file = csv.reader(f)
        for row in csv_file:
            print(row)

def read_json_file(filename):
    with open(filename, "r") as f:
        js = json.load(f)
        for person in js:
            print(f"Name: {person['Name']} | Age: {person['Age']} | City: {person['City']}")
        
 
# PRINT CSV AND JSON CONTENTS TO CONSOLE
print("\n------ CSV FILE CONTENTS ------")   
read_csv_file("output_pandas.csv")

print("\n------ JSON FILE CONTENTS ------")
read_json_file("output_pandas.json")

# CREATE SQLITE DATABSE
conn = sqlite3.connect("output_database.db")
cursor = conn.cursor()

# CLEAR OUT DATABASE
cursor.execute("DROP TABLE IF EXISTS EMPLOYEES")

# CREATE THE TABLE
cursor.execute("""
               CREATE TABLE IF NOT EXISTS EMPLOYEES (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   city TEXT NOT NULL,
                   salary REAL NOT NULL
               )
               """)
conn.commit()

# INSERT VALUES INTO DATABASE
cursor.execute("INSERT INTO EMPLOYEES (name, city, salary) VALUES (?,?,?)", ("Alice", "New York", 92000.0))
conn.commit()

# INSERT MANY VALUES INTO DATABSE
new_employees = [("Bob", "San Francisco", 86000.0), ("Charlie", "Paris", 43000.0), ("Peter", "Boston", 105000.0)]
cursor.executemany("INSERT INTO EMPLOYEES (name, city, salary) VALUES (?,?,?)", new_employees)
conn.commit()

# UPDATE DATABASE VALUES
cursor.execute("UPDATE EMPLOYEES SET salary = ? WHERE name = ?", (122000.5, "Alice"))

# DISPLAY THE DATABASE RECORDS TO CONSOLE
print("\n------ DATABASE FILE CONTENTS ------")   
cursor.execute("SELECT * FROM EMPLOYEES")
rows = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]} | Name: {row[1]} | City: {row[2]} | Salary: $ {row[3]:.2f}")
    
# CLOSE CONNECTION AND CURSOR
cursor.close()
conn.close()