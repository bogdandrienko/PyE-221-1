import psycopg2

# CRUD

# Read - чтение(сортировка и фильтрация) из базы и запись в эксель файл
# Create - вставка новых данных (из эксель файл)
# Delete - удаление строк по условиям
# Update - обновление из базы и запись в эксель файл

# READ (SELECT)
############################################################################

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

# CREATE (INSERT)
############################################################################
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
index = 12
for i in new_arr:
    query_string = f"""
    INSERT INTO public.example_table (username, age, married, credits, id) 
    VALUES ('{i[0]}', {i[1]}, {i[2]}, {i[3]}, {index})
    """
    index += 1

    cur.execute(query_string)
    conn.commit()  # применение данных после изменений

conn.close()

# DELETE (DELETE)
############################################################################

conn = psycopg2.connect("dbname=example user=postgres password=31284bogdan")
cur = conn.cursor()

query_string = """
    DELETE FROM public.example_table
    WHERE age <= 50 and married = 'true';
    """

#

cur.execute(query_string)
conn.commit()
conn.close()

# UPDATE (UPDATE)
############################################################################

conn = psycopg2.connect("dbname=example user=postgres password=31284bogdan")
cur = conn.cursor()

query_string = """
UPDATE public.example_table
SET credits = '666.66' 
WHERE id = 2;
"""

#

cur.execute(query_string)
conn.commit()
conn.close()

# CREATE TABLE
############################################################################

conn = psycopg2.connect("dbname=example user=postgres password=31284bogdan")
cur = conn.cursor()

query_string = """
CREATE TABLE public.products
(
    tovar text,
    gruppa text,
    postavshick text,
    date_post date,
    region text,
    prodashi integer DEFAULT 0,
    sbit integer DEFAULT 0,
    pribil boolean NOT NULL DEFAULT false,
    id SERIAL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.products
    OWNER to postgres;
"""
cur.execute(query_string)
conn.commit()
conn.close()
