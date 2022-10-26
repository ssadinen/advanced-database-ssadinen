import sqlite3

connection = sqlite3.connect("vegetables.db")

cursor = connection.cursor()

rows = cursor.execute("select name, type from vegetable, vegtype where vegetable.vegtype_id = vegtype.id")

print(rows)

rows = list(rows)

for row in rows:
    name, type = row
    print (f"my {type} vegetable was named {name}.")

cursor.execute("delete from vegetable where vegtype_id == 3")

connection.commit()

print("updated")
rows = cursor.execute("select name, type from vegetable, vegtype where vegetable.vegtype_id = vegtype.id")

print(rows)

rows = list(rows)

for row in rows:
    name, type = row
    print (f"my {type} vegetable was named {name}.")
