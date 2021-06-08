import tkinter
from tkinter import *
from tkinter.constants import *
import StaticTable

import AdminButtons
import DBMSGetData
import AdminButtonGlobal
import globalvalues


def getUserWork(tableframe,articlenameselected,contentframe):

    tableframe.destroy()

    if articlenameselected!="All":

        tableframe=tkinter.Frame(contentframe)
        tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(tableframe,DBMSGetData.getAllDataOfColumn("RECEIVEDWORK","ALLOTED",articlenameselected))

    else:
    
        tableframe=tkinter.Frame(contentframe)
        tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(tableframe,DBMSGetData.getAllData("RECEIVEDWORK"))
    
    return



def workDiaryList(root):


    contentframe=tkinter.Frame(root)
    contentframe.grid(row=0,column=1,ipadx=globalvalues.HEIGHT,ipady=globalvalues.WIDTH-100)


    tkinter.Label(contentframe,text="Diary Work-",font="Time 14").grid(row=0,column=0,sticky=W,pady=7)

    articlenamelist=["All"]
    try:
        for i in DBMSGetData.getData("TEAMREGISTER","USERNAME"):
            articlenamelist.append(i[0])
    except:
        pass 


    tableframe=tkinter.Frame(contentframe)
    tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
    StaticTable.drawTable(tableframe,DBMSGetData.getAllData("RECEIVEDWORK"))




    articlenameselected=tkinter.StringVar(contentframe)
    articlenameselected.set("All")
    tkinter.Label(contentframe,text="Username:").grid(row=1,column=0,sticky=W)
    tkinter.OptionMenu(contentframe,articlenameselected,*articlenamelist,command=lambda event=1:getUserWork(tableframe,articlenameselected.get(),contentframe)).grid(row=1,column=1,sticky=W)


    AdminButtonGlobal.CURRENTFRAME=contentframe


    return

