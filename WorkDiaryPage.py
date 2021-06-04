import tkinter
from tkinter import *
from tkinter.constants import *
import StaticTable




def workDiaryList(root):
    tkinter.Label(root,text="Diary Work-",bg="white").grid(row=0,column=0,sticky=W,pady=7)

    groupnameselected=tkinter.StringVar(root)
    groupnamelist = ["sample1","sample1"]
    groupnameselected.set("None")
    tkinter.Label(root,text="Article Name:",bg="white").grid(row=1,column=0,sticky=W)
    tkinter.OptionMenu(root,groupnameselected,*groupnamelist).grid(row=1,column=1,sticky=W)


    tableframe=tkinter.Frame(root,bg="white")
    tableframe.grid(row=3,column=0,sticky=W,ipady=250,ipadx=350,columnspan=25)
    StaticTable.drawTable(tableframe)

    return

