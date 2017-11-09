

import tabbar_test
import test
import sys
import leancloud
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout,QTextEdit,QLineEdit,QCheckBox,QPushButton,QMainWindow,QDialog
from PyQt5.QtCore import Qt

class Exp(QWidget):

    def __init__(self):
        super().__init__()
        leancloud.init("jRQRUX9jERMhnVedQNmgulIX-gzGzoHsz", master_key="1DXtrehIWMDGupIrw6g5YldD")
        self.initUI()

    def initUI(self):

        self.cb = QCheckBox('选择题',self)
        self.cb.toggle()
        self.cb.stateChanged.connect(self.checkBoxClick)

        self.btn = QPushButton('提交', self)
        #btn.move(200,300)
        self.btn.clicked.connect(self.showDialog)
        self.btn.resize(self.btn.sizeHint())

        self.title = QLabel('Title')
        self.author = QLabel('Author')
        self.review = QLabel('Review')

        self.titleEdit = QLineEdit()
        self.authorEdit = QLineEdit()
        self.reviewEdit = QTextEdit()



        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.cb,1,1)
        grid.addWidget(self.title,2,0)
        grid.addWidget(self.titleEdit,2,1)
        grid.addWidget(self.author,3,0)
        grid.addWidget(self.authorEdit,3,1)
        grid.addWidget(self.review,4,0)
        grid.addWidget(self.reviewEdit,4,1,5,1)
        grid.addWidget(self.btn,10,1)

        self.setGeometry(200,200,600,600)
        self.setLayout(grid)

        self.setWindowTitle('增加题库')

        self.show()

    def checkBoxClick(self, state):
        if state == Qt.Checked:
            print('选择题')
        else:
            print('问答题')


    def showDialog(self):
        print('提交')
        todo = Todo()
        todo.set('type',0)
        todo.set('title', self.titleEdit.text())
        todo.set('content', self.reviewEdit.toPlainText())
        todo.set('tkselect',['A. 张三','B.李四','C.王五','D.赵六','E.吴七'])
        todo.save()

        self.titleEdit.clear()
        self.reviewEdit.clear()


class Todo(leancloud.Object):
    pass

class qtDesigner(QDialog):
    def __init__(self):
        super().__init__()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exp()
    sys.exit(app.exec_())
    # app = QApplication(sys.argv)
    # MainWindow = QMainWindow()
    # ui = tabbar_test.Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())





