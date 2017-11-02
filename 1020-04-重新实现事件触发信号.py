#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 下午2:18
# @Author  : hukezhu
# @Site    : 
# @File    : 1020-04-重新实现事件触发信号.py
# @Software: PyCharm


import sys
from PyQt5.QtCore import pyqtSignal,QObject
from PyQt5.QtWidgets import QMainWindow, QApplication

class Communicate(QObject):
    closeApp = pyqtSignal()

class Exp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400,400,500,300)
        self.setWindowTitle('Emitting')

        self.c = Communicate()
        self.c.closeApp.connect(self.close)

    def mousePressEvent(self, QMouseEvent):
        self.c.closeApp.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exp()
    ex.show()
    sys.exit(app.exec_())


