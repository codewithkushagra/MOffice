import tkinter
from tkinter.constants import *
import AdminButtons




def admin(root):







    buttonframe=tkinter.Frame(root)
    buttonframe.grid(row=0,column=0,rowspan=7)

    AdminButtons.buttonCreate(buttonframe)    



    contentframe=tkinter.Frame(root)
    contentframe.grid(row=0,column=1)

    contentempty=tkinter.Frame(contentframe,bg="white")
    contentempty.grid(row=0,column=0,ipady=300,ipadx=350)

    contentwork=tkinter.Frame(contentframe,bg="green")
    contentwork.grid(row=0,column=0,sticky=NSEW)

    
    
    return