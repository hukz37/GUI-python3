#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/6 16:18
# @Author  : hukezhu
# @Site    :
# @File    :
# @Software: PyCharm


import itchat

def lc():
    print("Finash Login!")
def ec():
    print("exit")

itchat.auto_login(loginCallback=lc, exitCallback=ec,enableCmdQR=2)

