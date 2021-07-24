# reference from 
# "SQLite Databases With Python - Full Course"
# https://youtu.be/byHcYRpMgI4

# import sqlite3
import sqlite3

# connect to database
connect01 = sqlite3.connect("student_health.db")

# create a cursor
cursor01 = connect01.cursor()

# query the database - order by weight in DESC 
cursor01.execute("SELECT rowid, * FROM height＿weight ORDER BY weight desc")
iteams = cursor01.fetchall()
for iteam in iteams:
    print(iteam)
# (4, 'Edwin', 'Rice', 171, 100)
# (6, 'Wade', 'Kemp', 186, 93)
# (5, 'Grayson', 'Vance', 178, 89)
# (2, 'Kory', 'Stiles', 183, 84)
# (1, 'Samson', 'North', 197, 78)

# query the database - whose name have on inside
cursor01.execute("SELECT rowid, * FROM height＿weight WHERE first_name LIKE '%on'")
iteams = cursor01.fetchall()
for iteam in iteams:
    print(iteam)
# (1, 'Samson', 'North', 197, 78)
# (5, 'Grayson', 'Vance', 178, 89)

# query the database - whose name have on inside AND taller than 190
cursor01.execute("SELECT rowid, * FROM height＿weight WHERE first_name LIKE '%on' AND height >= 190")
iteams = cursor01.fetchall()
for tieam in iteams:
    print(iteam)
# (5, 'Grayson', 'Vance', 178, 89)

# query the database - whose weight >= 90 OR height <= 180
cursor01.execute("SELECT rowid, * FROM height＿weight WHERE weight > 90 OR height <= 180")
iteams = cursor01.fetchall()
for iteam in iteams:
    print(iteam)
# (4, 'Edwin', 'Rice', 171, 100)
# (5, 'Grayson', 'Vance', 178, 89)
# (6, 'Wade', 'Kemp', 186, 93)

# It can use lots of OR to query the database.
# For example, "SELECT rowid, * FROM sample_table WHERE condition1 OR condition2 OR condition3 OR condition4"

# commit
connect01.commit()

# close
connect01.close()
