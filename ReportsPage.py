import tkinter
from tkinter import *
from tkinter.constants import *
import StaticTable
import AdminButtonGlobal

import globalvalues

import DBMSGetData


def getUserWork(workstatusselected,tableframe,articlenameselected,contentframe):

    tableframe.destroy()

    if workstatusselected=="All" and articlenameselected!="All":

        tableframe=tkinter.Frame(contentframe)
        tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(tableframe,DBMSGetData.getAllDataOfColumn("RECEIVEDWORK","ALLOTED",articlenameselected))

    elif workstatusselected=="All" and articlenameselected=="All":
    
        tableframe=tkinter.Frame(contentframe)
        tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(tableframe,DBMSGetData.getAllData("RECEIVEDWORK"))

    elif workstatusselected!="All" and articlenameselected=="All":
        tableframe=tkinter.Frame(contentframe)
        tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(tableframe,DBMSGetData.getAllDataOfColumn("RECEIVEDWORK","WORKSTATUS",workstatusselected))

    else:
        tableframe=tkinter.Frame(contentframe)
        tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(tableframe,DBMSGetData.getAllDataByTwoColumn("RECEIVEDWORK","ALLOTED","WORKSTATUS",articlenameselected,workstatusselected))
    
    return





def reportList(root):


    contentframe=tkinter.Frame(root)
    contentframe.grid(row=0,column=1,ipadx=globalvalues.HEIGHT,ipady=globalvalues.WIDTH-100)

    tkinter.Label(contentframe,text="Work Reports-",font="Time 14").grid(row=0,column=0,sticky=W,pady=7)


    articlenamelist=["All"]
    try:
        for i in DBMSGetData.getData("TEAMREGISTER","USERNAME"):
            articlenamelist.append(i[0])
    except:
        pass 


    tableframe=tkinter.Frame(contentframe)
    tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
    StaticTable.drawTable(tableframe,DBMSGetData.getAllData("RECEIVEDWORK"))



    workstatusselected=tkinter.StringVar(contentframe)
    workstatuslist = ["All","Complete","Pending","Past due date"]
    workstatusselected.set("All")
    tkinter.Label(contentframe,text="Work Status:").grid(row=2,column=0,sticky=W)
    tkinter.OptionMenu(contentframe,workstatusselected,*workstatuslist,command=lambda event=1:getUserWork(workstatusselected.get(),tableframe,articlenameselected.get(),contentframe)).grid(row=2,column=1,sticky=W)



    articlenameselected=tkinter.StringVar(contentframe)
    articlenameselected.set("All")
    tkinter.Label(contentframe,text="Username:").grid(row=1,column=0,sticky=W)
    tkinter.OptionMenu(contentframe,articlenameselected,*articlenamelist,command=lambda event=1:getUserWork(workstatusselected.get(),tableframe,articlenameselected.get(),contentframe)).grid(row=1,column=1,sticky=W)


    

    AdminButtonGlobal.CURRENTFRAME=contentframe


    return