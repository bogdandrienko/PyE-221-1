import openpyxl
print(openpyxl.__version__)

from docx import Document
from docx.shared import Inches

document = Document()

#  (чем запускаем)   флаг    каким модулем      имя папки
#     python         -m         venv              env  # создание виртуального окружения
# python -m venv env

# cd env       cd Scripts     call activate.bat
# call env/Scripts/activate.bat  # активация виртуального окружения

# pip install --upgrade pip  # обновление pip внутри виртуального окружения

# pip install openpyxl==3.0.9  # установка специфичной версии
# pip install openpyxl  # установка последней версии
# pip uninstall openpyxl -y  # удаление библиотеки

# pip freeze > requirement.txt  # заморозка(сохранение) библиотек и модулей в текстовый файл
# pip install -r requirement.txt  # установка построчно каждой библиотеки с версией из файла
