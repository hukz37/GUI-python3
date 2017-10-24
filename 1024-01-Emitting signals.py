#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/24 下午2:33
# @Author  : Aries
# @Site    : 
# @File    : 1024-01-Emitting signals.py
# @Software: PyCharm


import sys
from PyQt5.QtCore import pyqtSignal,QObject,Qt
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel


class Communicate(QObject):
    closeApp = pyqtSignal()

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        title = QLabel('点击鼠标即可关闭程序')
        title.move(300,100)
        self.setCentralWidget(title)
        #title设置居中
        title.setAlignment(Qt.AlignCenter)


        self.setGeometry(300,300,290,150)
        self.setWindowTitle('Emitting signals')
        self.show()


    def mousePressEvent(self, QMouseEvent):
        self.c.closeApp.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

