import tkinter
from tkinter.constants import *
from tkinter import messagebox
import FrameSwitcher


def enterWork(workentry,newgroup,newparty,workentrysection):
    tkinter.Label(workentry,text="WORK ENTRY-",bg="white").grid(row=0,column=0,sticky=W,pady=7)
    tkinter.Button(workentry, text="Enter Work",command=lambda:FrameSwitcher.switchAdminFrame(workentrysection)).grid(row=1,column=0,pady=200,padx=10)
    tkinter.Button(workentry, text="Register New Party",command=lambda:FrameSwitcher.switchAdminFrame(newparty)).grid(row=1,column=1,pady=200,padx=10)
    tkinter.Button(workentry, text="Register New Group",command=lambda:FrameSwitcher.switchAdminFrame(newgroup)).grid(row=1,column=2,pady=200,padx=10)    
    return