#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/1 下午3:36
# @Author  : hukezhu
# @Site    : 
# @File    : 1101-02-QFileDialog.py
# @Software: PyCharm

"""
    在这个例子中，我们选择一个带有QFileDialog并显示其内容在QTextEdit

"""

from PyQt5.QtWidgets import (QMainWindow, QTextEdit,QAction,QFileDialog,QApplication)
from PyQt5.QtGui import QIcon
import sys

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'),'Open',self)
        openFile.setShortcut('Ctrl + O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300,300,350,300)
        self.setWindowTitle('File dialog')
        self.show()


    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self,'Open file','/home')

        if fname[0]:
            f = open(fname[0],'r')

        with f :
            data = f.read()
            self.textEdit.setText(data)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


