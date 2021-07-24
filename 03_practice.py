# reference from 
# "SQLite Databases With Python - Full Course"
# https://youtu.be/byHcYRpMgI4

# import sqlite3
import sqlite3

# Create a database named student_information.db
# create a connection to the database named connect01
connect01 = sqlite3.connect("student_information.db")

# Create a cursor named cursor01
cursor01 = connect01.cursor()

# Use the cursor to create a table named Information
# Create five fields in the table
cursor01.execute("""CREATE TABLE Information(
    first_name text,
    second_name text,
    email text,
    Citizenship text,
    Age interger
)""")

# Put the data into the table of the database
cursor01.execute("INSERT INTO Information VALUES ('Yui', 'Nakata', 'yui@gmail.com', 'Japan', 19)")
cursor01.execute("INSERT INTO Information VALUES ('Naruto', 'Nakamura', 'naruto@gmail.com', 'Japan', 22)")
cursor01.execute("INSERT INTO Information VALUES ('Tom', 'Smith', 'tom@gmail.com', 'America', 21)")
cursor01.execute("INSERT INTO Information VALUES ('世徹', '歐', 'ottk@gmail.com', 'Taiwan', 22)")

# Commit
connect01.commit()

# Close 
connect01.close()
