#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 下午1:49
# @Author  : Aries
# @Site    : 
# @File    : 1020-01-信号槽连接滑块与 LCD.py
# @Software: PyCharm

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QSlider,QVBoxLayout

class Exp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout()

        lcd = QLCDNumber(self)
        slider = QSlider(Qt.Horizontal , self)

        vbox.addWidget(lcd)
        vbox.addWidget(slider)
        self.setLayout(vbox)


        slider.valueChanged.connect(lcd.display)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('signals-slots')

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Exp()
    sys.exit(app.exec_())


