import sqlite3

connection = sqlite3.connect("vegetables.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table vegetable")
except:
    pass

try:
    cursor.execute("drop table vegtype")
except:
    pass

cursor.execute("create table vegetable (id integer primary key, name text, vegtype_id int)")

cursor.execute("create table vegtype (id integer primary key, type text)")

cursor.execute("insert into vegtype (type) values ('leafy')")
cursor.execute("insert into vegtype (type) values ('seeded')")
cursor.execute("insert into vegtype (type) values ('root')")

cursor.execute("insert into vegetable (name, vegtype_id) values ('spinach',1)")
cursor.execute("insert into vegetable (name, vegtype_id) values ('peppers',2)")
cursor.execute("insert into vegetable (name, vegtype_id) values ('potato',3)")
cursor.execute("insert into vegetable (name, vegtype_id) values ('lettuce',1)")

connection.commit()
connection.close()

print("done.")