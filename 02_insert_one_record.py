# reference from 
# "SQLite Databases With Python - Full Course"
# https://youtu.be/byHcYRpMgI4

import sqlite3

conn01 = sqlite3.connect('customer.db')

# Insert One Record Into Table
c01 = conn01.cursor()

c01.execute("INSERT INTO customers VALUES ('Ban', 'Takahashi', 'ban@gmail.com')")
c01.execute("INSERT INTO customers VALUES ('Tom', 'Smith', 'tom@gmail.com')")

print("command executed successfully!")

# Commit command
conn01.commit()

# Close connection
conn01.close()

# Every time you run the code, you will write the data into the database.
# It means these data will not be overwritten. It will keep repeating input to the database.

# In this case, we use main01.py to create a database and it's table.
# When we run the main02.py, we'll have Ban and Tom in the database.

# Ban	Takahashi	ban@gmail.com
# Tom	Smith	    tom@gmail.com

#  When we run the main02.py again, we'll have repeated data.

# Ban	Takahashi	ban@gmail.com
# Tom	Smith	    tom@gmail.com
# Ban	Takahashi	ban@gmail.com
# Tom	Smith	    tom@gmail.com
