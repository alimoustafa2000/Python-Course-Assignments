# import SQLite module 
import sqlite3

# connect database
db = sqlite3.connect("Database Data Types.db")

# setting up the cursor
cr = db.cursor()

# create tables and fields
cr.execute("create table if not exists Data (id INT, name TEXT, age TINYINT, dob DATE, rank FLOAT)")

# insert data into database
cr.execute("insert into Data (id, name, age, dob, rank) values (1, 'Ali', 22, '6/2/2000', 96.5)")
cr.execute("insert into Data (id, name, age, dob, rank) values (2, 'Ola', 20, '30/7/2002', 92.5)")

# commit changes
db.commit()

# close database
db.close()
