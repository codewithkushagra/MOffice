import tkinter
from tkinter.constants import *
from tkinter import messagebox
from tkinter import ttk

import globalvalues
import DBMSGetData
import DBMSSaveData
import AdminButtonGlobal
import FrameSwitcher

partynamemenu=ttk.Combobox
groupnamemenu=ttk.Combobox



def getPANAdress(partynameselected,groupnameselected,panlabel,addresslabel):
    datapanaddress=DBMSGetData.getOneVTwoP("GROUPANDPARTYDETAILS","PARTYADDRESS","PANNUMBER","PARTYNAME","GROUPNAME",partynameselected,groupnameselected)
    
    panlabel["text"]=datapanaddress[1]
    addresslabel["text"]=datapanaddress[0]    
    return



def getPartyNameMenu(groupnameselected,panlabel,addresslabel):
    
    global partynamemenu
    partynamelist = []
    
    
    for i in DBMSGetData.getWhereData("GROUPANDPARTYDETAILS","PARTYNAME","GROUPNAME",groupnameselected):
        partynamelist.append(i[0])
    
    if not partynamelist:
        partynamelist.append("None")

    partynamemenu['value']=partynamelist
    partynamemenu.set("None")

    panlabel["text"]="-"
    addresslabel["text"]="-"
    
    
    return



def saveWorkEntry(contentframe,root,departmenttype,departmenttypec,pannumber,departmentnameselected,recievedate,financialyear,assessmentyear):
    try:
        workstatus="Pending"
        DBMSSaveData.insertWorkRecord(departmenttype,departmenttypec,pannumber,departmentnameselected,recievedate,financialyear,assessmentyear,workstatus)
        FrameSwitcher.recreateWorkEntrySection(contentframe,root)
        messagebox.showinfo("Saved", "New work record have been added")
        
    except:
        messagebox.showerror("Error","Connection Error")
    return




def getDepartmentTypeCList(contentframe,departmenttype,departmenttypeclabel,departmentnameselected,departmenttypec):
    
    try:
        AdminButtonGlobal.DEPARTMENTTYPECNAMEMENU.destroy()
    except:
        pass
    

    try:
        AdminButtonGlobal.DEPARTMENTTYPECNAMEENTRY.destroy()
    except:
        pass

    entryboxlist=["Return","Scruitny","Notice","Tax Audit","Other Statutary Audit","Other Report"]
    
    departmenttypeclabel["text"]=departmenttype+":"

    if departmenttype in entryboxlist and (departmentnameselected !="TDS" or departmenttype=="Notice"):
        departmenttypec.set("")
        AdminButtonGlobal.DEPARTMENTTYPECNAMEENTRY=tkinter.Entry(contentframe, bd=1 ,width=10,textvariable=departmenttypec)
        AdminButtonGlobal.DEPARTMENTTYPECNAMEENTRY.grid(row=7,column=1,sticky=W,padx=8,pady=3)

    elif departmenttype=="Appeal":
        
        departmenttypeclist=["First Appeal","Second Appeal"]
        AdminButtonGlobal.DEPARTMENTTYPECNAMEMENU=tkinter.OptionMenu(contentframe,departmenttypec,*departmenttypeclist)
        AdminButtonGlobal.DEPARTMENTTYPECNAMEMENU.grid(row=7,column=1,sticky=W,padx=8,pady=3)
    
    elif departmentnameselected=="TDS" and departmenttype=="Return":
        
        departmenttypeclist=["24-Q Quater1","24-Q Quater2","24-Q Quater3","24-Q Quater4","26-Q Quater1","26-Q Quater2","26-Q Quater3","26-Q Quater4","revised","other"]
        AdminButtonGlobal.DEPARTMENTTYPECNAMEMENU=tkinter.OptionMenu(contentframe,departmenttypec,*departmenttypeclist)
        AdminButtonGlobal.DEPARTMENTTYPECNAMEMENU.grid(row=7,column=1,sticky=W,padx=8,pady=3)
    
    elif departmenttype=="New Project":

        departmenttypeclist=["T.L. & C.C.","T.L.","C.C.","Other"]
        AdminButtonGlobal.DEPARTMENTTYPECNAMEMENU=tkinter.OptionMenu(contentframe,departmenttypec,*departmenttypeclist)
        AdminButtonGlobal.DEPARTMENTTYPECNAMEMENU.grid(row=7,column=1,sticky=W,padx=8,pady=3)

    elif departmenttype=="Renewal":
        
        departmenttypeclist=["Projection","CMA"]
        AdminButtonGlobal.DEPARTMENTTYPECNAMEMENU=tkinter.OptionMenu(contentframe,departmenttypec,*departmenttypeclist)
        AdminButtonGlobal.DEPARTMENTTYPECNAMEMENU.grid(row=7,column=1,sticky=W,padx=8,pady=3)


    return



def getDepartmentTypeList(contentframe,departmenttype,departmentnameselected,departmenttypelabel,departmenttypeclabel,departmenttypec):
    
    AdminButtonGlobal.DEPARTMENTTYPENAMEMENU.destroy()
    departmenttypeclabel["text"]="-"
    try:
        AdminButtonGlobal.DEPARTMENTTYPECNAMEMENU.destroy()
    except:
        pass
    
    try:
        AdminButtonGlobal.DEPARTMENTTYPECNAMEENTRY.destroy()
    except:
        pass


    departmenttype.set("None")
    departmenttypelabel["text"]=departmentnameselected+":"

    if departmentnameselected=="Income Tax":

        departmenttypelist=["Return","Scruitny","Notice","Appeal","Other"]
        AdminButtonGlobal.DEPARTMENTTYPENAMEMENU=tkinter.OptionMenu(contentframe,departmenttype,*departmenttypelist,command=lambda event=0:getDepartmentTypeCList(contentframe,departmenttype.get(),departmenttypeclabel,departmentnameselected,departmenttypec))
        AdminButtonGlobal.DEPARTMENTTYPENAMEMENU.grid(row=6,column=1,sticky=W,padx=8,pady=3)
        
    elif departmentnameselected=="GST":

        departmenttypelist=["Return","Notice","Other"]
        AdminButtonGlobal.DEPARTMENTTYPENAMEMENU=tkinter.OptionMenu(contentframe,departmenttype,*departmenttypelist,command=lambda event=0:getDepartmentTypeCList(contentframe,departmenttype.get(),departmenttypeclabel,departmentnameselected,departmenttypec))
        AdminButtonGlobal.DEPARTMENTTYPENAMEMENU.grid(row=6,column=1,sticky=W,padx=8,pady=3)

    elif departmentnameselected=="Accounting":

        departmenttypelist=["-"]
        AdminButtonGlobal.DEPARTMENTTYPENAMEMENU=tkinter.OptionMenu(contentframe,departmenttype,*departmenttypelist,command=lambda event=0:getDepartmentTypeCList(contentframe,departmenttype.get(),departmenttypeclabel,departmentnameselected,departmenttypec))
        AdminButtonGlobal.DEPARTMENTTYPENAMEMENU.grid(row=6,column=1,sticky=W,padx=8,pady=3)
    
    elif departmentnameselected=="Audit":

        departmenttypelist=["Tax Aduit","Company Audit","GST Audit","General Audit","Other Statutary Audit","Other Report"]
        AdminButtonGlobal.DEPARTMENTTYPENAMEMENU=tkinter.OptionMenu(contentframe,departmenttype,*departmenttypelist,command=lambda event=0:getDepartmentTypeCList(contentframe,departmenttype.get(),departmenttypeclabel,departmentnameselected,departmenttypec))
        AdminButtonGlobal.DEPARTMENTTYPENAMEMENU.grid(row=6,column=1,sticky=W,padx=8,pady=3)
    
    elif departmentnameselected=="Project":

        departmenttypelist=["New Project","Renewal"]
        AdminButtonGlobal.DEPARTMENTTYPENAMEMENU=tkinter.OptionMenu(contentframe,departmenttype,*departmenttypelist,command=lambda event=0:getDepartmentTypeCList(contentframe,departmenttype.get(),departmenttypeclabel,departmentnameselected,departmenttypec))
        AdminButtonGlobal.DEPARTMENTTYPENAMEMENU.grid(row=6,column=1,sticky=W,padx=8,pady=3)

    elif departmentnameselected=="Other":

        departmenttypelist=["-"]
        AdminButtonGlobal.DEPARTMENTTYPENAMEMENU=tkinter.OptionMenu(contentframe,departmenttype,*departmenttypelist,command=lambda event=0:getDepartmentTypeCList(contentframe,departmenttype.get(),departmenttypeclabel,departmentnameselected,departmenttypec))
        AdminButtonGlobal.DEPARTMENTTYPENAMEMENU.grid(row=6,column=1,sticky=W,padx=8,pady=3)

    elif departmentnameselected=="TDS":

        departmenttypelist=["Return","Notice"]
        AdminButtonGlobal.DEPARTMENTTYPENAMEMENU=tkinter.OptionMenu(contentframe,departmenttype,*departmenttypelist,command=lambda event=0:getDepartmentTypeCList(contentframe,departmenttype.get(),departmenttypeclabel,departmentnameselected,departmenttypec))
        AdminButtonGlobal.DEPARTMENTTYPENAMEMENU.grid(row=6,column=1,sticky=W,padx=8,pady=3)

    elif departmentnameselected=="TCS":

        departmenttypelist=["Return","Notice"]
        AdminButtonGlobal.DEPARTMENTTYPENAMEMENU=tkinter.OptionMenu(contentframe,departmenttype,*departmenttypelist,command=lambda event=0:getDepartmentTypeCList(contentframe,departmenttype.get(),departmenttypeclabel,departmentnameselected,departmenttypec))
        AdminButtonGlobal.DEPARTMENTTYPENAMEMENU.grid(row=6,column=1,sticky=W,padx=8,pady=3)
    
    
    return







def enterWorkIn(root):

    contentframe=tkinter.Frame(root)
    contentframe.grid(row=0,column=1,ipadx=globalvalues.HEIGHT,ipady=globalvalues.WIDTH-100)

    
    tkinter.Label(contentframe,text="ADD WORK-",font="Time 14").grid(row=0,column=0,sticky=W,pady=7)


    global groupnamemenu
    
    groupnameselected=tkinter.StringVar(contentframe)
    groupnamelist=[]
    try:
        for i in DBMSGetData.getData("GROUPANDPARTYDETAILS","GROUPNAME"):
            groupnamelist.append(i[0])
    except:
        pass 
    
    
    

    tkinter.Label(contentframe,text="Group Name:").grid(row=1,column=0,sticky=W,pady=5)
    groupnamemenu=ttk.Combobox(contentframe,textvariable= groupnameselected)
    groupnamemenu.grid(row=1,column=1,sticky=W,padx=8,pady=3)
    groupnamemenu['value']=groupnamelist

    groupnamemenu.set("None")
    
    groupnamemenu.bind("<<ComboboxSelected>>",lambda event=1:getPartyNameMenu(groupnameselected.get(),panlabel,addresslabel))


    global partynamemenu

    tkinter.Label(contentframe,text="Party Name:").grid(row=2,column=0,sticky=W,pady=5)
    partynameselected=tkinter.StringVar(contentframe)
    partynamelist = ["All"]
    partynamemenu=ttk.Combobox(contentframe,textvariable=partynameselected)
    partynamemenu.grid(row=2,column=1,sticky=W,padx=8,pady=3)
    partynamemenu['value']=partynamelist
    partynamemenu.set("None")
    

    partynamemenu.bind("<<ComboboxSelected>>",lambda event=1: getPANAdress(partynameselected.get(),groupnameselected.get(),panlabel,addresslabel))
    
    
    tkinter.Label(contentframe,text="PAN No:").grid(row=3,column=0,sticky=W,pady=5)
    panlabel=tkinter.Label(contentframe,text="-")
    panlabel.grid(row=3,column=1,sticky=W,padx=8,pady=5)
    

    tkinter.Label(contentframe,text="Address:").grid(row=4,column=0,sticky=W,pady=5)
    addresslabel=tkinter.Label(contentframe,text="-")
    addresslabel.grid(row=4,column=1,sticky=W,padx=8,pady=5)

    #-----------------------------------department ----------------------------------------------------------------
    
    departmentnameselected=tkinter.StringVar(contentframe)
    departmentnamelist = ["Income Tax","Accounting","GST","Audit","Project","TDS","TCS","Other"]
    departmentnameselected.set("None")
    tkinter.Label(contentframe,text="Department:").grid(row=5,column=0,sticky=W,pady=5)
    AdminButtonGlobal.DEPARTMENTNAMEMENU=tkinter.OptionMenu(contentframe,departmentnameselected,*departmentnamelist,command=lambda event=0:getDepartmentTypeList(contentframe,departmenttype,departmentnameselected.get(),departmenttypelabel,departmenttypeclabel,departmenttypec))
    AdminButtonGlobal.DEPARTMENTNAMEMENU.grid(row=5,column=1,sticky=W,padx=8,pady=3)


    departmenttypelabel= tkinter.Label(contentframe,text="-")
    departmenttypelabel.grid(row=6,column=0,sticky=W,pady=5)
    departmenttype=tkinter.StringVar(contentframe)
    departmenttypelist = ["-"]
    departmenttype.set("None")
    AdminButtonGlobal.DEPARTMENTTYPENAMEMENU=tkinter.OptionMenu(contentframe,departmenttype,*departmenttypelist)
    AdminButtonGlobal.DEPARTMENTTYPENAMEMENU.grid(row=6,column=1,sticky=W,padx=8,pady=3)


    departmenttypeclabel = tkinter.Label(contentframe,text="-")
    departmenttypeclabel.grid(row=7,column=0,sticky=W,pady=5)
    departmenttypec=tkinter.StringVar(contentframe)
    departmenttypeclist = ["-"]
    departmenttypec.set("None")
    AdminButtonGlobal.DEPARTMENTTYPECNAMEMENU=tkinter.OptionMenu(contentframe,departmenttypec,*departmenttypeclist)
       

    #-----------------------------------department-end ----------------------------------------------------------------

    recievedate=tkinter.StringVar(contentframe)
    tkinter.Label(contentframe,text="Recieve Date:").grid(row=8,column=0,sticky=W,pady=5)
    tkinter.Entry(contentframe, bd=1 ,width=20,textvariable=recievedate).grid(row=8,column=1,sticky=W,padx=8,pady=3)

    financialyear=tkinter.StringVar(contentframe)
    tkinter.Label(contentframe,text="Financial Year:").grid(row=9,column=0,sticky=W,pady=5)
    tkinter.Entry(contentframe, bd=1 ,width=20,textvariable=financialyear).grid(row=9,column=1,sticky=W,padx=8,pady=3)

    assessmentyear=tkinter.StringVar(contentframe)
    tkinter.Label(contentframe,text="Assessment Year:").grid(row=10,column=0,sticky=W,pady=5)
    tkinter.Entry(contentframe, bd=1 ,width=20,textvariable=assessmentyear).grid(row=10,column=1,sticky=W,padx=8,pady=3)

    tkinter.Button(contentframe,text="Save",command=lambda:saveWorkEntry(contentframe,root,departmenttype.get(),departmenttypec.get(),panlabel["text"],departmentnameselected.get(),recievedate.get(),financialyear.get(),assessmentyear.get())).grid(row=11,columnspan=2,pady=20)

    AdminButtonGlobal.CURRENTFRAME=contentframe

    return