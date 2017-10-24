#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 下午1:29
# @Author  : Aries
# @Site    : 
# @File    : 1016-02.py
# @Software: PyCharm


import sys
from PyQt5.QtWidgets import QWidget,QToolTip,QPushButton,QApplication
from PyQt5.QtGui import QFont



class Exp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        #设置提示信息的文字字体和大小信息
        QToolTip.setFont(QFont('SansSerif',10))

        #这里为整个Exp窗口设置提示内容,支持html语法(这里是加粗)
        self.setToolTip('This is a <b>widget</b>')


        btn = QPushButton('Push',self)
        #这里为按钮设置提示内容
        btn.setToolTip('Press and Push!')
        btn.resize(btn.sizeHint())
        btn.move(40 , 50)

        self.setGeometry(200,300,400,400)
        self.setWindowTitle('setToolTip')
        self.show()



if __name__  == '__main__':
    app = QApplication(sys.argv)
    ex = Exp()
    sys.exit(app.exec_())

