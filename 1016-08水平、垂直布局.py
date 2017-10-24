#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 下午3:27
# @Author  : Aries
# @Site    : 
# @File    : 1016-08水平、垂直布局.py
# @Software: PyCharm




#   QVBoxLayout和QHBoxLayout，V代表Vertical，H代表Horizontal，分别控制竖向和横向的布局




import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout

class Exp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')


#   addStrtch()，它的作用是在布局中添加空白，并把非空白内容顶到布局的尾部（对于QHBoxLayout()而言是右边，对于QVBoxLayout()而言是底部），这也是按钮始终能够在窗口右下角的原因。

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle("Layout Management")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exp()
    sys.exit(app.exec_())


