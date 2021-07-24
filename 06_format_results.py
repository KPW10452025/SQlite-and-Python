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
cursor01.execute("SELECT * FROM height＿weight")
iteams01 = cursor01.fetchall()
for iteam in iteams01:
    print(iteam)
# ('Samson', 'North', 197, 76)
# ('Kory', 'Stiles', 183, 84)
# ('Rory', 'Norris', 185, 103)
# ('Edwin', 'Rice', 171, 62)
# ('Grayson', 'Vance', 178, 89)
# ('Wade', 'Kemp', 186, 93)

cursor01.execute("SELECT * FROM height＿weight")
iteams02 = cursor01.fetchall()
for iteam in iteams02:
    print(iteam[2])
# 197
# 183
# 185
# 171
# 178
# 186

cursor01.execute("SELECT * FROM height＿weight")
iteams03 = cursor01.fetchall()
sum = 0
for iteam in iteams03:
    sum = sum + iteam[2]
average_height = sum / (len(iteams03))
print("average_height =", average_height)
# average_height = 183.33333333333334

cursor01.execute("SELECT * FROM height＿weight")
iteams04 = cursor01.fetchall()
for iteam in iteams04:
    print(iteam[0] + " " + iteam[1] + "\t" + str(iteam[2]) + " cm" + "\t" + str(iteam[3]) + " kg")
# Samson North	197 cm	76 kg
# Kory Stiles	183 cm	84 kg
# Rory Norris	185 cm	103 kg
# Edwin Rice	171 cm	62 kg
# Grayson Vance	178 cm	89 kg
# Wade Kemp	    186 cm	93 kg

connect01.commit()
connect01.close()

