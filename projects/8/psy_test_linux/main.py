import psycopg2

# connection_string = "dbname='flask_database' user='postgres' host='localhost' password='31284bogdan'"
connection_string = "dbname='flask_database' user='flask_user' host='localhost' password='12345qwertY!'"
connection = psycopg2.connect(connection_string)
cursor = connection.cursor()
connection.autocommit = False
try:
    cursor.execute("""INSERT INTO zarplata (username, salary) VALUES ('Bogdan', '60000'), ('Alice', '80000');""")
    cursor.execute("""select * from zarplata;""")
    # print(10 - "")  #
    # print({"name": "Bogdan"}["username"])  #
    data = cursor.fetchall()
    print(data)
    print(len(data))
    print(10 / 0)  # ZEROdivision
except Exception as error:
    connection.rollback()
    print(error)
else:
    connection.commit()
finally:
    cursor.close()
    connection.close()
