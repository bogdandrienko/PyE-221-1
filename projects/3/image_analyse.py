# прочитать изображение в память (подать путь к изображению - от пользователя) - чтение с диска
# выдать данных об изображении
# обработка изображения (подать все нужные параметры - от пользователя)
# выдать данных об итоговом изображении
# запись (сохранение результата) - перезапись/или сохранить как

import time
import sys
import requests
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QGridLayout, QCheckBox, QPushButton
import cv2  # pip install opencv-python

# from threading import Thread


class MainWindow(QWidget):  # MainWindow - класс наследник(дочерний) от класса QWidget(родитель)
    def __init__(self, width=640, height=480, title="title"):
        QWidget.__init__(self)  # тут происходит вызов конструктора для родителя

        self.setWindowTitle(title)
        self.resize(width, height)

        self.image_data = None

        # layout = QVBoxLayout()
        # self.setLayout(layout)
        #
        # self.line_edit = QLineEdit()
        # layout.addWidget(self.line_edit)
        #
        # self.line_edit1 = QLineEdit()
        # layout.addWidget(self.line_edit1)
        #
        # self.label = QLabel()
        # layout.addWidget(self.label)

        self.layout = QGridLayout()  # экземпляр класса интерфейса grid(сетка)
        self.setLayout(self.layout)  # вкладываем QGridLayout -> MainWindow(QWidget)

        self.label_path = QLabel('Путь к файлу: ')  # экзампляр строки текста
        self.layout.addWidget(self.label_path, 1, 1)

        self.line_edit_path = QLineEdit('dino.jpg')  # экзампляр строки ввода текста
        self.layout.addWidget(self.line_edit_path, 2, 1)  # вкладываем QLineEdit -> QGridLayout

        self.label_check = QLabel('Статус: ')  # экзампляр строки текста
        self.layout.addWidget(self.label_check, 1, 2)

        self.check_box_status = QCheckBox()  # экзампляр строки ввода текста
        self.check_box_status.setChecked(False)
        self.layout.addWidget(self.check_box_status, 2, 2)  # вкладываем QLineEdit -> QGridLayout

        self.push_button_check = QPushButton('проверить наличие файла')  # экзампляр строки ввода текста
        self.push_button_check.clicked.connect(self.check_image_in_path)
        # self.push_button_check.setGeometry(QtCore.QRect(200, 150, 93, 28))
        self.layout.addWidget(self.push_button_check, 2, 3)  # вкладываем QLineEdit -> QGridLayout

        # self.line_edit1 = QLineEdit()  # экзампляр строки ввода текста
        # self.layout2.addWidget(self.line_edit1)  # вкладываем QLineEdit -> QGridLayout
        #
        # self.line_edit2 = QLineEdit()  # экзампляр строки ввода текста
        # self.layout2.addWidget(self.line_edit2, 2, 2)  # вкладываем QLineEdit -> QGridLayout

        # self.line_edit3 = self.render_line_edit(self.layout2, '111111111', 2, 2)

        # self.line_edit3 = QLineEdit()  # экзампляр строки ввода текста
        # self.layout2.addWidget(self.line_edit3)  # вкладываем QLineEdit -> QGridLayout

        # self.line_edit.textChanged.connect(self.line_edit_text_changed)

        self.show()

    def read_and_check_image_in_path(self):

        value = self.line_edit_path.text()
        print(value)

        # тут мы будем проверять наличие файла по пути в строке

        # opencv
        # self.image_data = пиксели

        # C:\Project\Github_Projects\PyE-221-1\dino.jpg - абсолютный
        # dino.jpg - относительный
        # img1 = cv2.imread(value, cv2.IMREAD_GRAYSCALE)  # читаем изображение по пути, с флагом для серого
        # cv2.imshow('dino_window1', img1)  # рендерит(отрисовывает на экране) массив пикселей - изображение

        try:
            img2 = cv2.imread(value, cv2.IMREAD_COLOR)  # читаем изображение по пути, с флагом для цветного
            cv2.imshow('dino_window2', img2)  # рендерит(отрисовывает на экране) массив пикселей - изображение
            cv2.waitKey(1)  # для задержки отображения кадра (если изображение, то нужен параметр 1)
            # cv2.imwrite('dino2.jpg', img)
        except Exception as error:
            print(error)
            img2 = []

        print(img2)
        print(len(img2))
        print(type(img2))

        if len(img2) > 0:  # [] - False, [''] - True, '' - False, '1' - True
            has_file = True
            print('изображение успешно прочитано')
            self.image_data = img2
        else:
            has_file = False
            print('изображение не прочитано!')

        self.check_box_status.setChecked(has_file)

        # self.push_button_check.hide()

    def render_line_edit(self, parent, default="", row=1, col=1):
        new = QLineEdit(default)
        parent.addWidget(new, row, col)
        return new

    def create_line_edit(self):
        self.layout.addWidget(QLineEdit())
        return

    # def line_edit_text_changed(self, text):
    #     try:
    #         text = round(course_dollar * float(text), 3)
    #         self.label.setText("Ваша сумма: " + str(text) + " $")
    #     except Exception as error:
    #         self.label.setText('ошибка ввода данных')


app = QApplication(sys.argv)
mw = MainWindow(640, 480, 'image analyse')
app.exec()

# class Base(object):
#     def __init__(self):
#         print
#         "Base created"
#
#
# class ChildA(Base):
#     def __init__(self):
#         Base.__init__(self)
#
#
# class ChildB(Base):
#     def __init__(self):
#         super(ChildB, self).__init__()
#
#
# ChildA()
# ChildB()
