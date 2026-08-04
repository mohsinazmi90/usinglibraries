import sqlite3

# ESTABLISH CONNECTION (CREATES THE FILE IF IT DOESNT EXIST)
conn = sqlite3.connect("school.db")

# CREATE A CURSOR OBJECT
cursor = conn.cursor()
print("Database connected successfully.")

# ALWAYS CLOSE THE CONNECTION WHEN DONE
conn.close()

