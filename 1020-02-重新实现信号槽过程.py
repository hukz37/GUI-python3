#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 下午2:02
# @Author  : Aries
# @Site    : 
# @File    : 1020-02-重新实现信号槽过程.py
# @Software: PyCharm


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget

class Exp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,400,400)
        self.setWindowTitle('Escape')

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_Alt:
            self.setWindowTitle('Alt')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exp()
    ex.show()
    sys.exit(app.exec_())


