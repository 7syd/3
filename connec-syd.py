import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user='root',
    password="siddheya78",
    database="d_name"
)

cursor = conn.cursor()

# C_query = "CREATE TABLE Student_2 (name varchar(10), age INT (3), address varchar(10))"

# cursor.execute(C_query)
# conn.commit()


i_query = "INSERT INTO Student_2 (name, age, address) VALUES (%s, %s, %s)"
values = ("sidd", 19, "PUNE")
cursor.execute(i_query, values)
conn.commit()

u_query = "UPDATE Student_2 SET age = %s WHERE name = %s"
new_age = 25
name_to_update = "sidd"
cursor.execute(u_query, (new_age, name_to_update))
conn.commit()

s_query = "SELECT * FROM Student_2 WHERE name = %s"
name_to_select = "sidd"
cursor.execute(s_query, (name_to_select,))  # Note the comma to create a single-element tuple
result = cursor.fetchall()
if result:
    for row in result:
        print(row)
else:
    print("No such record")

d_query = "DELETE FROM Student WHERE name = %s"
name_to_delete = "sidd"
cursor.execute(d_query, (name_to_delete,))
conn.commit()

cursor.close()
conn.close()
