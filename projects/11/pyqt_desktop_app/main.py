"""
1. Сборка в .exe (без консоли)
2. Подготовить скрипты для сборки, восстановления
3. Настройки хранятся в json / sql lite (import/export)
4. Основные данные хранятся в postgres
5. Threading / asyncio
6. tray
7. debugging
8. авторизация/аутентификация
9. веб запросы
10. обработка данных в отдельном процессе
"""
import json
import threading
import time

from PyQt6 import uic
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QMenu, QMainWindow, QTextEdit
import sys
from PyQt6 import QtCore, QtWidgets, QtGui


# pip install openpyxl psycopg2 pyqt6

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()

class Ui2(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui2, self).__init__()
        uic.loadUi('uic.ui', self)

        self.store: dict[str, any] = {"delay": 2.0, "text": "Python"}


        self.lineEditText: QtWidgets.QLineEdit = self.findChild(QtWidgets.QLineEdit, 'lineEditText')

        self.pushButtonExport = self.findChild(QtWidgets.QPushButton, 'pushButtonExport')
        self.pushButtonExport.clicked.connect(self.export_settings)

        self.pushButtonImport.clicked.connect(self.import_settings)

        icon = QIcon("src/images/icon.png")

        # Create the tray
        tray = QSystemTrayIcon()
        tray.setIcon(icon)
        tray.setVisible(True)
        menu = QMenu()
        action = QAction("A menu item")
        menu.addAction(action)

        # Add a Quit option to the menu.
        quit = QAction("Quit")
        # quit.triggered.connect(self.quit)
        menu.addAction(quit)

        # Add the menu to the tray
        tray.setContextMenu(menu)

        self.show()

    def start(self):
        print("start")

    def import_settings(self):
        with open("src/settings.json", "r") as file:
            self.store = json.load(file)
        self.update()

    def update(self):
        self.lineEditText.setText(self.store["text"])

    def export_settings(self):
        self.store["text"] = self.lineEditText.text()

        with open("src/settings.json", "w") as file:
            json.dump(self.store, file)


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('uic.ui', self)

        self.pause = False

        self.setWindowTitle("My App")
        self.setWindowIcon(QtGui.QIcon("./src/images/icon.png"))
        # self.setStyle()
        self.resize(1280, 720)
        self.setMinimumSize(640, 480)
        self.setMaximumSize(1920, 1080)

        self.button1 = QtWidgets.QPushButton("старт")
        self.button2 = QtWidgets.QPushButton("стоп")
        self.button1.clicked.connect(self.start)
        self.button2.clicked.connect(self.stop)

        layout = QtWidgets.QGridLayout()

        layout.addWidget(self.button1, 0, 0)
        layout.addWidget(self.button2, 1, 0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # self.label.setText("you pressed the button")

    def start(self):
        self.pause = False
        new_thread = threading.Thread(target=self.click)
        new_thread.start()

    def stop(self):
        self.pause = True

    def click(self):
        print("started")
        time.sleep(2.5)
        while not self.pause:
            print("action\n")
            time.sleep(2.0)
        print("stopped")
        pass

    @staticmethod
    def init():
        # Form, Window = uic.loadUiType("uic.ui")
        app = QApplication([])
        window = Ui2()
        # window = Window()
        # form = Form()
        # form.setupUi(window)

        window.show()
        app.exec()

        # app = QApplication(sys.argv)
        # app.setStyle('Fusion')
        # # app.setStyle('windowsvista') # def
        # # app.setStyle('Windows') # xp
        # window = Ui()
        # window.show()
        # app.exec()


if __name__ == "__main__":
    Ui.init()
