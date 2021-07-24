# SQLite comes preinstalled on Mac, so you can simply open the terminal application and type sqlite3 to launch the server.
# Type .help for all the command.
# Type .quit to quit SQLite.

# reference from 
# "SQLite Databases With Python - Full Course"
# https://youtu.be/byHcYRpMgI4

# sqlite3 --- SQLite 数据库 DB-API 2.0 接口模块
# https://docs.python.org/zh-cn/3/library/sqlite3.html

# { 01:Connect to Database in Python }

# first to import sqlite3
import sqlite3

# to create a connection.
# connextion_name = sqlite3.connect('db_name')
# if db_name doesn't exist, it'll create a database named db_name.
# And now the main.py will have a connection to db_name.db which named conn01.
conn01 = sqlite3.connect('customer.db')

# { 02:Create A Table }

# Create a cursor
c01 = conn01.cursor()

# Create a table
c01.execute("""CREATE TABLE customers(
    first_name text,
    second_name text,
    email text
)""")
# Datatypes:
# Null
# INTEGER
# REAL
# TEXT
# BLOB

# Commit command
conn01.commit()

# Close connection
conn01.close()
