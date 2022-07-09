from flask import Flask
import psycopg2
from flask import jsonify

# 127.0.0.1:5432 (localhost:5432) - текущая машина, откуда идёт запрос
# 192.168.1.121:5432 - локальный адрес текущей машины в этой подсети
# 89.218.132.130:80 - внешний "белый" ip-адрес от Казактелекома
# km.kz - домен первого уровня
# web.km.kz (89.218.132.130) - домен второго уровня

app = Flask(__name__)


@app.route("/")  # 'http://192.168.1.121:5000' + '/' - маршрут в браузерной строке
def index():
    return "<h1>Index</h1>"


@app.route("/get_all_rows/")
def get_all_rows():
    conn = psycopg2.connect("dbname=example user=postgres password=31284bogdan")
    cur = conn.cursor()
    query_string = """
    SELECT * FROM public.example_table
    ORDER BY id ASC
    """
    cur.execute(query_string)
    records = cur.fetchall()
    cur.close()
    conn.close()
    data = jsonify(records)
    return data
