# reference from 
# "SQLite Databases With Python - Full Course"
# https://youtu.be/byHcYRpMgI4

# import sqlite3
import sqlite3

# connect to database 
connect = sqlite3.connect("student_health.db")

# create a cursor
cursor = connect.cursor()

# query the database - LIMIT
# use LIMIT to limit the number of output
cursor.execute("SELECT rowid, * FROM height＿weight LIMIT 3")
iteams = cursor.fetchall()
for iteam in iteams:
    print(iteam)
# (1, 'Samson', 'North', 197, 78)
# (2, 'Kory', 'Stiles', 183, 84)
# (4, 'Edwin', 'Rice', 171, 100)

cursor.execute("SELECT rowid, * FROM height＿weight WHERE height > 170 LIMIT 2")
iteams = cursor.fetchall()
for iteam in iteams:
    print(iteam)
# (1, 'Samson', 'North', 197, 78)
# (2, 'Kory', 'Stiles', 183, 84)

# without LIMIT there will have 5 result output. 
# with LIMIT 2, it just show 2 result output.

# commit
connect.commit()

# close
connect.close()
