import tkinter
from tkinter import *
from tkinter.constants import *
import StaticTable

import AdminButtons
import DBMSGetData
import globalvalues


def workDiaryList(root):


    contentframe=tkinter.Frame(root)
    contentframe.grid(row=0,column=1,ipadx=globalvalues.HEIGHT,ipady=globalvalues.WIDTH-100)


    tkinter.Label(contentframe,text="Diary Work-",font="Time 14").grid(row=0,column=0,sticky=W,pady=7)

    groupnameselected=tkinter.StringVar(contentframe)
    groupnamelist = ["sample1","sample1"]
    groupnameselected.set("None")
    tkinter.Label(contentframe,text="Article Name:").grid(row=1,column=0,sticky=W)
    tkinter.OptionMenu(contentframe,groupnameselected,*groupnamelist).grid(row=1,column=1,sticky=W)


    tableframe=tkinter.Frame(contentframe)
    tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
    StaticTable.drawTable(tableframe,DBMSGetData.getAllData("RECEIVEDWORK"))


    buttonframe=tkinter.Frame(root)
    tkinter.Frame(buttonframe,relief=RIDGE,borderwidth=2,bg="red").grid(row=0,column=0,rowspan=40,ipady=globalvalues.HEIGHT,ipadx=100)
    buttonframe.grid(row=0,column=0,rowspan=40,sticky=N)

    AdminButtons.buttonCreate(buttonframe,contentframe,root)


    return

