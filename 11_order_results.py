# reference from 
# "SQLite Databases With Python - Full Course"
# https://youtu.be/byHcYRpMgI4

import sqlite3

# connect to database
connect01 = sqlite3.connect("student_health.db")

# create a cursor
cursor01 = connect01.cursor()

# query the database
cursor01.execute("select rowid, * from height＿weight")
iteams01 = cursor01.fetchall()
for iteam in iteams01:
    print(iteam)
# (1, 'Samson', 'North', 197, 78)
# (2, 'Kory', 'Stiles', 183, 84)
# (4, 'Edwin', 'Rice', 171, 100)
# (5, 'Grayson', 'Vance', 178, 89)
# (6, 'Wade', 'Kemp', 186, 93)

# query the database - order by (ASC - ascending)
# ascending by rowid (ASC)
cursor01.execute("select rowid, * from height＿weight order by rowid")
iteams02 = cursor01.fetchall()
for iteam in iteams02:
    print(iteam)
# (1, 'Samson', 'North', 197, 78)
# (2, 'Kory', 'Stiles', 183, 84)
# (4, 'Edwin', 'Rice', 171, 100)
# (5, 'Grayson', 'Vance', 178, 89)
# (6, 'Wade', 'Kemp', 186, 93)

# query the database - order by (DESC - descending)
# descending by rowid (DESC)
cursor01.execute("select rowid, * from height＿weight order by rowid DESC")
iteams03 = cursor01.fetchall()
for iteam in iteams03:
    print(iteam)
# (6, 'Wade', 'Kemp', 186, 93)
# (5, 'Grayson', 'Vance', 178, 89)
# (4, 'Edwin', 'Rice', 171, 100)
# (2, 'Kory', 'Stiles', 183, 84)
# (1, 'Samson', 'North', 197, 78)

# query the database - order by height (ASC)
cursor01.execute("select rowid, * from height＿weight order by height")
iteams04 = cursor01.fetchall()
for iteam in iteams04:
    print(iteam)
# (4, 'Edwin', 'Rice', 171, 100)      171
# (5, 'Grayson', 'Vance', 178, 89)    178
# (2, 'Kory', 'Stiles', 183, 84)      183 
# (6, 'Wade', 'Kemp', 186, 93)        186
# (1, 'Samson', 'North', 197, 78)     197

# query the databae - order by first_name (DESC)
cursor01.execute("select rowid, *from height＿weight order by first_name DESC")
iteams05 = cursor01.fetchall()
for iteam in iteams05:
    print(iteam)
# (6, 'Wade', 'Kemp', 186, 93)        W
# (1, 'Samson', 'North', 197, 78)     S
# (2, 'Kory', 'Stiles', 183, 84)      K
# (5, 'Grayson', 'Vance', 178, 89)    G
# (4, 'Edwin', 'Rice', 171, 100)      E

# commit
connect01.commit()

# close
connect01.close()
