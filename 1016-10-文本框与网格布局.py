#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 下午4:09
# @Author  : Aries
# @Site    : 
# @File    : 1016-10-文本框与网格布局.py
# @Software: PyCharm


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout,QTextEdit,QLineEdit

class Exp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(title,1,0)
        grid.addWidget(titleEdit,1,1)
        grid.addWidget(author,2,0)
        grid.addWidget(authorEdit,2,1)
        grid.addWidget(review,3,0)
        grid.addWidget(reviewEdit,3,1,5,1)

        self.setGeometry(300,300,400,400)
        self.setLayout(grid)

        self.setWindowTitle('review')

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exp()
    sys.exit(app.exec_())


