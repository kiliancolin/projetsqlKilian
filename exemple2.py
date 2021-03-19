# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:43:33 2021

@author: M CHOUCHI
"""
from tkinter import *

root = Tk()

files = [] 
btn = []   

for i in range(5): 
    files.append("sql "+str(i))

for i in range(len(files)):     
    btn.append(Button(root, text=files[i], command=lambda c=i: print(btn[c].cget("text"))))
    btn[i].pack() 
root.mainloop()
