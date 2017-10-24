#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 下午1:48
# @Author  : Aries
# @Site    : 
# @File    : 1016-03.py
# @Software: PyCharm


import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication


class Exp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        btn = QPushButton('Quit',self)
        btn.resize(btn.sizeHint())
        #这一段demo最主要是这句代码,将按钮的点击事件置为程序的退出
        btn.clicked.connect(QCoreApplication.quit)
        btn.move(40,50)

        self.setGeometry(200,300,400,400)
        self.setWindowTitle("Quit")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exp()
    sys.exit(app.exec_())