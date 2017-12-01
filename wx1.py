from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread,pyqtSignal
import itchat
import time,os
import shutil
import re

from itchat.content import *

from wx import weChatWord

from PyQt5.Qt import pyqtSetPickleProtocol



class mainwindowapp(QMainWindow,wechatunrecall.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.createActions()
        self.createTrayIcon()
        self.pushButton.clicked.connect(self.saveLog)
        self.pushButton_2.clicked.connect(self.clearlog)
        self.pushButton_3.clicked.connect(self.houtai)
        self.trayIcon.activated.connect(self.iconActivated)
        timeArray = time.localtime()
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        self.setLog(otherStyleTime+"，程序运行时，请用手机扫描弹出的二维码进行登录，并确保电脑上自带的Window照片查"
                                   "看器可用，撤回的图片文件等可下载附件连同运行日志保存在程序目录下BackUp文件夹中。\n")
        self.weChatBigWord()


    def saveLog(self):
        '''
        保存日志
        :return:
        '''
        if not os.path.exists(".\\BackUp\\"):
            os.mkdir(".\\BackUp\\")
        timeArray = time.localtime()
        otherStyleTime = time.strftime("%Y-%m-%d%H%M%S", timeArray)
        text=self.textBrowser.toPlainText()
        logPath=".\\BackUp\\"+otherStyleTime+'.txt'
        with open(logPath,'w') as f:
            f.write(text)

    def setLog(self,msg):
        '''
        往运行日志窗口写撤回消息的内容
        :param msg:
        :return:
        '''
        self.textBrowser.append(msg)

    def createTrayIcon(self):
        '''
        创建托盘图标，可以让程序最小化到windows托盘中运行
        :return:
        '''
        self.trayIconMenu=QMenu(self)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)
        self.trayIcon=QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)
        self.trayIcon.setIcon(QIcon('./media/images/maincion.png'))
        self.setWindowIcon(QIcon('./media/images/maincion.png'))
        self.trayIcon.show()

    def createActions(self):
        '''
        为托盘图标添加功能
        :return:
        '''
        self.restoreAction=QAction("恢复",self,triggered=self.showNormal)
        self.quitAction=QAction("退出",self,triggered=QApplication.instance().quit)


    def iconActivated(self,reason):
        '''
        激活托盘功能
        :param reason:
        :return:
        '''
        if reason in (QSystemTrayIcon.Trigger, QSystemTrayIcon.DoubleClick):
            self.showNormal()


    def houtai(self):
        self.hide()

    def clearlog(self):
        self.textBrowser.clear()


    def weChatBigWord(self):
        '''
        weChatThread类实例化，并启动线程
        :return:
        '''
        self.wcBWThread=weChatWord()
        self.wcBWThread.getMsgSignal.connect(self.setLog)
        self.wcBWThread.start()