# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:38:22 2021

@author: M CHOUCHI
"""
from tkinter import Tk, Label, Button

class ExempleGUI:
    def __init__(self, master,i):
        self.master = master
        self.listebouton =[]
        for j in range(0,i):            
            self.listebouton.append(("question requête "+str(j+1),Button(master, text="button_"+str(j+1), command=lambda c=j: self.OnButtonClick(c))))            
            self.listebouton[j][1].pack()
                        
    def OnButtonClick(self, j):
        print(self.listebouton[j][0])

root = Tk()
my_gui = ExempleGUI(root,3)
root.mainloop()
