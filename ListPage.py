from os import getgrouplist
import tkinter
from tkinter.constants import *
from tkinter import messagebox
from tkinter import ttk
import StaticTable

import DBMSGetData
import globalvalues
import AdminButtonGlobal

partynamemenu=ttk.Combobox
groupnamemenu=ttk.Combobox
contentframe=tkinter.Frame


def getGroupData(departmentselected,partynameselected,groupnameselected):

    AdminButtonGlobal.CURRENTTABLEFRAME.destroy()
    if partynameselected!="All" and departmentselected=="All":
        
        panlist=DBMSGetData.getOneForOne("GROUPANDPARTYDETAILS","PANNUMBER","PARTYNAME",partynameselected)
        totalwork=DBMSGetData.getAllDataOfColumn("RECEIVEDWORK","PANNUMBER",panlist[0])
        AdminButtonGlobal.CURRENTTABLEFRAME=tkinter.Frame(contentframe)
        AdminButtonGlobal.CURRENTTABLEFRAME.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(AdminButtonGlobal.CURRENTTABLEFRAME,totalwork)

    elif partynameselected=="All" and departmentselected!="All":
        
        panlist=DBMSGetData.getWhereData("GROUPANDPARTYDETAILS","PANNUMBER","GROUPNAME",groupnameselected)
        totalwork=[]
        for i in panlist:
            totalwork+=DBMSGetData.getAllDataByTwoColumn("RECEIVEDWORK","PANNUMBER","DEPARTMENT",i[0],departmentselected)

        AdminButtonGlobal.CURRENTTABLEFRAME=tkinter.Frame(contentframe)
        AdminButtonGlobal.CURRENTTABLEFRAME.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(AdminButtonGlobal.CURRENTTABLEFRAME,totalwork)

    elif partynameselected!="All" and departmentselected!="All":

        panlist=DBMSGetData.getOneForOne("GROUPANDPARTYDETAILS","PANNUMBER","PARTYNAME",partynameselected)
        totalwork=DBMSGetData.getAllDataByTwoColumn("RECEIVEDWORK","PANNUMBER","DEPARTMENT",panlist[0],departmentselected)
        AdminButtonGlobal.CURRENTTABLEFRAME=tkinter.Frame(contentframe)
        AdminButtonGlobal.CURRENTTABLEFRAME.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(AdminButtonGlobal.CURRENTTABLEFRAME,totalwork)
        

    else:
        panlist=DBMSGetData.getWhereData("GROUPANDPARTYDETAILS","PANNUMBER","GROUPNAME",groupnameselected)
        totalwork=[]
        for i in panlist:
            totalwork+=DBMSGetData.getAllDataOfColumn("RECEIVEDWORK","PANNUMBER",i[0])
        
        AdminButtonGlobal.CURRENTTABLEFRAME=tkinter.Frame(contentframe)
        AdminButtonGlobal.CURRENTTABLEFRAME.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(AdminButtonGlobal.CURRENTTABLEFRAME,totalwork)
    
    return



def getPartyNameMenu(groupnameselected,departmentselected):
    
    AdminButtonGlobal.CURRENTTABLEFRAME.destroy()
    
    partynamelist = ["All"]
    
    global partynamemenu


    if groupnameselected=="All" and departmentselected=="All":
        

        try: 
            partynamemenu['value']=partynamelist
            partynamemenu.current(0)
        except:
            pass

        AdminButtonGlobal.CURRENTTABLEFRAME=tkinter.Frame(contentframe)
        AdminButtonGlobal.CURRENTTABLEFRAME.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(AdminButtonGlobal.CURRENTTABLEFRAME,DBMSGetData.getAllData("RECEIVEDWORK"))
        
    elif groupnameselected=="All" and departmentselected!="All":
        

        try: 
            partynamemenu['value']=partynamelist
            partynamemenu.current(0)
        except:
            pass

        AdminButtonGlobal.CURRENTTABLEFRAME=tkinter.Frame(contentframe)
        AdminButtonGlobal.CURRENTTABLEFRAME.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(AdminButtonGlobal.CURRENTTABLEFRAME,DBMSGetData.getAllDataOfColumn("RECEIVEDWORK","DEPARTMENT",departmentselected))
    
    elif groupnameselected!="All" and departmentselected!="All":
        for i in DBMSGetData.getWhereData("GROUPANDPARTYDETAILS","PARTYNAME","GROUPNAME",groupnameselected):
            partynamelist.append(i[0])
        try: 
            partynamemenu['value']=partynamelist
            partynamemenu.current()
        except:
            pass
        
        
        
        panlist=DBMSGetData.getWhereData("GROUPANDPARTYDETAILS","PANNUMBER","GROUPNAME",groupnameselected)
        totalwork=[]
        for i in panlist:
            totalwork+=DBMSGetData.getAllDataByTwoColumn("RECEIVEDWORK","PANNUMBER","DEPARTMENT",i[0],departmentselected)

        AdminButtonGlobal.CURRENTTABLEFRAME=tkinter.Frame(contentframe)
        AdminButtonGlobal.CURRENTTABLEFRAME.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(AdminButtonGlobal.CURRENTTABLEFRAME,totalwork)  

    else:
        for i in DBMSGetData.getWhereData("GROUPANDPARTYDETAILS","PARTYNAME","GROUPNAME",groupnameselected):
            partynamelist.append(i[0])
        print(partynamelist)
        try: 
            partynamemenu['value']=partynamelist
            partynamemenu.current()
        except:
            pass
        
        panlist=DBMSGetData.getWhereData("GROUPANDPARTYDETAILS","PANNUMBER","GROUPNAME",groupnameselected)
        totalwork=[]
        for i in panlist:
            totalwork+=DBMSGetData.getAllDataOfColumn("RECEIVEDWORK","PANNUMBER",i[0])
        
        AdminButtonGlobal.CURRENTTABLEFRAME=tkinter.Frame(contentframe)
        AdminButtonGlobal.CURRENTTABLEFRAME.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(AdminButtonGlobal.CURRENTTABLEFRAME,totalwork)
        
    
    
    return


def getDepartmentTable(contentframe,departmentselected,groupnameselected,partynameselected):
    
    AdminButtonGlobal.CURRENTTABLEFRAME.destroy()
    
    if groupnameselected=="All" and departmentselected!="All":
        print(departmentselected)
        AdminButtonGlobal.CURRENTTABLEFRAME=tkinter.Frame(contentframe)
        AdminButtonGlobal.CURRENTTABLEFRAME.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(AdminButtonGlobal.CURRENTTABLEFRAME,DBMSGetData.getAllDataOfColumn("RECEIVEDWORK","DEPARTMENT",departmentselected))
    elif departmentselected=="All" and groupnameselected=="All":
        AdminButtonGlobal.CURRENTTABLEFRAME=tkinter.Frame(contentframe)
        AdminButtonGlobal.CURRENTTABLEFRAME.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(AdminButtonGlobal.CURRENTTABLEFRAME,DBMSGetData.getAllData("RECEIVEDWORK"))
    elif groupnameselected!="All" and departmentselected=="All" and partynameselected=="All":
        panlist=DBMSGetData.getWhereData("GROUPANDPARTYDETAILS","PANNUMBER","GROUPNAME",groupnameselected)
        totalwork=[]
        for i in panlist:
            totalwork+=DBMSGetData.getAllDataOfColumn("RECEIVEDWORK","PANNUMBER",i[0])
        
        AdminButtonGlobal.CURRENTTABLEFRAME=tkinter.Frame(contentframe)
        AdminButtonGlobal.CURRENTTABLEFRAME.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(AdminButtonGlobal.CURRENTTABLEFRAME,totalwork)

    elif departmentselected!="All" and groupnameselected!="All" and partynameselected=="All":
        panlist=DBMSGetData.getWhereData("GROUPANDPARTYDETAILS","PANNUMBER","GROUPNAME",groupnameselected)
        totalwork=[]
        for i in panlist:
            totalwork+=DBMSGetData.getAllDataByTwoColumn("RECEIVEDWORK","PANNUMBER","DEPARTMENT",i[0],departmentselected)

        AdminButtonGlobal.CURRENTTABLEFRAME=tkinter.Frame(contentframe)
        AdminButtonGlobal.CURRENTTABLEFRAME.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(AdminButtonGlobal.CURRENTTABLEFRAME,totalwork)
    elif partynameselected!="All" and departmentselected=="All":
        panlist=DBMSGetData.getOneForOne("GROUPANDPARTYDETAILS","PANNUMBER","PARTYNAME",partynameselected)
        totalwork=DBMSGetData.getAllDataOfColumn("RECEIVEDWORK","PANNUMBER",panlist[0])
        AdminButtonGlobal.CURRENTTABLEFRAME=tkinter.Frame(contentframe)
        AdminButtonGlobal.CURRENTTABLEFRAME.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(AdminButtonGlobal.CURRENTTABLEFRAME,totalwork)
    elif partynameselected!="All" and departmentselected!="All":
        panlist=DBMSGetData.getOneForOne("GROUPANDPARTYDETAILS","PANNUMBER","PARTYNAME",partynameselected)
        totalwork=DBMSGetData.getAllDataByTwoColumn("RECEIVEDWORK","PANNUMBER","DEPARTMENT",panlist[0],departmentselected)
        AdminButtonGlobal.CURRENTTABLEFRAME=tkinter.Frame(contentframe)
        AdminButtonGlobal.CURRENTTABLEFRAME.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(AdminButtonGlobal.CURRENTTABLEFRAME,totalwork)        
    
    return



def workList(root):

    global contentframe

    contentframe=tkinter.Frame(root)
    contentframe.grid(row=0,column=1,ipadx=globalvalues.HEIGHT,ipady=globalvalues.WIDTH-100)


    tkinter.Label(contentframe,text="Work List-",font="Time 14").grid(row=0,column=0,sticky=W,pady=7)


    global groupnamemenu
    
    groupnameselected=tkinter.StringVar(contentframe)
    groupnamelist=["All"]
    try:
        for i in DBMSGetData.getData("GROUPANDPARTYDETAILS","GROUPNAME"):
            groupnamelist.append(i[0])
    except:
        pass 
    

    

    tkinter.Label(contentframe,text="Group Name:").grid(row=1,column=0,sticky=W,pady=5)
    groupnamemenu=ttk.Combobox(contentframe,textvariable= groupnameselected)
    groupnamemenu.grid(row=1,column=1,sticky=W,padx=8,pady=3)
    groupnamemenu['value']=groupnamelist

    groupnamemenu.current(0)
    
    groupnamemenu.bind("<<ComboboxSelected>>",lambda event=1:getPartyNameMenu(groupnameselected.get(),departmentselected.get()))


    global partynamemenu

    tkinter.Label(contentframe,text="Party Name:").grid(row=2,column=0,sticky=W,pady=5)
    partynameselected=tkinter.StringVar(contentframe)
    partynamelist = ["All"]
    partynamemenu=ttk.Combobox(contentframe,textvariable=partynameselected)
    partynamemenu.grid(row=2,column=1,sticky=W,padx=8,pady=3)
    partynamemenu['value']=partynamelist
    partynamemenu.current(0)
    

    partynamemenu.bind("<<ComboboxSelected>>",lambda event=1: getGroupData(departmentselected.get(),partynameselected.get(),groupnameselected.get()))

    

    departmentselected=tkinter.StringVar(contentframe)
    departmentlist = ["All","Income Tax","Accounting","GST","Audit","Project","TDS","TCS","Other"]
    departmentselected.set("All")
    tkinter.Label(contentframe,text="Department:").grid(row=3,column=0,sticky=W)
    tkinter.OptionMenu(contentframe,departmentselected,*departmentlist,command=lambda event=1:getDepartmentTable(contentframe,departmentselected.get(),groupnameselected.get(),partynameselected.get())).grid(row=3,column=1,sticky=W,pady=3,padx=8)


    AdminButtonGlobal.CURRENTTABLEFRAME=tkinter.Frame(contentframe)
    AdminButtonGlobal.CURRENTTABLEFRAME.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
    StaticTable.drawTable(AdminButtonGlobal.CURRENTTABLEFRAME,DBMSGetData.getAllData("RECEIVEDWORK"))



    AdminButtonGlobal.CURRENTFRAME=contentframe    

    
    return