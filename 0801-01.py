#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/1 上午9:30
# @Author  : hukezhu
# @Site    : 
# @File    : 0801-01.py
# @Software: PyCharm

import tkinter as tk

win = tk.Tk()

win.title('Python GUI')

#disable resizing the GUI,传入0,0就不能进行缩放拉伸,最大化按钮也不可用
#当然也可以传入具体的值
win.resizable(0,0)

win.mainloop()