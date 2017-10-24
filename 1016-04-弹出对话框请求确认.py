#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 下午1:57
# @Author  : Aries
# @Site    : 
# @File    : 1016-04-弹出对话框请求确认.py
# @Software: PyCharm


import sys
from PyQt5.QtWidgets import QWidget, QApplication ,QMessageBox

class Exp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200,300,400,400)
        self.setWindowTitle('退出')
        self.show()

    def closeEvent(self,event):
        reply = QMessageBox.question(self,'Message','You sure to quit ?', QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exp()
    sys.exit(app.exec_())