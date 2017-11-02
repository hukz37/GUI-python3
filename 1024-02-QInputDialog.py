#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/24 下午3:18
# @Author  : hukezhu
# @Site    : 
# @File    : 1024-02-QInputDialog.py
# @Software: PyCharm


import sys
from PyQt5.QtWidgets import (QWidget,QPushButton,QLineEdit,QInputDialog,QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.btn = QPushButton('按钮', self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130,22)

        self.setGeometry(300,300,390,150)
        self.setWindowTitle('demo')
        self.show()

    def showDialog(self):

        text, ok = QInputDialog.getText(self,'输入对话框','输入你的姓名:')

        if ok:
            self.le.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

