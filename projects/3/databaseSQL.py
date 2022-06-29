import psycopg2


# conn_str = (
#     "DATABASE=example;"
#     "UID=postgres;"
#     "PWD=31284bogdan;"
#     "SERVER=127.0.0.1;"
#     "PORT=5432;"
#     )

# Connect to your postgres DB
conn = psycopg2.connect("dbname=example user=postgres password=31284bogdan")  # localhost (127.0.0.1 / 192.168.1.121)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM example_table")

# Retrieve query results
records = cur.fetchall()

print(records)
print(type(records))

for i in records:
    print(i)
    print(type(i))


conn.close()

# CRUD

# Create - вставка новых данных (из эксель файл)
# Read - чтение(сортировка и фильтрация) из базы и запись в эксель файл
# Update - обновление из базы и запись в эксель файл
# Delete - удаление строк по условиям
