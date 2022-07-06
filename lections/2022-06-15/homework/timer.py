import sys
import time
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton
import threading  # операции в другом потоке
import asyncio  # асинхронные операции
import multiprocessing  # операции в другом процессе


class MyUiClass(QWidget):
    def __init__(self, width=640, height=480, title="title"):
        QWidget.__init__(self)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.is_play = True

        self.seconds = 0
        self.minutes = 0
        self.hours = 0

        self.label_time = QLabel('00:00:00')
        self.layout.addWidget(self.label_time, 0, 0)

        self.push_button_stop = QPushButton('stop')
        self.push_button_stop.clicked.connect(self.stop)
        self.layout.addWidget(self.push_button_stop, 8, 0)

        self.push_button_reset = QPushButton('reset')
        self.push_button_reset.clicked.connect(self.reset)
        self.layout.addWidget(self.push_button_reset, 8, 1)

        self.push_button_start = QPushButton('start')
        self.push_button_start.clicked.connect(self.start)
        self.layout.addWidget(self.push_button_start, 8, 2)

        self.setWindowTitle(title)
        self.resize(width, height)
        self.show()

    def start(self):
        print("start")
        self.is_play = True

        def second_thread(arg1, arg2):
            while self.is_play:
                time.sleep(1)
                self.seconds += 1
                if self.seconds > 59:
                    self.seconds = 0
                    self.minutes += 1
                if self.minutes > 59:
                    self.minutes = 0
                    self.hours += 1
                if self.hours > 24:
                    self.seconds = 0
                    self.minutes = 0
                    self.hours = 0
                self.update_text()

        arg1 = ''
        arg2 = ''
        thread2 = threading.Thread(target=second_thread, args=[arg1, arg2])
        thread2.start()

    def stop(self):
        print("stop")
        self.is_play = not self.is_play
        self.update_text()

    def reset(self):
        print("reset")
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.update_text()

    def update_text(self):
        def beatify(value: int):
            if value < 10:
                return f"0{value}"
            return f"{value}"

        seconds = beatify(self.seconds)
        minutes = beatify(self.minutes)
        hours = beatify(self.hours)
        time_string = f'{hours}:{minutes}:{seconds}'
        self.label_time.setText(time_string)


app = QApplication(sys.argv)
ui = MyUiClass(640, 480, 'timer')
app.exec()
