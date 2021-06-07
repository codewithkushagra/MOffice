import tkinter
from tkinter import *
from tkinter.constants import *
import StaticTable
import AdminButtons

import globalvalues

import DBMSGetData

def reportList(root):


    contentframe=tkinter.Frame(root)
    contentframe.grid(row=0,column=1,ipadx=globalvalues.HEIGHT,ipady=globalvalues.WIDTH-100)

    tkinter.Label(contentframe,text="Work Reports-",font="Time 14").grid(row=0,column=0,sticky=W,pady=7)

    articlenameselected=tkinter.StringVar(contentframe)
    articlenamelist = ["sample1","sample1"]
    articlenameselected.set("None")
    tkinter.Label(contentframe,text="Article Name:").grid(row=1,column=0,sticky=W)
    tkinter.OptionMenu(contentframe,articlenameselected,*articlenamelist).grid(row=1,column=1,sticky=W)


    workstatusselected=tkinter.StringVar(contentframe)
    workstatuslist = ["complete","pending","past due date"]
    workstatusselected.set("None")
    tkinter.Label(contentframe,text="Work Status:").grid(row=2,column=0,sticky=W)
    tkinter.OptionMenu(contentframe,workstatusselected,*workstatuslist).grid(row=2,column=1,sticky=W)


    tableframe=tkinter.Frame(contentframe)
    tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
    StaticTable.drawTable(tableframe,DBMSGetData.getAllData("RECEIVEDWORK"))


    buttonframe=tkinter.Frame(root)
    tkinter.Frame(buttonframe,relief=RIDGE,borderwidth=2,bg="red").grid(row=0,column=0,rowspan=40,ipady=globalvalues.HEIGHT,ipadx=100)
    buttonframe.grid(row=0,column=0,rowspan=40,sticky=N)


    AdminButtons.buttonCreate(buttonframe,contentframe,root)


    return