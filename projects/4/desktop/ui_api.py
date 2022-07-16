import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton, QLineEdit
import threadi  # операции в другом потоке
import asyncio  # асинхронные операции
import multiprocessing  # операции в другом процессе
import requests  # библиотека для синхронных HTTP запросов
import aiohttp  # библиотека для асинхронных HTTP запросов


class MyUiClass(QWidget):
    def __init__(self, width=640, height=480, title="title"):
        QWidget.__init__(self)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.line_edit_domen = QLineEdit('http://192.168.1.121:5000/get_all_rows/')
        self.layout.addWidget(self.line_edit_domen, 0, 0)

        self.label_result = QLabel('')
        self.layout.addWidget(self.label_result, 1, 0)

        self.push_button_start = QPushButton('sync request')
        self.push_button_start.clicked.connect(self.sync_request)
        self.layout.addWidget(self.push_button_start, 1, 1)

        self.setWindowTitle(title)
        self.resize(width, height)
        self.show()

    def sync_request(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.0.0 Safari/537.36'
        }
        response = requests.get(url=self.line_edit_domen.text(), headers=headers)
        # print(response.text)
        # print(response.json())
        self.label_result.setText(response.text)


app = QApplication(sys.argv)
ui = MyUiClass(640, 480, 'api')
app.exec()
