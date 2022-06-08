import os
import shutil

# first = os.path.abspath(os.path.dirname(__file__))  # содержит абсолютный путь к текущему скрипту
first = ''  # содержит относительный путь к текущему скрипту
second = "temp\\junk2.txt"  # \ - изоляция символа   \n - перенос строки, \t - табуляция...
path = os.path.join(first, second)
print(f"path: {path}")
try:
    os.remove(path)  # удаление файла
except Exception as error:
    print(error)
finally:
    try:
        os.rmdir('temp')  # удаление пустой папки
    except Exception as error:
        print(error)
        shutil.rmtree('temp')  # удаление не пустой папки
