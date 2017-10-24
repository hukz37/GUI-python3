#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 下午2:10
# @Author  : Aries
# @Site    : 
# @File    : 1016-05-创建菜单栏.py
# @Software: PyCharm


import sys
from PyQt5.QtWidgets import qApp,QAction,QApplication,QMainWindow
from PyQt5.QtGui import QIcon


class Exp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        exitAction = QAction(QIcon('123.png'),'&退出程序',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit app')
        exitAction.triggered.connect(qApp.quit)

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&文件')
        fileMenu.addAction(exitAction)

        self.statusBar()

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('menubar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exp()
    sys.exit(app.exec_())