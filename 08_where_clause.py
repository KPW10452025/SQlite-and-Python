# reference from 
# "SQLite Databases With Python - Full Course"
# https://youtu.be/byHcYRpMgI4

# import sqlite3
import sqlite3

# Connect to database
connect01 = sqlite3.connect("student_health.db")

# Create a cursor
cursor01 = connect01.cursor()

# Query the database with WHERE and LIKE

# Search someone with Rory in the first name
cursor01.execute("SELECT * FROM height＿weight WHERE first_name = 'Rory'")
print("Search someone with Rory in the first name.")
print(cursor01.fetchall())
# Search someone with Rory in the first name.
# [('Rory', 'Norris', 185, 103)]

# Search someone height over 180 
cursor01.execute("SELECT * FROM height＿weight WHERE height >= 180")
iteams01 = cursor01.fetchall()
print("Search someone height over 180.")
for iteam in iteams01:
    print(iteam)
# Search someone height over 180.
# ('Samson', 'North', 197, 76)
# ('Kory', 'Stiles', 183, 84)
# ('Rory', 'Norris', 185, 103)
# ('Wade', 'Kemp', 186, 93)

# Search someone weight over 90
cursor01.execute("SELECT rowid, * FROM height＿weight WHERE weight >= 90")
iteams02 = cursor01.fetchall()
print("Search someone weight over 90.")
for iteam in iteams02:
    print(iteam)
# Search someone weight over 90.
# (3, 'Rory', 'Norris', 185, 103)
# (6, 'Wade', 'Kemp', 186, 93)

# Search someone whose name have N
cursor01.execute("SELECT rowid, * FROM height＿weight WHERE  second_name LIKE 'N%'")
iteams03 = cursor01.fetchall()
print("Search someone whose name have N.")
for iteam in iteams03:
    print(iteam)
# Search someone whose name have N.
# (1, 'Samson', 'North', 197, 76)
# (3, 'Rory', 'Norris', 185, 103)

# Search someone whose name have Z
cursor01.execute("SELECT rowid, * FROM height＿weight WHERE  second_name LIKE 'Z%'")
iteams04 = cursor01.fetchall()
print("Search someone whose name have Z.")
if iteams04 == []:
    print("No one has Z in their name.")
else:
    for iteam in iteams04:
        print(iteam)
# Search someone whose name have Z.
# No one has Z in their name.

connect01.commit()
connect01.close()
