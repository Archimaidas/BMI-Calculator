from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from instr import *

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.initUi()
        self.set_appear()
        self.show()

    def result(self):
        height_m = float(self.exp.height) / 100
        weight = float(self.exp.weight)
        self.index = weight / (height_m ** 2)

        if self.index < 18.5:
            return txt_res1
        elif self.index < 25:
            return txt_res2
        elif self.index < 30:
            return txt_res3
        else:
            return txt_res4

    def initUi(self):
        self.workh_text = QLabel(txt_workheart + self.result())
        self.index_text = QLabel(txt_index + f"{self.index:.1f}")
        self.name_text = QLabel(self.exp.name)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.name_text, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.index_text, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
