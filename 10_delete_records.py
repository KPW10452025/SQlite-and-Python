# reference from 
# "SQLite Databases With Python - Full Course"
# https://youtu.be/byHcYRpMgI4

# import sqlite3
import sqlite3

# Connect to database
connect01 = sqlite3.connect("student_health.db")

# Create a cursor
cursor01 = connect01.cursor()

# Query the database
cursor01.execute("SELECT rowid, * FROM height＿weight")
iteams01 = cursor01.fetchall()
for iteam in iteams01:
    print(iteam)
# (1, 'Samson', 'North', 197, 78)
# (2, 'Kory', 'Stiles', 183, 84)
# (3, 'Rory', 'Norris', 185, 103)
# (4, 'Edwin', 'Rice', 171, 100)
# (5, 'Grayson', 'Vance', 178, 89)
# (6, 'Wade', 'Kemp', 186, 93)

# Delete record
cursor01.execute("DELETE from height＿weight WHERE rowid = 3")


cursor01.execute("SELECT rowid, * FROM height＿weight")
iteams02 = cursor01.fetchall()
for iteam in iteams02:
    print(iteam)
# (1, 'Samson', 'North', 197, 78)
# (2, 'Kory', 'Stiles', 183, 84)
# (4, 'Edwin', 'Rice', 171, 100)
# (5, 'Grayson', 'Vance', 178, 89)
# (6, 'Wade', 'Kemp', 186, 93)

connect01.commit()
connect01.close()
