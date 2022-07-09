import datetime
import sys
import time

import requests
from bs4 import BeautifulSoup
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QComboBox
import threading

values = [{"name": "", "value": 0}]


def get_fresh_values():
    while True:

        current_time = datetime.datetime.now().strftime("%S")

        if int(current_time) // 10 % 2:
            print('задержка')
            time.sleep(10)

        print(f"Seconds: {current_time}")

        # time.sleep(1)

        url = 'https://myfin.by/converter.html'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.0.0 Safari/537.36'
        }
        response = requests.get(url=url, headers=headers)

        with open('new_html.html', 'wb') as file:
            file.write(response.content)

        soup = BeautifulSoup(response.text, 'lxml')

        print(soup)
        # print(soup.text)

        # data = soup.find_all('div', class_="converter-container__item")

        data = soup.findAll("input", class_="input_calc form-control form-input-sum bestmb")

        print(data)

        values = []
        for i in data:
            print(i, '\n')

            sep_name_left = 'id="bestmb_'
            sep_name_right = '" inputmode'

            val_name_1 = str(i).split(sep=sep_name_left)[1]
            val_name_2 = val_name_1.split(sep=sep_name_right)[0]

            print(val_name_2, '\n')

            sep_value_left = 'value="'
            sep_value_right = '"/>'

            val_value_1 = str(i).split(sep=sep_value_left)[1]
            val_value_2 = val_value_1.split(sep=sep_value_right)[0]

            print(val_value_2, '\n')

            dict_value = {
                "name": val_name_2,
                "value": val_value_2,
            }
            values.append(dict_value)

        print(values)


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

        self.combo_box_filter = QComboBox()
        self.combo_box_filter.addItem("usd")
        self.combo_box_filter.addItem("eur")
        self.combo_box_filter.addItems(["gbp", "cny", "pln", "rub"])

        layout.addWidget(self.combo_box_filter)  # вкладываем QComboBox -> QGridLayout

        self.show()

    def line_edit_text_changed(self, text):
        try:
            combo = self.combo_box_filter.currentText()
            print(combo)

            for dictionary in values:  # массив со словарями
                keys1 = dictionary.keys()

                print(keys1)

                values1 = dictionary.values()

                print(values1)

                item1 = dictionary.items()

                print(item1)

                # if combo in values1:
                #     print('валюта есть')
                #     text = round(float(dictionary["value"]) * float(text), 3)
                #     self.label.setText("Ваша сумма: " + str(text) + " единиц")
                # else:
                #     print('валюты нет')

                if dictionary["name"] == combo:
                    print('валюта есть')
                    text = round(float(dictionary["value"]) * float(text), 3)
                    self.label.setText("Ваша сумма: " + str(text) + " единиц")

        except Exception as error:
            self.label.setText('ошибка ввода данных')


threading.Thread(target=get_fresh_values).start()

app = QApplication(sys.argv)
mw = MainWindow()
app.exec()
