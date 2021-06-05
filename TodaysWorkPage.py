import tkinter
from tkinter import *
from tkinter.constants import *
import StaticTable

import AdminButtons


def todaysWorkList(root):


    contentframe=tkinter.Frame(root)
    contentframe.grid(row=0,column=1)    

    tkinter.Label(contentframe,text="Today's Work-").grid(row=0,column=0,sticky=W,pady=7)

    groupnameselected=tkinter.StringVar(contentframe)
    groupnamelist = ["sample1","sample1"]
    groupnameselected.set("None")
    tkinter.Label(contentframe,text="Article Name:").grid(row=1,column=0,sticky=W)
    tkinter.OptionMenu(contentframe,groupnameselected,*groupnamelist).grid(row=1,column=1,sticky=W)


    tableframe=tkinter.Frame(contentframe)
    tableframe.grid(row=3,column=0,sticky=W,ipady=250,ipadx=350,columnspan=25)
    StaticTable.drawTable(tableframe)


    buttonframe=tkinter.Frame(root)
    tkinter.Frame(buttonframe,relief=RIDGE,borderwidth=2).grid(row=0,column=0,rowspan=8,ipady=300,ipadx=100)
    buttonframe.grid(row=0,column=0,rowspan=7,sticky=N)

    AdminButtons.buttonCreate(buttonframe,contentframe,root)


    return