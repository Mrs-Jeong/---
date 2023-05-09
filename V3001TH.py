from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # проверка типов вводимых 
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

from zwillinge import *
from CityOfRedLights import *
class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3

class NitricOxide(QWidget):
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
        ''' создаёт графические элементы '''

        self.txt_fio = QLabel(txt_fio)
        self.txt_age = QLabel(txt_age)
        self.txt_1 = QLabel(txt_1)
        self.txt_2 = QLabel(txt_2)
        self.txt_3= QLabel(txt_3)
        self.txt_timer = QLabel(txt_timer)

        self.bts_next = QPushButton(txt_sendresults, self)
        self.bts_test1 = QPushButton(txt_starttest1, self)
        self.bts_test2 = QPushButton(txt_starttest2, self)
        self.bts_test3 = QPushButton(txt_starttest3, self)
    
        self.line_fio = QLineEdit(txt_fio)
        self.line_age = QLineEdit(txt_age)
        self.line_1 = QLineEdit('0')
        self.line_2 = QLineEdit('0')
        self.line_3 = QLineEdit('0')

        self.l_layout = QVBoxLayout()
        self.r_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()


        self.l_layout.addWidget(self.txt_fio, alignment = Qt.AlignLeft)
        self.l_layout.addWidget(self.line_fio, alignment = Qt.AlignLeft)
        self.l_layout.addWidget(self.txt_age, alignment = Qt.AlignLeft)
        self.l_layout.addWidget(self.line_age, alignment = Qt.AlignLeft)
        self.l_layout.addWidget(self.txt_1, alignment = Qt.AlignLeft)
        self.l_layout.addWidget(self.bts_test1, alignment = Qt.AlignLeft)
        self.l_layout.addWidget(self.line_1, alignment = Qt.AlignLeft)
        self.l_layout.addWidget(self.txt_2, alignment = Qt.AlignLeft)
        self.l_layout.addWidget(self.bts_test2, alignment = Qt.AlignLeft)
        self.l_layout.addWidget(self.line_2, alignment = Qt.AlignLeft)
        self.l_layout.addWidget(self.txt_3, alignment = Qt.AlignLeft)
        self.l_layout.addWidget(self.bts_test3, alignment = Qt.AlignLeft)
        self.l_layout.addWidget(self.line_3, alignment = Qt.AlignLeft)
        self.l_layout.addWidget(self.bts_next, alignment = Qt.AlignCenter)
        self.r_layout.addWidget(self.txt_timer, alignment = Qt.AlignRight)

        self.h_layout.addLayout(self.l_layout)
        self.h_layout.addLayout(self.r_layout)
        self.setLayout(self.h_layout)

    def timer1(self):
        global time 
        time = QTime(0,0,15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer2(self):
        global time 
        time = QTime(0,0,30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer3(self):
        global time 
        time = QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.txt_timer.setText(time.toString("hh:mm:ss"))
        self.txt_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.txt_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.txt_timer.setText(time.toString("ss"))
        self.txt_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.txt_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("ss") == "00":
            self.timer.stop()

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.txt_timer.setText(time.toString("hh:mm:ss"))
        self.txt_timer.setFont(QFont("Times", 36, QFont.Bold))
        if int(time.toString("ss")) >= 45:
            self.txt_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("ss")) <= 15:
            self.txt_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.txt_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()


    def next_clicked (self):
        self.hide()
        self.exp = Experiment(int(self.line_age.text()), self.line_1.text(), self.line_2.text(), self.line_3.text())
        self.fw = Curiosity(self.exp)


    def connect(self):
        self.bts_test1.clicked.connect(self.timer1)
        self.bts_test2.clicked.connect(self.timer2)
        self.bts_test3.clicked.connect(self.timer3)
        self.bts_next.clicked.connect(self.next_clicked)


