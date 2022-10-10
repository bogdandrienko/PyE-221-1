import random
import sys
import time
import aiohttp
import asyncio
import json

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QGridLayout,
    QWidget
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        layout = QGridLayout()

        self.label1 = QLabel("Данные от сервера")
        layout.addWidget(self.label1, 1, 1)

        self.lineedit1 = QLineEdit("стандартный текст")
        layout.addWidget(self.lineedit1, 2, 1)

        self.label2 = QLabel(self)
        layout.addWidget(self.label1, 3, 1)
        self.pixmap = QPixmap('python.jpeg')
        self.label2.setPixmap(self.pixmap)

        pushbutton1 = QPushButton("старт")
        layout.addWidget(pushbutton1, 4, 2)
        pushbutton1.clicked.connect(self.click_button_1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setWindowTitle("CRUD PYQT6")
        self.setGeometry(1400, 900, 1400, 900)
        self.show()

    def click_button_1(self) -> None:
        print("push!")

        MainWindow.set_text(elem=self.label1, text="...ОБНОВЛЕНИЕ...")
        time.sleep(0.1)
        MainWindow.set_text(elem=self.label1, text="...ЗАВЕРШЕНО...")
        time.sleep(0.1)
        MainWindow.set_text(elem=self.label1, text=MainWindow.get_text(elem=self.lineedit1))

        self.get_data(count=random.randint(1, 10))

    @staticmethod
    def set_text(elem, text: str) -> None:
        elem.setText(text)

    @staticmethod
    def get_text(elem) -> str:
        return elem.text()

    def get_data(self, count: int) -> None:
        async def main():
            async with aiohttp.ClientSession() as session:
                async with session.get('https://jsonplaceholder.typicode.com/posts') as resp_object:
                    json_dict = await resp_object.json()
                    self.set_text(elem=self.label1, text=json_dict[count]["body"])

        asyncio.run(main())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    app.exec()
