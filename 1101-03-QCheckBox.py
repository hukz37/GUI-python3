#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/1 下午4:37
# @Author  : hukezhu
# @Site    : 
# @File    : 1101-03-QCheckBox.py
# @Software: PyCharm



"""

        在这个例子中，QCheckBox部件用于切换窗口的标题。

"""


import sys
from PyQt5.QtWidgets import QWidget, QCheckBox,QApplication
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()


    def initUI(self):
        cb = QCheckBox('Show title',self)
        cb.move(20,20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('QCheckBox')
        self.show()

    def changeTitle(self,state):

        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('未选中')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


