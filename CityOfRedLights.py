from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # проверка типов вводимых значений
from PyQt5.QtWidgets import (
      QApplication, QWidget,
      QHBoxLayout, QVBoxLayout, QGridLayout,
      QGroupBox, QRadioButton,
      QPushButton, QLabel, QListWidget, QLineEdit)
     
from zwillinge import *

class Curiosity(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        # создаём и настраиваем графические элементы:
        self.initUI()
 
      #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
     
      # старт:
        self.show()

    def howl(self):
        if self.exp.age <7:
            self.index = 0
            return 'нет данных'
        self.index = (4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200)/10
        if self.exp.age == 7 or self.exp.age == 8:
            if self.index >= 21:
                return 'низкий'
            elif self.index < 21 and self.index >17:
                return 'удовлетворительный'
            elif self.index < 17 and self.index >12:
                return 'средний'
            elif self.index < 12 and self.index >7:
                return 'выше среднего'
            elif self.index <= 7:
                return 'высокий'
        elif self.exp.age == 9 or self.exp.age == 10:
            if self.index >= 20:
                return 'низкий'
            elif self.index < 20 and self.index >16:
                return 'удовлетворительный'
            elif self.index < 16 and self.index >11:
                return 'средний'
            elif self.index < 11 and self.index >5:
                return 'выше среднего'
            elif self.index <= 5:
                return 'высокий'
        elif self.exp.age == 11 or self.exp.age == 12:
            if self.index >= 18:
                return 'низкий'
            elif self.index < 18 and self.index >14:
                return 'удовлетворительный'
            elif self.index < 14 and self.index >9:
                return 'средний'
            elif self.index < 9 and self.index >4:
                return 'выше среднего'
            elif self.index <= 4:
                return 'высокий'
        elif self.exp.age == 13 or self.exp.age == 14:
            if self.index >= 17:
                return 'низкий'
            elif self.index < 17 and self.index >13:
                return 'удовлетворительный'
            elif self.index < 13 and self.index >8:
                return 'средний'
            elif self.index < 8 and self.index >2:
                return 'выше среднего'
            elif self.index <= 2:
                return 'высокий'
        elif self.exp.age >= 15:
            if self.index >= 15:
                return 'низкий'
            elif self.index < 15 and self.index >11:
                return 'удовлетворительный'
            elif self.index < 11 and self.index >6:
                return 'средний'
            elif self.index < 6 and self.index >1:
                return 'выше среднего'
            elif self.index <= 1:
                return 'высокий'
            
            
    def initUI(self):
      ''' создаёт графические элементы '''
      self.work_text = QLabel(txt_workheart + self.howl())
      self.index_text = QLabel(txt_index + str(self.index))
 
      self.layout_line = QVBoxLayout()
      self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
      self.layout_line.addWidget(self.work_text, alignment = Qt.AlignCenter)        
      self.setLayout(self.layout_line)
 
    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_hight)
        self.move(win_x, win_y)




