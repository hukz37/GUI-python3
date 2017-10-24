#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 下午2:34
# @Author  : Aries
# @Site    : 
# @File    : 1016-06-工具栏.py
# @Software: PyCharm

import sys
from PyQt5.QtWidgets import QApplication,qApp,QMainWindow,QAction
from PyQt5.QtGui import QIcon


import sys
from PyQt5.QtWidgets import QApplication,qApp,QMainWindow,QAction
from PyQt5.QtGui import QIcon

class Toolbar(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        exitAction = QAction(QIcon('123.png'),'&退出',self)
        exitAction.setShortcut('Ctrl + Q')
        exitAction.setStatusTip('Be careful')
        exitAction.triggered.connect(qApp.quit)
        self.toolbar = self.addToolBar('Exitoo')
        self.toolbar.addAction(exitAction)

        self.statusBar()

        self.setGeometry(300,300,400,240)
        self.setWindowTitle("工具栏")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Toolbar()
    sys.exit(app.exec_())

