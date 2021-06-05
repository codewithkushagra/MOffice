import tkinter
from tkinter.constants import *
from tkinter import messagebox
import FrameSwitcher
import AdminButtons

def enterWork(root):

    contentframe=tkinter.Frame(root)
    contentframe.grid(row=0,column=1)


    buttonframe=tkinter.Frame(root)
    tkinter.Frame(buttonframe,relief=RIDGE,borderwidth=2).grid(row=0,column=0,rowspan=8,ipady=300,ipadx=100)
    buttonframe.grid(row=0,column=0,rowspan=7,sticky=N)


    AdminButtons.buttonCreate(buttonframe,contentframe,root)


    tkinter.Label(contentframe,text="WORK ENTRY-").grid(row=0,column=0,sticky=W,pady=7)
    tkinter.Button(contentframe, text="Enter Work",command=lambda:FrameSwitcher.recreateWorkEntrySection(contentframe,root,buttonframe)).grid(row=1,column=0,pady=200,padx=10)
    tkinter.Button(contentframe, text="Register New Party",command=lambda:FrameSwitcher.recreateNewParty(contentframe,root,buttonframe)).grid(row=1,column=1,pady=200,padx=10)
    tkinter.Button(contentframe, text="Register New Group",command=lambda:FrameSwitcher.recreateNewGroup(contentframe,root,buttonframe)).grid(row=1,column=2,pady=200,padx=10)    


    
    return