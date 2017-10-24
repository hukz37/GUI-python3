#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 下午12:56
# @Author  : Aries
# @Site    : 
# @File    : 1016-01.py
# @Software: PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Exp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,200,300,200)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('123.png'))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exp()
    sys.exit(app.exec_())


