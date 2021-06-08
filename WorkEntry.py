import tkinter
from tkinter.constants import *
from tkinter import messagebox
import FrameSwitcher
import AdminButtons
import AdminButtonGlobal


import globalvalues


def enterWork(root):

    contentframe=tkinter.Frame(root)
    contentframe.grid(row=0,column=1,ipadx=globalvalues.HEIGHT,ipady=globalvalues.WIDTH-100)

    AdminButtonGlobal.CURRENTFRAME=contentframe

    
    tkinter.Label(contentframe,text="WORK ENTRY-",font="Time 14").grid(row=0,column=0,sticky=W,pady=7)
    tkinter.Button(contentframe, text="Enter Work",command=lambda:FrameSwitcher.recreateWorkEntrySection(contentframe,root)).grid(row=1,column=0,pady=20,padx=10,sticky=W)
    tkinter.Button(contentframe, text="Register New Party",command=lambda:FrameSwitcher.recreateNewParty(contentframe,root)).grid(row=2,column=0,pady=20,padx=10,sticky=W)
    tkinter.Button(contentframe, text="Register New Group",command=lambda:FrameSwitcher.recreateNewGroup(contentframe,root)).grid(row=3,column=0,pady=20,padx=10,sticky=W)    


    
    return