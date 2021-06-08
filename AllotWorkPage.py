import tkinter
from tkinter import *
from tkinter.constants import *
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
    articlenameselected.set("All")
    tkinter.Label(contentframe,text="Username:").grid(row=1,column=0,sticky=W)
    tkinter.OptionMenu(contentframe,articlenameselected,*articlenamelist,command=lambda event=1:getUserWork(articlenameselected.get(),contentframe)).grid(row=1,column=1,sticky=W)

    

    AdminButtonGlobal.CURRENTFRAME=contentframe

    return