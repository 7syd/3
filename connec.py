import mysql.connector

new_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "6969",
    database = "tester"
)

new_cursor = new_db.cursor()

table_query = "Create table tester6(id INT, name VARCHAR(200), age INT)"
new_cursor.execute(table_query)

new_db.commit()

insert_query = "Insert into tester6(id,name,age) Values (%s,%s,%s)"
vals = [('101','ash','20'),('102','sidd','20'),('103','harsh','19')]

new_cursor.executemany(insert_query,vals)

new_db.commit()

display_query = "Select * From tester6"

new_cursor.execute(display_query)
new_data = new_cursor.fetchall()

print("\nInserted values Table : \n")
for x in new_data:
    print(x)



update_query = "Update tester6 set age = '20' where id = '103'"
new_cursor.execute(update_query)

new_db.commit()

new_cursor.execute(display_query)
new_data2 = new_cursor.fetchall()

print("\nUpdated Table : \n")
for x in new_data2:
    print(x)




delete_query = "Delete from tester6 where id = '103'"
new_cursor.execute(delete_query)

new_db.commit()

new_cursor.execute(display_query)
new_data3 = new_cursor.fetchall()

print("\nDeleted values Table : \n")
for x in new_data3:
    print(x)

