#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 下午3:08
# @Author  : Aries
# @Site    : 
# @File    : 1016-07-工具栏、菜单栏、状态栏整合.py
# @Software: PyCharm

import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit,QApplication,qApp,QAction
from PyQt5.QtGui import QIcon



class Exp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        text = QTextEdit()
        self.setCentralWidget(text)

        exitAction = QAction(QIcon('123.png'),'退出',self)
        exitAction.setShortcut('Ctrl + Q')
        exitAction.setStatusTip('Press and quit !')
        exitAction.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&列表')
        fileMenu.addAction(exitAction)

        self.statusBar()

        tbar = self.addToolBar('Exit')
        tbar.addAction(exitAction)

        self.setGeometry(400,200,600,400)
        self.setWindowTitle('整合')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exp()
    sys.exit(app.exec_())

