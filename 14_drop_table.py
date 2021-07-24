# reference from 
# "SQLite Databases With Python - Full Course"
# https://youtu.be/byHcYRpMgI4

# import sqlite3
import sqlite3

# connect to database
connect = sqlite3.connect("student_health.db")

# create a cursor
cursor = connect.cursor()

# query the database
cursor.execute("SELECT rowid, * FROM height＿weight")
iteams = cursor.fetchall()
for iteam in iteams:
    print(iteam)
# (1, 'Samson', 'North', 197, 78)
# (2, 'Kory', 'Stiles', 183, 84)
# (4, 'Edwin', 'Rice', 171, 100)
# (5, 'Grayson', 'Vance', 178, 89)
# (6, 'Wade', 'Kemp', 186, 93)

# Create another table named create_and_delete
cursor.execute("""CREATE TABLE create_and_delete(
    first_name text,
    second_name text,
    email text
)""")

cursor.execute("SELECT rowid, * FROM create_and_delete")
iteams = cursor.fetchall()
print(iteams)
# []

# use DROP TABLE to delete table
cursor.execute("DROP TABLE create_and_delete")

connect.commit()
connect.close()
