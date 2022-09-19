import sys
import PySide6.QtWidgets as QtWidgets
import PySide6.QtGui as QtGui


class ExampleWindow(QtWidgets.QWidget):
    def __init__(self, window_name: str):
        super().__init__()

        self.window_name = window_name
        self.setGeometry(640, 480, 640, 480)
        self.setWindowTitle(self.window_name)
        self.layout = QtWidgets.QGridLayout()

        btn_quit = QtWidgets.QPushButton('нажми меня', self)
        btn_quit.clicked.connect(QtWidgets.QApplication.instance().quit)
        self.layout.addWidget(btn_quit, 0, 0)

        btn_1 = QtWidgets.QPushButton('', self)
        btn_1.clicked.connect(self.get_value_from_QLineEdit)
        self.layout.addWidget(btn_1, 0, 1)

        lbl1 = QtWidgets.QLabel(text="id", parent=self)
        self.layout.addWidget(lbl1, 1, 0)
        self.txt1 = QtWidgets.QLineEdit("-1", parent=self)
        self.layout.addWidget(self.txt1, 2, 0)

        lbl2 = QtWidgets.QLabel(text="name", parent=self)
        self.layout.addWidget(lbl2, 1, 1)
        txt2 = QtWidgets.QLineEdit("2", parent=self)
        self.layout.addWidget(txt2, 2, 1)

        lbl3 = QtWidgets.QLabel(text="surname", parent=self)
        self.layout.addWidget(lbl3, 1, 2)
        txt3 = QtWidgets.QLineEdit("2", parent=self)
        self.layout.addWidget(txt3, 2, 2)

        lbl4 = QtWidgets.QLabel("age", parent=self)
        self.layout.addWidget(lbl4, 1, 3)
        txt4 = QtWidgets.QLineEdit("4", parent=self)
        self.layout.addWidget(txt4, 2, 3)

        lbl5 = QtWidgets.QLabel("salary", parent=self)
        self.layout.addWidget(lbl5, 1, 4)
        txt5 = QtWidgets.QLineEdit("5", self)
        self.layout.addWidget(txt5, 2, 4)

        self.setLayout(self.layout)

        self.show()

    def get_value_from_QLineEdit(self):
        print(f"{self.txt1.text()}  !!!")

    def print_hello_world(self):
        print(f"{self.window_name} hello!")

    def closeEvent(self, event: QtGui.QCloseEvent):
        reply = QtWidgets.QMessageBox.question(self, 'Внимание', 'Вы действительно хотите выйти?',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = ExampleWindow('Наше приложение на PySide6')
    sys.exit(app.exec())

# id = -1
# name = 3
# surname = 3
# age = 4
# salary = 5
