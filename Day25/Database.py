    #2. Creating a DataBase
"""    
import sqlite3
connection = sqlite3.connect("Day25/students.db")
print("Database created successfully!")
connection.close()
"""

    #3. Creating a Table
    
import sqlite3
connection = sqlite3.connect("Day25/student.db")
cursor = connection.cursor()
cursor.execute("""
               Create table if not exists students(
                   id integer primary key autoincrement,
                   name text,
                   cgpa real
                   )"""
)
connection.commit()
connection.close()


    #4. Inserting Data
  
import sqlite3
connection = sqlite3.connect("Day25/student.db")
cursor = connection.cursor()
cursor.executemany(
    "insert into students(name,cgpa) values(?,?)",
    [("Sai",9.2),
    ("Manikanta",8.8)]
)
connection.commit()
connection.close()



    #5. Reading Data

import sqlite3
connection = sqlite3.connect("Day25/student.db")
cursor = connection.cursor()
cursor.execute("select * from students")
rows = cursor.fetchall()
for row in rows:
    print(row)
connection.commit()

    #6. Updating and deleting Data
    
    #Update:   
cursor.execute(
    "Update students set cgpa = ? where name = ?",
    (9.5,"Sai")
)
connection.commit()

    #Delete
cursor.execute(
    "DELETE FROM students WHERE name = ?",
    ("Sai",)
)
connection.commit()
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("After deletion:")
for row in rows:
    print(row)
    
cursor.execute("DELETE FROM students WHERE name = ?", ("Sai",))
connection.commit()

print("Deleted rows:", cursor.rowcount)

cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

connection.close()
connection.close()

