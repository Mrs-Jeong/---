from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

from zwillinge import *
from V3001TH import *

class Gangstas(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()
        self.start()
        self.connect()
        self.show()

    def start(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_hight)
        self.move(win_x, win_y)
        
    def initui(self):
        self.hello_txt = QLabel(txt_hello)
        self.instraction = QLabel(txt_instraction)
        self.button = QPushButton(txt_next)
        self.layout1 = QVBoxLayout()
        self.layout1.addWidget(self.hello_txt)
        self.layout1.addWidget(self.instraction)
        self.layout1.addWidget(self.button)
        self.setLayout(self.layout1)
    
    def next_clicked(self):
        self.hide()
        self.mamur = NitricOxide()

    def connect(self):
        self.button.clicked.connect(self.next_clicked)



app = QApplication([])
mw = Gangstas()
app.exec_()
