from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from instr import *
from final_win import *

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Experiment:
    def __init__(self, age, name, height, weight):
        self.age = age
        self.name = name
        self.height = height
        self.weight = weight

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.connects()
        self.set_appear()
        self.show()

    def initUi(self):
        self.btn_next = QPushButton(txt_sendresults, self)

        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_height = QLabel(txt_height)
        self.text_weight = QLabel(txt_weight)

        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.line_height = QLineEdit(txt_hintheight)
        self.line_weight = QLineEdit(txt_hintweight)

        self.l_line = QVBoxLayout()
        self.l_line.addWidget(self.text_name, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.line_name, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.text_age, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.line_age, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.text_height, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.line_height, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.text_weight, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.line_weight, alignment=Qt.AlignCenter)

        self.l_line.addWidget(self.btn_next, alignment=Qt.AlignCenter)

        self.setLayout(self.l_line)

    def next_click(self):
        self.hide()
        self.exp = Experiment(self.line_age.text(), self.line_name.text(),
                               self.line_height.text(), self.line_weight.text())
        self.tw = FinalWin(self.exp)
        self.tw.show()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
