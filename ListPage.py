import tkinter
from tkinter.constants import *
from tkinter import messagebox
import StaticTable
import FrameSwitcher
import AdminButtons
import DBMSGetData
import globalvalues
import AdminButtonGlobal



def getGroupData(departmentselected,tableframe,partynameselected,groupnameselected,contentframe):
    tableframe.destroy()
    
    if partynameselected!="All" and departmentselected=="All":

        panlist=DBMSGetData.getOneForOne("GROUPANDPARTYDETAILS","PANNUMBER","PARTYNAME",partynameselected)
        totalwork=DBMSGetData.getAllDataOfColumn("RECEIVEDWORK","PANNUMBER",panlist[0])
        tableframe=tkinter.Frame(contentframe)
        tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(tableframe,totalwork)

    elif partynameselected=="All" and departmentselected!="All":
        
        panlist=DBMSGetData.getWhereData("GROUPANDPARTYDETAILS","PANNUMBER","GROUPNAME",groupnameselected)
        totalwork=[]
        for i in panlist:
            totalwork+=DBMSGetData.getAllDataByTwoColumn("RECEIVEDWORK","PANNUMBER","DEPARTMENT",i[0],departmentselected)

        tableframe=tkinter.Frame(contentframe)
        tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(tableframe,totalwork)

    elif partynameselected!="All" and departmentselected!="All":

        panlist=DBMSGetData.getOneForOne("GROUPANDPARTYDETAILS","PANNUMBER","PARTYNAME",partynameselected)
        totalwork=DBMSGetData.getAllDataByTwoColumn("RECEIVEDWORK","PANNUMBER","DEPARTMENT",panlist[0],departmentselected)
        tableframe=tkinter.Frame(contentframe)
        tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(tableframe,totalwork)
        

    else:
        panlist=DBMSGetData.getWhereData("GROUPANDPARTYDETAILS","PANNUMBER","GROUPNAME",groupnameselected)
        totalwork=[]
        for i in panlist:
            totalwork+=DBMSGetData.getAllDataOfColumn("RECEIVEDWORK","PANNUMBER",i[0])
        
        tableframe=tkinter.Frame(contentframe)
        tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(tableframe,totalwork)
    
    return



def getPartyNameMenu(departmentselected,tableframe,partynamemenu,partynameselected,groupnameselected,contentframe):
    
    partynamemenu.destroy()
    tableframe.destroy()
    partynameselected.set("All")
    partynamelist = ["All"]
    
    if groupnameselected=="All" and departmentselected=="All":
        partynameselected.set("All")
        partynamemenu=tkinter.OptionMenu(contentframe,partynameselected,*partynamelist,command=lambda event=1:getGroupData(departmentselected,tableframe,partynameselected.get(),groupnameselected,contentframe))
        partynamemenu.grid(row=2,column=1,sticky=W,padx=8,pady=3)
        tableframe=tkinter.Frame(contentframe)
        tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(tableframe,DBMSGetData.getAllData("RECEIVEDWORK"))
        
    elif groupnameselected=="All" and departmentselected!="All":

        partynameselected.set("All")
        partynamemenu=tkinter.OptionMenu(contentframe,partynameselected,*partynamelist,command=lambda event=1:getGroupData(departmentselected,tableframe,partynameselected.get(),groupnameselected,contentframe))
        partynamemenu.grid(row=2,column=1,sticky=W,padx=8,pady=3)
        tableframe=tkinter.Frame(contentframe)
        tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(tableframe,DBMSGetData.getAllDataOfColumn("RECEIVEDWORK","DEPARTMENT",departmentselected))
    
    elif groupnameselected!="All" and departmentselected!="All":
        for i in DBMSGetData.getWhereData("GROUPANDPARTYDETAILS","PARTYNAME","GROUPNAME",groupnameselected):
            partynamelist.append(i[0])
        partynameselected.set("All")
        partynamemenu=tkinter.OptionMenu(contentframe,partynameselected,*partynamelist,command=lambda event=1:getGroupData(departmentselected,tableframe,partynameselected.get(),groupnameselected,contentframe))
        partynamemenu.grid(row=2,column=1,sticky=W,padx=8,pady=3)
        
        
        panlist=DBMSGetData.getWhereData("GROUPANDPARTYDETAILS","PANNUMBER","GROUPNAME",groupnameselected)
        totalwork=[]
        for i in panlist:
            totalwork+=DBMSGetData.getAllDataByTwoColumn("RECEIVEDWORK","PANNUMBER","DEPARTMENT",i[0],departmentselected)

        tableframe=tkinter.Frame(contentframe)
        tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(tableframe,totalwork)  

    else:
        for i in DBMSGetData.getWhereData("GROUPANDPARTYDETAILS","PARTYNAME","GROUPNAME",groupnameselected):
            partynamelist.append(i[0])
        partynameselected.set("All")
        partynamemenu=tkinter.OptionMenu(contentframe,partynameselected,*partynamelist,command=lambda event=1:getGroupData(departmentselected,tableframe,partynameselected.get(),groupnameselected,contentframe))
        partynamemenu.grid(row=2,column=1,sticky=W,padx=8,pady=3)
        
        
        panlist=DBMSGetData.getWhereData("GROUPANDPARTYDETAILS","PANNUMBER","GROUPNAME",groupnameselected)
        totalwork=[]
        for i in panlist:
            totalwork+=DBMSGetData.getAllDataOfColumn("RECEIVEDWORK","PANNUMBER",i[0])
        
        tableframe=tkinter.Frame(contentframe)
        tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(tableframe,totalwork)
        
    
    
    return


def getDepartmentTable(contentframe,tableframe,departmentselected,groupnameselected,partynameselected):
    
    tableframe.destroy()
    
    if groupnameselected=="All" and departmentselected!="All":
        print(departmentselected)
        tableframe=tkinter.Frame(contentframe)
        tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(tableframe,DBMSGetData.getAllDataOfColumn("RECEIVEDWORK","DEPARTMENT",departmentselected))
    elif departmentselected=="All" and groupnameselected=="All":
        tableframe=tkinter.Frame(contentframe)
        tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(tableframe,DBMSGetData.getAllData("RECEIVEDWORK"))
    elif groupnameselected!="All" and departmentselected=="All" and partynameselected=="All":
        panlist=DBMSGetData.getWhereData("GROUPANDPARTYDETAILS","PANNUMBER","GROUPNAME",groupnameselected)
        totalwork=[]
        for i in panlist:
            totalwork+=DBMSGetData.getAllDataOfColumn("RECEIVEDWORK","PANNUMBER",i[0])
        
        tableframe=tkinter.Frame(contentframe)
        tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(tableframe,totalwork)

    elif departmentselected!="All" and groupnameselected!="All" and partynameselected=="All":
        panlist=DBMSGetData.getWhereData("GROUPANDPARTYDETAILS","PANNUMBER","GROUPNAME",groupnameselected)
        totalwork=[]
        for i in panlist:
            totalwork+=DBMSGetData.getAllDataByTwoColumn("RECEIVEDWORK","PANNUMBER","DEPARTMENT",i[0],departmentselected)

        tableframe=tkinter.Frame(contentframe)
        tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(tableframe,totalwork)
    elif partynameselected!="All" and departmentselected=="All":
        panlist=DBMSGetData.getOneForOne("GROUPANDPARTYDETAILS","PANNUMBER","PARTYNAME",partynameselected)
        totalwork=DBMSGetData.getAllDataOfColumn("RECEIVEDWORK","PANNUMBER",panlist[0])
        tableframe=tkinter.Frame(contentframe)
        tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(tableframe,totalwork)
    elif partynameselected!="All" and departmentselected!="All":
        panlist=DBMSGetData.getOneForOne("GROUPANDPARTYDETAILS","PANNUMBER","PARTYNAME",partynameselected)
        totalwork=DBMSGetData.getAllDataByTwoColumn("RECEIVEDWORK","PANNUMBER","DEPARTMENT",panlist[0],departmentselected)
        tableframe=tkinter.Frame(contentframe)
        tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
        StaticTable.drawTable(tableframe,totalwork)        
    
    return



def workList(root):


    contentframe=tkinter.Frame(root)
    contentframe.grid(row=0,column=1,ipadx=globalvalues.HEIGHT,ipady=globalvalues.WIDTH-100)


    tkinter.Label(contentframe,text="Work List-",font="Time 14").grid(row=0,column=0,sticky=W,pady=7)

    tkinter.Label(contentframe,text="Party Name:").grid(row=2,column=0,sticky=W,pady=5)
    partynameselected=tkinter.StringVar(contentframe)
    partynamelist = ["-"]
    partynameselected.set("All")
    partynamemenu=tkinter.OptionMenu(contentframe,partynameselected,*partynamelist)
    partynamemenu.grid(row=2,column=1,sticky=W,padx=8,pady=3)

    
    groupnameselected=tkinter.StringVar(contentframe)
    groupnamelist=["All"]
    try:
        for i in DBMSGetData.getData("GROUPANDPARTYDETAILS","GROUPNAME"):
            groupnamelist.append(i[0])
    except:
        pass 
    
    
    
    groupnameselected.set("All")

    tkinter.Label(contentframe,text="Group Name:").grid(row=1,column=0,sticky=W,pady=5)
    tkinter.OptionMenu(contentframe,groupnameselected,*groupnamelist,command=lambda event=0: getPartyNameMenu(departmentselected.get(),tableframe,partynamemenu,partynameselected,groupnameselected.get(),contentframe)).grid(row=1,column=1,sticky=W,padx=8,pady=3)

    departmentselected=tkinter.StringVar(contentframe)
    departmentlist = ["All","Income Tax","Accounting","GST","Audit","Project","TDS","TCS","Other"]
    departmentselected.set("All")
    tkinter.Label(contentframe,text="Department:").grid(row=3,column=0,sticky=W)
    tkinter.OptionMenu(contentframe,departmentselected,*departmentlist,command=lambda event=1:getDepartmentTable(contentframe,tableframe,departmentselected.get(),groupnameselected.get(),partynameselected.get())).grid(row=3,column=1,sticky=W,pady=3,padx=8)


    tableframe=tkinter.Frame(contentframe)
    tableframe.grid(row=4,column=0,sticky=W,ipadx=globalvalues.WIDTH-300,ipady=globalvalues.HEIGHT-200,columnspan=25)
    StaticTable.drawTable(tableframe,DBMSGetData.getAllData("RECEIVEDWORK"))


    AdminButtonGlobal.CURRENTFRAME=contentframe    

    
    return