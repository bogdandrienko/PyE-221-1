import sys
import threading
import multiprocessing
from PyQt6 import QtWidgets, QtCore, QtGui


class PyQtWindow(QtWidgets.QWidget):
    def __init__(self, window_title: str):
        super().__init__()

        self.layout = QtWidgets.QGridLayout(self)

        ##############################################

        self.label_url = QtWidgets.QLabel("url")
        self.layout.addWidget(self.label_url, 0, 0)

        self.line_edit_url = QtWidgets.QLineEdit("http://192.168.0.101:8000/api/todos_drf/1/")
        self.layout.addWidget(self.line_edit_url, 1, 0)

        self.label_status = QtWidgets.QLabel("status")
        self.layout.addWidget(self.label_status, 0, 1)

        self.line_edit_status = QtWidgets.QLineEdit("...")
        self.layout.addWidget(self.line_edit_status, 1, 1)

        self.button_start = QtWidgets.QPushButton("get request")
        self.button_start.clicked.connect(self.start)
        self.layout.addWidget(self.button_start, 1, 3)

        ###

        self.label_id = QtWidgets.QLabel("id")
        self.layout.addWidget(self.label_id, 2, 0)

        self.label_user_id = QtWidgets.QLabel("user_id")
        self.layout.addWidget(self.label_user_id, 2, 1)

        self.label_title = QtWidgets.QLabel("title")
        self.layout.addWidget(self.label_title, 2, 2)

        self.label_completed = QtWidgets.QLabel("completed")
        self.layout.addWidget(self.label_completed, 2, 3)

        ##

        self.line_edit_id = QtWidgets.QLineEdit("...")
        self.layout.addWidget(self.line_edit_id, 3, 0)

        self.line_edit_user_id = QtWidgets.QLineEdit("...")
        self.layout.addWidget(self.line_edit_user_id, 3, 1)

        self.line_edit_title = QtWidgets.QLineEdit("...")
        self.layout.addWidget(self.line_edit_title, 3, 2)

        self.check_box_completed = QtWidgets.QCheckBox("completed?")
        self.layout.addWidget(self.check_box_completed, 3, 3)

        ##

        ##############################################

        self.setWindowTitle(window_title)
        self.resize(640, 480)
        self.show()

    def start(self):
        print("get data")

        import requests

        url = str(self.line_edit_url.text())
        print(url)

        response = requests.get(url=url)
        data = response.json()
        print(data, type(data))

        self.line_edit_status.setText(str(response.status_code))

        self.line_edit_id.setText(str(data["id"]))
        self.line_edit_user_id.setText(str(data["user_id"]))
        self.line_edit_title.setText(str(data["title"]))
        self.check_box_completed.setChecked(bool(data["completed"]))



if __name__ == '__main__':
    pyqt_app = QtWidgets.QApplication([])
    pyqt_ui = PyQtWindow("client")

    sys.exit(pyqt_app.exec())
