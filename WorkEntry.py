import tkinter
from tkinter.constants import *
from tkinter import messagebox
import FrameSwitcher
import AdminButtons



import globalvalues


def enterWork(root):

    contentframe=tkinter.Frame(root)
    contentframe.grid(row=0,column=1,ipadx=globalvalues.HEIGHT,ipady=globalvalues.WIDTH-100)


    buttonframe=tkinter.Frame(root)
    tkinter.Frame(buttonframe,relief=RIDGE,borderwidth=2,bg="red").grid(row=0,column=0,rowspan=40,ipady=globalvalues.HEIGHT,ipadx=100)
    buttonframe.grid(row=0,column=0,rowspan=40,sticky=N)


    AdminButtons.buttonCreate(buttonframe,contentframe,root)

    
    tkinter.Label(contentframe,text="WORK ENTRY-",font="Time 14").grid(row=0,column=0,sticky=W,pady=7)
    tkinter.Button(contentframe, text="Enter Work",command=lambda:FrameSwitcher.recreateWorkEntrySection(contentframe,root,buttonframe)).grid(row=1,column=0,pady=20,padx=10,sticky=W)
    tkinter.Button(contentframe, text="Register New Party",command=lambda:FrameSwitcher.recreateNewParty(contentframe,root,buttonframe)).grid(row=2,column=0,pady=20,padx=10,sticky=W)
    tkinter.Button(contentframe, text="Register New Group",command=lambda:FrameSwitcher.recreateNewGroup(contentframe,root,buttonframe)).grid(row=3,column=0,pady=20,padx=10,sticky=W)    


    
    return