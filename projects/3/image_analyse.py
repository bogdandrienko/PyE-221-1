# прочитать изображение в память (подать путь к изображению - от пользователя) - чтение с диска
# выдать данных об изображении
# обработка изображения (подать все нужные параметры - от пользователя)
# выдать данных об итоговом изображении
# запись (сохранение результата) - перезапись/или сохранить как

import sys
import time
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QGridLayout, QCheckBox, QPushButton, QSlider, \
    QComboBox
import cv2  # pip install opencv-python


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

        self.line_edit_path = QLineEdit('image_data/dino.jpg')  # экзампляр строки ввода текста
        self.layout.addWidget(self.line_edit_path, 2, 1)  # вкладываем QLineEdit -> QGridLayout

        self.label_check = QLabel('Статус: ')  # экзампляр строки текста
        self.layout.addWidget(self.label_check, 1, 2)

        self.check_box_status = QCheckBox()  # экзампляр чек бокса
        self.check_box_status.setChecked(False)
        self.layout.addWidget(self.check_box_status, 2, 2)  # вкладываем QCheckBox -> QGridLayout

        self.push_button_check = QPushButton('проверить наличие файла')  # экзампляр строки ввода текста
        self.push_button_check.clicked.connect(self.read_and_check_image_in_path)
        # self.push_button_check.setGeometry(QtCore.QRect(200, 150, 93, 28))
        self.layout.addWidget(self.push_button_check, 2, 3)  # вкладываем QLineEdit -> QGridLayout

        self.label_width = QLabel('Ширина: ')
        self.layout.addWidget(self.label_width, 3, 1)

        self.label_height = QLabel('Высота: ')
        self.layout.addWidget(self.label_height, 3, 2)

        self.line_edit_width = QLineEdit('0')  # экзампляр строки ввода текста
        self.layout.addWidget(self.line_edit_width, 4, 1)  # вкладываем QLineEdit -> QGridLayout

        self.line_edit_height = QLineEdit('0')  # экзампляр строки ввода текста
        self.layout.addWidget(self.line_edit_height, 4, 2)  # вкладываем QLineEdit -> QGridLayout

        self.check_box_wb = QCheckBox()  # экзампляр чек бокса
        self.check_box_wb.setChecked(False)
        self.layout.addWidget(self.check_box_wb, 5, 1)  # вкладываем QCheckBox -> QGridLayout

        self.label_check_wb = QLabel('сделать чёрно-белым: ')  # экзампляр строки текста
        self.layout.addWidget(self.label_check_wb, 5, 2)

        self.check_box_protect = QCheckBox()  # экзампляр чек бокса
        self.check_box_protect.setChecked(False)
        self.check_box_protect.stateChanged.connect(self.protect)
        self.layout.addWidget(self.check_box_protect, 5, 3)  # вкладываем QCheckBox -> QGridLayout

        self.label_check_box_protect = QLabel('подтвердить изменения: ')  # экзампляр строки текста
        self.layout.addWidget(self.label_check_box_protect, 5, 4)

        # self.slider_quality = QSlider(Qt.Horizontal)
        self.slider_quality = QSlider()
        self.slider_quality.setMinimum(1)
        self.slider_quality.setMaximum(100)
        self.slider_quality.setValue(95)
        self.layout.addWidget(self.slider_quality, 4, 5)

        self.label_slider_quality = QLabel('качество: ')  # экзампляр строки текста
        self.layout.addWidget(self.label_slider_quality, 5, 5)

        self.label_1 = QLabel('')
        self.layout.addWidget(self.label_1, 6, 1)

        self.push_button_start = QPushButton('выполнить')  # экзампляр строки ввода текста
        self.push_button_start.clicked.connect(self.start)
        self.push_button_start.setEnabled(False)
        # self.push_button_check.setGeometry(QtCore.QRect(200, 150, 93, 28))
        self.layout.addWidget(self.push_button_start, 7, 1)  # вкладываем QLineEdit -> QGridLayout

        self.push_button_stop = QPushButton('отменить')  # экзампляр строки ввода текста
        self.push_button_stop.clicked.connect(self.stop)
        # self.push_button_check.setGeometry(QtCore.QRect(200, 150, 93, 28))
        self.layout.addWidget(self.push_button_stop, 7, 3)  # вкладываем QLineEdit -> QGridLayout

        self.combo_box_filter = QComboBox()
        self.combo_box_filter.addItem("гаусс")
        self.combo_box_filter.addItem("фильтр 2")
        self.combo_box_filter.addItems(["фильтр 3", "фильтр 4", "фильтр 5"])

        self.layout.addWidget(self.combo_box_filter, 7, 4)  # вкладываем QComboBox -> QGridLayout

        # self.line_edit1 = QLineEdit()  # экзампляр строки ввода текста
        # self.layout2.addWidget(self.line_edit1)  # вкладываем QLineEdit -> QGridLayout
        #
        # self.line_edit2 = QLineEdit()  # экзампляр строки ввода текста
        # self.layout2.addWidget(self.line_edit2, 2, 2)  # вкладываем QLineEdit -> QGridLayout

        # self.line_edit3 = self.render_line_edit(self.layout2, '111111111', 2, 2)

        # self.line_edit3 = QLineEdit()  # экзампляр строки ввода текста
        # self.layout2.addWidget(self.line_edit3)  # вкладываем QLineEdit -> QGridLayout

        # self.line_edit.textChanged.connect(self.line_edit_text_changed)

        def delay(seconds: float):
            time.sleep(seconds)
            # тут код(поток исполнения)
            self.show()
        delay(0.5)
        # self.show()

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
        except Exception as error:
            print(error)
            img2 = []

        print(img2)
        print(len(img2))
        print(type(img2))

        if len(img2) > 0:  # [] - False, [''] - True, '' - False, '1' - True
            cv2.imshow('dino_window2', img2)  # рендерит(отрисовывает на экране) массив пикселей - изображение
            cv2.waitKey(1)  # для задержки отображения кадра (если изображение, то нужен параметр 1)
            # cv2.imwrite('dino2.jpg', img)

            has_file = True
            print('изображение успешно прочитано')

            self.image_data = img2
            print(self.image_data.shape)
            # height, width = self.image_data.shape[:2]  # -> (1920, 1080)
            height, width, channels = self.image_data.shape  # -> (1920, 1080, 3)

            self.line_edit_width.setText(str(width))
            self.line_edit_height.setText(str(height))

        else:
            has_file = False
            print('изображение не прочитано!')

            self.line_edit_width.setText("0")
            self.line_edit_height.setText("0")

        self.check_box_status.setChecked(has_file)

        # self.push_button_check.hide()  # прятать элемент интерфейса

    def start(self):
        print("start")

        # combo = self.combo_box_filter.itemText(3)
        combo = self.combo_box_filter.currentText()
        print(combo)

        white_black = bool(self.check_box_wb.isChecked())

        quality = int(self.slider_quality.value())
        width = int(self.line_edit_width.text())
        height = int(self.line_edit_height.text())

        image = self.image_data
        print(type(image))

        if white_black:
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # BGR(RGB) -> GRAY
            image = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)[1]  # GRAY -> WHITE

        # value = 100  # 0 -> 255
        # if value > 127:
        #     value = 1
        # else:
        #     value = 0

        image = cv2.resize(image, (width, height))

        # 0 200 400
        #  150 250
        # image = image[150:250:1]  # обрезка

        cv2.imwrite("image_data/dino_new.jpg", image, [cv2.IMWRITE_JPEG_QUALITY, quality])

    def stop(self):
        print("stop")
        pass

    def protect(self):
        self.push_button_start.setEnabled(self.check_box_protect.isChecked())

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
mw = MainWindow(640, 480, 'image analyse')  # создаём инстанс (экземпляр) класса
# пока класс не умрёт, эта часть кода не затронется
app.exec()  # очистка памяти

app1 = QApplication(sys.argv)
app1.exec()

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
