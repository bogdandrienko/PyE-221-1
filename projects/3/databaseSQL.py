import psycopg2


password = ''
















conn = psycopg2.connect(
    dbname='example', user='postgres', password=password, host='localhost'
)
cursor = conn.cursor()
cursor.execute('SELECT * FROM example_table')
records = cursor.fetchall()

print(records)

cursor.close()
conn.close()


# CRUD

# Create - вставка новых данных (из эксель файл)
# Read - чтение(сортировка и фильтрация) из базы и запись в эксель файл
# Update - обновление из базы и запись в эксель файл
# Delete - удаление строк по условиям
