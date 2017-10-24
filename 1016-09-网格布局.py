#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 下午3:54
# @Author  : Aries
# @Site    : 
# @File    : 1016-09-网格布局.py
# @Software: PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout,QPushButton


class Exp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        name = ['Cal','Bac', ' ', 'Close' ,
                '7','8','9','/',
                '4','5','6','*',
                '1','2','3','-',
                '0','.','=','+']

        position = [(i,j) for  i in range(5) for j in range(4)]

        for name , position in zip(name,position):
            if name == ' ':
                continue
            button = QPushButton(name)
            grid.addWidget(button,*position)

        self.move(300,150)
        self.setWindowTitle("简单计算器")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exp()
    sys.exit(app.exec_())

