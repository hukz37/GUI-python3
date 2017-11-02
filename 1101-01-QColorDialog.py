#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/1 下午3:03
# @Author  : hukezhu
# @Site    : 
# @File    : 1101-01-QColorDialog.py
# @Software: PyCharm


"""
    在这个例子中，我们从QColorDialog选择一个颜色值,改变背景一个QFrame控件颜色。


"""

from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, QColorDialog,QApplication)
from PyQt5.QtGui import QColor
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        col = QColor(0,0,0)

        self.btn = QPushButton('Dialog',self)
        self.btn.move(20,20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color : %s}" % col.name())
        self.frm.setGeometry(130,22,100,100)

        self.setGeometry(300,300,250,180)
        self.setWindowTitle('Color dialog')
        self.show()


    def showDialog(self):

        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                % col.name())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())