import random

import pyodbc
import psycopg2


# -- CRUD create read update delete:
#
# -- SELECT * FROM public.zarplata ORDER BY id ASC -- Выборка с сортировкой
# -- SELECT * FROM public.zarplata where alive = '0' -- Условная выборка
# -- SELECT name, value FROM public.zarplata ORDER BY id ASC -- Выборка определённых полей
# -- SELECT * FROM public.zarplata ORDER BY value desc, id desc -- desc | acs
# -- SELECT sum(value) FROM public.zarplata -- sum, max, min, avg,
# -- SELECT min(value), position FROM public.zarplata GROUP by position
#
# -- INSERT INTO public.zarplata (id, name, position, value, alive) VALUES ('8', 'Alice', 'programmer', '210000', '0') -- Вставка строки
# -- INSERT INTO public.zarplata (id, name, position, value, alive) VALUES ('11', 'Alice', 'programmer', '111', '1'), ('10', 'Alice', 'programmer', '222', '1') -- Вставка строк
#
# -- UPDATE public.zarplata SET value = value + 666 where alive = '1'
#
# -- DELETE FROM public.zarplata where name = 'Тлеген2'
#
# -- SELECT * FROM public.zarplata

def start(name):
    # Server = host = ip = localhost = 127.0.0.1
    # connection_string = 'DRIVER={PostgreSQL Unicode};' \
    #                     'Server=127.0.0.1;' \
    #                     'Port=5432;' \
    #                     'Database=zarplata;' \
    #                     'User ID=postgres;' \
    #                     'Password=31284bogdan;' \
    #                     'String Types=Unicode'

    connection_string = "dbname=zarplata user=postgres password=31284bogdan"

    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    connection.autocommit = False

    try:
        # while True:
        #     username = input("Введите своё имя")
        #     if len(username) > 3:
        #         break

        # anything
        # sql_string = "SELECT * FROM public.zarplata"
        # sql_string = "SELECT * FROM public.zarplata where alive = '0'"
        # sql_string = f"INSERT INTO public.zarplata VALUES ('7', '{str(username)}', 'programmer', '6666', '0')"

        # class User:
        #     def __init__(self, id, name):
        #         self.id = id
        #         self.name = name
        # users = [User(id=x, name=f"Alice{x}") for x in range(200, 300)]

        sql_string = "INSERT INTO public.zarplata (id, name, position, value, alive) VALUES "
        for x in range(101, 200):
            sql_string += f" ('{x}', 'Alice{x}', 'programmer', " \
                          f"'{random.randint(20000, 60000) * x}', '{random.randint(0, 1)}'), "

        # datas = [
        #     {
        #         "id": x,
        #         "name": f"Alice{x}",
        #         "position": "programmer",
        #         "value": random.randint(20000, 60000) * x,
        #         "alive": random.randint(0, 1)
        #     } for x in range(20, 100)
        # ]
        # for row in datas:
        #     sql_string += f""" ('{row["id"]}', '{row["name"]}', '{row["position"]}',
        #                 '{row["value"]}', '{row["alive"]}'), """
        # print(f"datas: {datas}")
        sql_string = sql_string[:-2:]

        # sql_string = "INSERT INTO public.zarplata (id, name, position, value, alive) VALUES " \
        #              "('11', 'Alice', 'programmer', '111', '1'),  " \
        #              "('10', 'Alice', 'programmer', '222', '1')"
        #
        cursor.execute(sql_string)
        try:
            # data = cursor.fetchone()
            data = cursor.fetchall()  # [(5, 'Alice', 'programmer', 210000, False), (1, 'Bogdan', 'programmer', 200...]
            print(f"data: {data}")
        except:
            pass
    except Exception as error:
        print(f"error: {error}")
        connection.rollback()  # откат всей транзакции
    else:  # блок, который выполняется, если ошибок не было
        connection.commit()  # применение всей транзакции
    finally:  # блок, который выполняется всегда
        cursor.close()
        connection.close()


if __name__ == '__main__':
    start('')
