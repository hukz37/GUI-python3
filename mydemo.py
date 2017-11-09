#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/10 上午11:27
# @Author  : hukezhu
# @Site    :
# @File    :
# @Software: PyCharm

import leancloud
import test1
import sys
from PyQt5 import QtWidgets
from test1 import Ui_MainWindow

class MyWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setupUi(self)

    def submit(self):

        todo = Todo()
        string = ''
        if self.tabWidget.currentIndex() == 0:
            string = '问答题:\n\n 问题:  %s \n\n 答案:    %s' %(self.lineEdit.text(),self.textEdit.toPlainText())
            if len(self.lineEdit.text()) == 0:
                self.statusbar.showMessage('内容为空,不允许提交', msecs=0)
                return
            self.textBrowser.setPlainText(string)
            todo.set('questiontype', 0)
            todo.set('questiontype_text','问答题')
            todo.set('question', self.lineEdit.text())
            todo.set('questiondescribe', self.textEdit.toPlainText())
        elif self.tabWidget.currentIndex() == 1:
            print('现在选择的是选择题')
            string = '选择题:\n\n 问题:  %s \n\n 选项:    \n\n    %s\n    %s\n    %s\n    %s\n    %s' %(self.lineEdit_2.text(),self.lineEdit_3.text(),self.lineEdit_4.text(),self.lineEdit_5.text(),self.lineEdit_6.text(),self.lineEdit_7.text())
            if len(self.lineEdit_2.text()) == 0:
                self.statusbar.showMessage('内容为空,不允许提交', msecs=0)
                return
            self.textBrowser.setPlainText(string)
            todo.set('questiontype', 1)
            todo.set('questiontype_text', '选择题')
            todo.set('question', self.lineEdit_2.text())
            todo.set('tkselect',[self.lineEdit_3.text(),self.lineEdit_4.text(),self.lineEdit_5.text(),self.lineEdit_6.text(),self.lineEdit_7.text()])

        todo.save()

        self.statusbar.showMessage('提交成功',msecs=2000)

        self.lineEdit.clear()
        self.textEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()


class Todo(leancloud.Object):
    pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    leancloud.init("jRQRUX9jERMhnVedQNmgulIX-gzGzoHsz", master_key="1DXtrehIWMDGupIrw6g5Y3l2d1D")
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())


