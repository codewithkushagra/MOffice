import tkinter
from tkinter import *
from tkinter.constants import *
from tkinter import ttk

import StaticTable

import globalvalues
import DBMSGetData
import AdminButtonGlobal



def getUserWork(workstatusselected,articlenameselected,contentframe):

    AdminButtonGlobal.CURRENTTABLEFRAME.destroy()

    if workstatusselected=="All" and articlenameselected!="All":

        AdminButtonGlobal.CURRENTTABLEFRAME=tkinter.Frame(contentframe)
        AdminButtonGlobal.CURRENTTABLEFRAME.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(AdminButtonGlobal.CURRENTTABLEFRAME,DBMSGetData.getAllDataOfColumn("RECEIVEDWORK","ALLOTED",articlenameselected))

    elif workstatusselected=="All" and articlenameselected=="All":
    
        AdminButtonGlobal.CURRENTTABLEFRAME=tkinter.Frame(contentframe)
        AdminButtonGlobal.CURRENTTABLEFRAME.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(AdminButtonGlobal.CURRENTTABLEFRAME,DBMSGetData.getAllData("RECEIVEDWORK"))

    elif workstatusselected!="All" and articlenameselected=="All":
        AdminButtonGlobal.CURRENTTABLEFRAME=tkinter.Frame(contentframe)
        AdminButtonGlobal.CURRENTTABLEFRAME.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(AdminButtonGlobal.CURRENTTABLEFRAME,DBMSGetData.getAllDataOfColumn("RECEIVEDWORK","WORKSTATUS",workstatusselected))

    else:
        AdminButtonGlobal.CURRENTTABLEFRAME=tkinter.Frame(contentframe)
        AdminButtonGlobal.CURRENTTABLEFRAME.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(AdminButtonGlobal.CURRENTTABLEFRAME,DBMSGetData.getAllDataByTwoColumn("RECEIVEDWORK","ALLOTED","WORKSTATUS",articlenameselected,workstatusselected))
    
    return






def todaysWorkList(root):


    contentframe=tkinter.Frame(root)
    contentframe.grid(row=0,column=1,ipadx=globalvalues.HEIGHT,ipady=globalvalues.WIDTH-100) 

    tkinter.Label(contentframe,text="Today's Work-",font="Time 14").grid(row=0,column=0,sticky=W,pady=7)

    articlenamelist=["All"]
    try:
        for i in DBMSGetData.getData("TEAMREGISTER","USERNAME"):
            articlenamelist.append(i[0])
    except:
        pass 


    AdminButtonGlobal.CURRENTTABLEFRAME=tkinter.Frame(contentframe)
    AdminButtonGlobal.CURRENTTABLEFRAME.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
    StaticTable.drawTable(AdminButtonGlobal.CURRENTTABLEFRAME,DBMSGetData.getAllData("RECEIVEDWORK"))



    workstatusselected=tkinter.StringVar(contentframe)
    workstatuslist = ["All","Complete","Pending","Past due date"]
    workstatusselected.set("All")
    tkinter.Label(contentframe,text="Work Status:").grid(row=2,column=0,sticky=W)
    tkinter.OptionMenu(contentframe,workstatusselected,*workstatuslist,command=lambda event=1:getUserWork(workstatusselected.get(),articlenameselected.get(),contentframe)).grid(row=2,column=1,sticky=W)



    articlenameselected=tkinter.StringVar(contentframe)
    
    tkinter.Label(contentframe,text="Username:").grid(row=1,column=0,sticky=W)
    articlenamemenu=ttk.Combobox(contentframe,textvariable=articlenameselected)
    articlenamemenu.grid(row=1,column=1,sticky=W)
    articlenamemenu['value']=articlenamelist
    articlenamemenu.current(0)

    articlenamemenu.bind("<<ComboboxSelected>>",lambda event=1:getUserWork(articlenameselected.get(),contentframe))


    AdminButtonGlobal.CURRENTFRAME=contentframe


    return