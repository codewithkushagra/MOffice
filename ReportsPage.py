import tkinter
from tkinter import *
from tkinter.constants import *
import StaticTable
import AdminButtons



def reportList(root):


    contentframe=tkinter.Frame(root)
    contentframe.grid(row=0,column=1)

    tkinter.Label(contentframe,text="Work Reports-").grid(row=0,column=0,sticky=W,pady=7)

    articlenameselected=tkinter.StringVar(contentframe)
    articlenamelist = ["sample1","sample1"]
    articlenameselected.set("None")
    tkinter.Label(contentframe,text="Article Name:").grid(row=1,column=0,sticky=W)
    tkinter.OptionMenu(contentframe,articlenameselected,*articlenamelist).grid(row=1,column=1,sticky=W)


    workstatusselected=tkinter.StringVar(contentframe)
    workstatuslist = ["complete","pending","past due date"]
    workstatusselected.set("None")
    tkinter.Label(contentframe,text="Work Status:").grid(row=1,column=2,sticky=W)
    tkinter.OptionMenu(contentframe,workstatusselected,*workstatuslist).grid(row=1,column=3,sticky=W)


    tableframe=tkinter.Frame(contentframe)
    tableframe.grid(row=3,column=0,sticky=W,ipady=250,ipadx=350,columnspan=25)
    StaticTable.drawTable(tableframe)


    buttonframe=tkinter.Frame(root)
    tkinter.Frame(buttonframe,relief=RIDGE,borderwidth=2).grid(row=0,column=0,rowspan=8,ipady=300,ipadx=100)
    buttonframe.grid(row=0,column=0,rowspan=7,sticky=N)


    AdminButtons.buttonCreate(buttonframe,contentframe,root)


    return