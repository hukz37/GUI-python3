#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 下午2:08
# @Author  : Aries
# @Site    : 
# @File    : 1020-03-发送信号&自定义槽函数.py
# @Software: PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class Exp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(400,400,300,300)
        self.setWindowTitle('sender')

        btn1 = QPushButton('Hello',self)
        btn2 = QPushButton('World',self)

        btn1.move(30,150)
        btn2.move(150,150)

        self.statusBar()

        btn1.clicked.connect(self.btnclicked)
        btn2.clicked.connect(self.btnclicked)

    def btnclicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was clicked!')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Exp()
    ex.show()
    sys.exit(app.exec_())

