import time
from threading import Thread

import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
import requests
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel
from bs4 import BeautifulSoup

value = 420000.6

course_dollar = 0.0
url = 'https://finance.rambler.ru/calculators/converter/1-KZT-USD/'
# url = 'https://www.instagram.com/gazetakm/?hl=ru'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
response = requests.get(url=url, headers=headers)
print(response)
print(response.status_code)


def get_course():
    global course_dollar
    while True:
        if response.status_code == 200:  # 200 - удачный ответ
            soup = BeautifulSoup(response.text, 'lxml')
            # print(soup)
            print(type(soup))

            data = soup.find_all('div', class_='converter-display__cross-block')[0]
            new_data = str(data).split(sep='__value">')[1:]

            # [(1, 'KZT'), (0.0023, 'USD')]
            tenge = tuple(
                [
                    new_data[0].split('</div>\n<div class="converter-display__currency">')[0],
                    new_data[0].split('</div>\n<div class="converter-display__currency">')[1].split('</div>')[0]
                ]
            )
            print(tenge)
            print(type(tenge))

            dollar = tuple(
                [
                    new_data[1].split('</div>')[0],
                    new_data[1].split('</div>')[-3].split('>')[-1]
                ]
            )
            print(dollar)
            print(type(dollar))

            course = [tenge, dollar]
            print(course)
            print(type(course))

            # value
            index = 0

            for valute in course:
                index += 1
                print(f'Объект №{index}: {valute}')
                if valute[-1] == 'USD':
                    course_dollar = float(valute[0])
                    result = round(value * float(valute[0]), 3)
                    print(str(result) + " $")

            # print(new_data)
            # print(len(new_data))

            # content = response.content
            # with open(file='temp/new2.html', mode='wb') as file:
            #     file.write(content)

            # data = content.decode(encoding='ISO-8859-1')
            # print(type(data))
            # print(data)

            # new_data = data.split('value="')
            # print(len(new_data))
            # for i in new_data:
            #     print(i + '\n')
            # print(new_data)
        else:
            print("ошибка получения данных!")
        time.sleep(5.0)
        print('Курс обновлён')


Thread(target=get_course).start()

# import sys
# import random
# from PySide6 import QtCore, QtWidgets, QtGui
#
#
# class MyWidget(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
#         self.button = QtWidgets.QPushButton("File")
#         self.text = QtWidgets.QLabel("Hello World")
#         self.layout = QtWidgets.QVBoxLayout(self)
#         self.layout.addWidget(self.text)
#         self.layout.addWidget(self.button)
#
#         self.button.clicked.connect(self.magic)
#
#     @QtCore.Slot()
#     def magic(self):
#         self.text.setText(random.choice(self.hello))
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#
#     widget = MyWidget()
#     widget.resize(800, 600)
#     widget.show()
#
#     sys.exit(app.exec())



class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.line_edit = QLineEdit()
        layout.addWidget(self.line_edit)

        self.label = QLabel()
        layout.addWidget(self.label)

        self.line_edit.textChanged.connect(self.line_edit_text_changed)

        self.show()

    def line_edit_text_changed(self, text):
        try:
            text = round(course_dollar * float(text), 3)
            self.label.setText("Ваша сумма: " + str(text) + " $")
        except Exception as error:
            self.label.setText('ошибка ввода данных')


app = QApplication(sys.argv)
mw = MainWindow()
app.exec()
