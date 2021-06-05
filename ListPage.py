import tkinter
from tkinter.constants import *
from tkinter import messagebox
import StaticTable
import AdminButtons




def workList(root):


    contentframe=tkinter.Frame(root)
    contentframe.grid(row=0,column=1)


    tkinter.Label(contentframe,text="Work List-").grid(row=0,column=0,sticky=W,pady=7)

    groupnameselected=tkinter.StringVar(contentframe)
    groupnamelist = ["sample1","sample1"]
    groupnameselected.set("None")
    tkinter.Label(contentframe,text="Group Name:").grid(row=1,column=0,sticky=W)
    tkinter.OptionMenu(contentframe,groupnameselected,*groupnamelist).grid(row=1,column=1,sticky=W)

    partynameselected=tkinter.StringVar(contentframe)
    partynamelist = ["sample1","sample1"]
    partynameselected.set("None")
    tkinter.Label(contentframe,text="Party Name:").grid(row=1,column=2,sticky=W)
    tkinter.OptionMenu(contentframe,partynameselected,*partynamelist).grid(row=1,column=3,sticky=W)

    departmentselected=tkinter.StringVar(contentframe)
    departmentlist = ["sample1","sample1"]
    departmentselected.set("None")
    tkinter.Label(contentframe,text="Department:").grid(row=1,column=4,sticky=W)
    tkinter.OptionMenu(contentframe,departmentselected,*departmentlist).grid(row=1,column=5,sticky=W)


    tableframe=tkinter.Frame(contentframe)
    tableframe.grid(row=3,column=0,sticky=W,ipady=250,ipadx=350,columnspan=25)
    StaticTable.drawTable(tableframe)


    buttonframe=tkinter.Frame(root)
    tkinter.Frame(buttonframe,relief=RIDGE,borderwidth=2).grid(row=0,column=0,rowspan=8,ipady=300,ipadx=100)
    buttonframe.grid(row=0,column=0,rowspan=7,sticky=N)

    AdminButtons.buttonCreate(buttonframe,contentframe,root)
    return