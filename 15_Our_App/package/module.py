import sqlite3

# Query the DB and return all records
def show_all():
    print("You have successfully executed 'show_all'")
    connect = sqlite3.connect("employee.db")
    cursor = connect.cursor()
    cursor.execute("SELECT rowid, * FROM information")
    iteams = cursor.fetchall()
    for iteam in iteams:
        print(iteam)
    connect.commit()
    connect.close()

# Add a new record to the table
def add_one(first_name, second_name, email, gender, salary):
    connect = sqlite3.connect("employee.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO information VALUES (?, ?, ?, ?, ?)", (first_name, second_name, email, gender, salary))
    connect.commit()
    connect.close()
    print("You have successfully executed 'add_one'")

# Delete record from table
def delete_one(id):
    connect = sqlite3.connect("employee.db")
    cursor = connect.cursor()
    cursor.execute("DELETE FROM information WHERE rowid = (?)", (id))
    connect.commit()
    connect.close()
    print("You have successfully executed 'delete_one'")

# Add many records to the table
def add_many(list):
    connect = sqlite3.connect("employee.db")
    cursor = connect.cursor()
    cursor.executemany("INSERT INTO information VALUES (?, ?, ?, ?, ?)", (list))
    connect.commit()
    connect.close()
    print("You have successfully executed 'add_many'")

# Look up with where
def email_lookup(email):
    connect = sqlite3.connect("employee.db")
    cursor = connect.cursor()
    cursor.execute("SELECT rowid, * FROM information WHERE email = (?)", (email,))
    iteams = cursor.fetchall()
    for iteam in iteams:
        print(iteam)
    connect.commit()
    connect.close()
