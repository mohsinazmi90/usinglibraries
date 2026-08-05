import sqlite3

def run_sqlite_demo(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # CREATE A NEW TABE EVERY TIME SO IT DOESNT ADD SAME ROWS
    cursor.execute("DROP TABLE IF EXISTS PETSHOP")
    
    # CREATE DATABASE TABLE
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS PETSHOP (
                       tag INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       type TEXT NOT NULL
                   )
                   """)
    conn.commit()
    
    # INSERT INTO DB
    cursor.execute("INSERT INTO PETSHOP(name, type) VALUES(?,?)", ("Twix", "Cat"))
    conn.commit()
    
    # ADD MANY PETS INTO DATABASE USING 'EXECUTEMANY'
    new_pets = [("Max", "Dog"), ("Luis", "Fish"), ("Simba", "Cat")]
    
    cursor.executemany("INSERT INTO PETSHOP(name, type) VALUES(?,?)", new_pets)
    conn.commit()
    
    # READ DATA FROM DATABASE
    print("\n----- ALL PETS -----")
    cursor.execute("SELECT * FROM petshop")
    
    pets_in_db = cursor.fetchall()
    
    for pets in pets_in_db:
        print(pets)
    
    # PRINT CATS ONLY
    print("\n----- CATS ONLY -----")
    cursor.execute("SELECT name FROM petshop WHERE type = ?", ("Cat",))
    
    cats_in_db = cursor.fetchall()
    
    for cat in cats_in_db:
        print(f"Name: {cat[0]}")
        
    # UPDATE DATABSE
    cursor.execute("UPDATE petshop SET type = ? WHERE name = ?", ("Chimp", "Luis"))
    conn.commit()
    
    # VERIFY UPDATE
    cursor.execute("SELECT * FROM petshop WHERE name = ?", ("Luis",))
    updated_luis = cursor.fetchone()
    
    print(f"\n----- UPDATED 'TYPE' FOR LUIS: '{updated_luis[2].upper()}' -----")
    
    # CLOSE CONNECTIONS (CURSOR AND CONN)
    cursor.close()
    conn.close()
    
run_sqlite_demo("petshop_sample.db")