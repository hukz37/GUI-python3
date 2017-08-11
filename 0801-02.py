#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/1 上午10:08
# @Author  : hukezhu
# @Site    : 
# @File    : 0801-02.py
# @Software: PyCharm

import tkinter as tk
from tkinter import ttk

win = tk.Tk()

#ttk.Label(win,text="Hello World!").grid(column=0,row = 0)

aLabel = ttk.Label(win , text = '请输入名称')
aLabel.grid(column = 0, row = 0)

def ClickAction():
    action.configure(text="** I have been Clicked! **" + name.get() + number.get())
    aLabel.configure(foreground='red')

action = ttk.Button(win,text = "点击" ,command=ClickAction)
action.grid(column = 2, row = 1)
#Disable the Button Widget
#action.configure(state='disabled')

#ttk.Label(win, text = '请输入名称:').grid(column=0,row=0)

name = tk.StringVar()
nameEntered = ttk.Entry(win,width=12,textvariable=name)
nameEntered.grid(column=0,row = 1)
nameEntered.focus()


ttk.Label(win,text = "Choose a number:").grid(column=1,row=0)
number = tk.StringVar()
#state参数限制了只读,不能修改
numberChosen = ttk.Combobox(win,width=12,textvariable=number,state='readonly')
numberChosen['values']=(1,2,3,52,100,2367)
numberChosen.grid(column = 1, row = 1)
numberChosen.current(0)


chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text = "Disabled" , variable = chVarDis, state = 'disabled')
check1.select()
check1.grid(column = 0, row = 4, sticky = tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text = 'UnChecked', variable = chVarUn)
check2.deselect()
check2.grid(column =  1, row = 4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win,text='Enabled',variable=chVarEn)
check3.select()
check3.grid(column = 2, row = 4 ,sticky = tk.W)



win.mainloop()

#The reson why it became so small is that we added a widget to our form. Without
#a widget ,tkinter uses a default size.

