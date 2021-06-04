import tkinter
from tkinter.constants import *
from tkinter import messagebox
import StaticTable




def workList(root):
    tkinter.Label(root,text="Work List-",bg="white").grid(row=0,column=0,sticky=W,pady=7)

    groupnameselected=tkinter.StringVar(root)
    groupnamelist = ["sample1","sample1"]
    groupnameselected.set("None")
    tkinter.Label(root,text="Group Name:",bg="white").grid(row=1,column=0,sticky=W)
    tkinter.OptionMenu(root,groupnameselected,*groupnamelist).grid(row=1,column=1,sticky=W)


    tableframe=tkinter.Frame(root,bg="white")
    tableframe.grid(row=3,column=0,sticky=W,ipady=250,ipadx=350,columnspan=25)
    StaticTable.drawTable(tableframe)
    return