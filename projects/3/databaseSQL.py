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

# read data
cur.execute("""
SELECT * FROM public.example_table
WHERE age > 19
ORDER BY Age ASC, credits DESC
""")

# Retrieve query results
records = cur.fetchall()

print(records)
print(type(records))

for i in records:
    print(i)
    print(type(i))

conn.close()


conn = psycopg2.connect("dbname=example user=postgres password=31284bogdan")
cur = conn.cursor()

# ('t', 25, True, 30000.6, 1)

new_arr = [
    ['w', 25, 'true', 30000.6, 1],
    ['b', 50, 'false', 30.6, 1],
    ['y', 25, 'true', 30000.6, 1],
    ['r', 75, 'false', 500.6, 0],
    ['u', 88, 'true', 30000.6, 1],
    ['3', 25, 'true', 305.6, 0],
]

# create data
index = 15
for i in new_arr:

    query_string = f"""
    INSERT INTO public.example_table (username, age, married, credits, id) 
    VALUES ('{i[0]}', {i[1]}, {i[2]}, {i[3]}, {index})
    """
    index += 1

    cur.execute(query_string)
    conn.commit()
# records = cur.fetchall()

# CRUD

# Create - вставка новых данных (из эксель файл)
# Read - чтение(сортировка и фильтрация) из базы и запись в эксель файл
# Update - обновление из базы и запись в эксель файл
# Delete - удаление строк по условиям
