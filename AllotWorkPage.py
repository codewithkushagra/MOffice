import tkinter
from tkinter import *
from tkinter.constants import *
from tkinter import ttk
import StaticTable
import globalvalues
import AdminButtonGlobal

import DBMSGetData


def getUserWork(articlenameselected,contentframe):

    AdminButtonGlobal.CURRENTTABLEFRAME.destroy()

    if articlenameselected!="All":

        AdminButtonGlobal.CURRENTTABLEFRAME=tkinter.Frame(contentframe)
        AdminButtonGlobal.CURRENTTABLEFRAME.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(AdminButtonGlobal.CURRENTTABLEFRAME,DBMSGetData.getAllDataOfColumn("RECEIVEDWORK","ALLOTED",articlenameselected))

    else:
    
        AdminButtonGlobal.CURRENTTABLEFRAME=tkinter.Frame(contentframe)
        AdminButtonGlobal.CURRENTTABLEFRAME.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(AdminButtonGlobal.CURRENTTABLEFRAME,DBMSGetData.getAllData("RECEIVEDWORK"))
    
    return




def allotWorkList(root):

    contentframe=tkinter.Frame(root)
    contentframe.grid(row=0,column=1,ipadx=globalvalues.HEIGHT,ipady=globalvalues.WIDTH-100)

    tkinter.Label(contentframe,text="Allot Work-",font="Time 14").grid(row=0,column=0,sticky=W,pady=10)

    articlenamelist=["All"]
    try:
        for i in DBMSGetData.getData("TEAMREGISTER","USERNAME"):
            articlenamelist.append(i[0])
    except:
        pass 

    

    AdminButtonGlobal.CURRENTTABLEFRAME=tkinter.Frame(contentframe)
    AdminButtonGlobal.CURRENTTABLEFRAME.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
    StaticTable.drawTable(AdminButtonGlobal.CURRENTTABLEFRAME,DBMSGetData.getAllData("RECEIVEDWORK"),True)


    
    

  

    articlenameselected=tkinter.StringVar(contentframe)
    
    tkinter.Label(contentframe,text="Username:").grid(row=1,column=0,sticky=W)
    articlenamemenu=ttk.Combobox(contentframe,textvariable=articlenameselected)
    articlenamemenu.grid(row=1,column=1,sticky=W)
    articlenamemenu['value']=articlenamelist
    articlenamemenu.current(0)

    articlenamemenu.bind("<<ComboboxSelected>>",lambda event=1:getUserWork(articlenameselected.get(),contentframe))

    AdminButtonGlobal.CURRENTFRAME=contentframe

    return