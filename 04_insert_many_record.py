# reference from 
# "SQLite Databases With Python - Full Course"
# https://youtu.be/byHcYRpMgI4

# import sqlite3
import sqlite3

# Create a database named student_health.db
# create a connection to the database named connect01
connect01 = sqlite3.connect("student_health.db")

# Create a cursor named cursor01
cursor01 = connect01.cursor()

# Use the cursor to create a table named height＿weight
# Create two fields in the table
cursor01.execute("""CREATE TABLE height＿weight(
    first_name text,
    second_name text,
    height interger,
    weight interger
)""")

# Create a list of data
many_students_height_weight = [
                                ('Samson', 'North', 197, 76),
                                ('Kory', 'Stiles', 183, 84),
                                ('Rory', 'Norris', 185, 103),
                                ('Edwin', 'Rice', 171, 62),
                                ('Grayson', 'Vance', 178, 89),
                                ('Wade', 'Kemp', 186, 93),
                            ]


# Insert the data list into the table of the database
# use the code .executemany
cursor01.executemany("INSERT INTO height＿weight VALUES (?, ?, ?, ?)", many_students_height_weight)

# Commit
connect01.commit()

# Close 
connect01.close()
