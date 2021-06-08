import tkinter
from tkinter.constants import *
from tkinter import messagebox
import globalvalues
import DBMSGetData
import DBMSSaveData
import AdminButtons
import FrameSwitcher




def getPANAdress(partynameselected,groupnameselected,panlabel,addresslabel):
    datapanaddress=DBMSGetData.getOneVTwoP("GROUPANDPARTYDETAILS","PARTYADDRESS","PANNUMBER","PARTYNAME","GROUPNAME",partynameselected,groupnameselected)
    
    panlabel["text"]=datapanaddress[1]
    addresslabel["text"]=datapanaddress[0]    
    return



def getPartyNameMenu(partynamemenu,partynameselected,groupnameselected,contentframe,panlabel,addresslabel):
    
    partynamemenu.destroy()    
    partynamelist = []
    
    if not partynamelist:
        partynamelist.append("None")
    
    for i in DBMSGetData.getWhereData("GROUPANDPARTYDETAILS","PARTYNAME","GROUPNAME",groupnameselected):
        partynamelist.append(i[0])
    panlabel["text"]="-"
    addresslabel["text"]="-"
    partynameselected.set("None")
    partynamemenu=tkinter.OptionMenu(contentframe,partynameselected,*partynamelist,command=lambda event=0:getPANAdress(partynameselected.get(),groupnameselected,panlabel,addresslabel))
    partynamemenu.grid(row=2,column=1,sticky=W,padx=8,pady=3)
    
    return



def saveWorkEntry(buttonframe,contentframe,root,departmenttype,departmenttypec,pannumber,departmentnameselected,recievedate,financialyear,assessmentyear):
    try:
        workstatus="Pending"
        DBMSSaveData.insertWorkRecord(departmenttype,departmenttypec,pannumber,departmentnameselected,recievedate,financialyear,assessmentyear,workstatus)
        FrameSwitcher.recreateWorkEntrySection(contentframe,root,buttonframe)
        messagebox.showinfo("Saved", "New work record have been added")
        
    except:
        messagebox.showerror("Error","Connection Error")
    return




def getDepartmentTypeCList(contentframe,departmenttypemenu,departmentnameselected,departmenttype,departmenttypeclabel,departmenttypec,departmenttypecmenu):
    
    departmenttypemenu.destroy()

    tkinter.Label(contentframe,text=departmenttype).grid(row=6,column=1,sticky=W,padx=8,pady=3)

    entryboxlist=["Return","Scruitny","Notice","Tax Audit","Other Statutary Audit","Other Report"]
    
    departmenttypeclabel["text"]=departmenttype+":"

    if departmenttype in entryboxlist and (departmentnameselected !="TDS" or departmenttype=="Notice"):
        departmenttypec.set("")
        departmenttypecmenu=tkinter.Entry(contentframe, bd=1 ,width=10,textvariable=departmenttypec)
        departmenttypecmenu.grid(row=7,column=1,sticky=W,padx=8,pady=3)

    elif departmenttype=="Appeal":
        
        departmenttypeclist=["First Appeal","Second Appeal"]
        departmenttypecmenu=tkinter.OptionMenu(contentframe,departmenttypec,*departmenttypeclist)
        departmenttypecmenu.grid(row=7,column=1,sticky=W,padx=8,pady=3)
    
    elif departmentnameselected=="TDS" and departmenttype=="Return":
        
        departmenttypeclist=["24-Q Quater1","24-Q Quater2","24-Q Quater3","24-Q Quater4","26-Q Quater1","26-Q Quater2","26-Q Quater3","26-Q Quater4","revised","other"]
        departmenttypecmenu=tkinter.OptionMenu(contentframe,departmenttypec,*departmenttypeclist)
        departmenttypecmenu.grid(row=7,column=1,sticky=W,padx=8,pady=3)
    
    elif departmenttype=="New Project":

        departmenttypeclist=["T.L. & C.C.","T.L.","C.C.","Other"]
        departmenttypecmenu=tkinter.OptionMenu(contentframe,departmenttypec,*departmenttypeclist)
        departmenttypecmenu.grid(row=7,column=1,sticky=W,padx=8,pady=3)

    elif departmenttype=="Renewal":
        
        departmenttypeclist=["Projection","CMA"]
        departmenttypecmenu=tkinter.OptionMenu(contentframe,departmenttypec,*departmenttypeclist)
        departmenttypecmenu.grid(row=7,column=1,sticky=W,padx=8,pady=3)


    return



def getDepartmentTypeList(contentframe,departmentnamemenu,departmenttypelabel,departmenttypeclabel,departmentnameselected,departmenttype,departmenttypec,departmenttypemenu,departmenttypecmenu):
    
    departmentnamemenu.destroy()
    departmenttypemenu.destroy()
    departmenttypecmenu.destroy()
    tkinter.Label(contentframe,text=departmentnameselected).grid(row=5,column=1,sticky=W,padx=8,pady=3)

    departmenttype.set("None")
    departmenttypelabel["text"]=departmentnameselected+":"

    if departmentnameselected=="Income Tax":

        departmenttypelist=["Return","Scruitny","Notice","Appeal","Other"]
        departmenttypemenu=tkinter.OptionMenu(contentframe,departmenttype,*departmenttypelist,command=lambda event=0:getDepartmentTypeCList(contentframe,departmenttypemenu,departmentnameselected,departmenttype.get(),departmenttypeclabel,departmenttypec,departmenttypecmenu))
        departmenttypemenu.grid(row=6,column=1,sticky=W,padx=8,pady=3)
        
    elif departmentnameselected=="GST":

        departmenttypelist=["Return","Notice","Other"]
        departmenttypemenu=tkinter.OptionMenu(contentframe,departmenttype,*departmenttypelist,command=lambda event=0:getDepartmentTypeCList(contentframe,departmenttypemenu,departmentnameselected,departmenttype.get(),departmenttypeclabel,departmenttypec,departmenttypecmenu))
        departmenttypemenu.grid(row=6,column=1,sticky=W,padx=8,pady=3)

    elif departmentnameselected=="Accounting":

        departmenttypelist=["-"]
        departmenttypemenu=tkinter.OptionMenu(contentframe,departmenttype,*departmenttypelist,command=lambda event=0:getDepartmentTypeCList(contentframe,departmenttypemenu,departmentnameselected,departmenttype.get(),departmenttypeclabel,departmenttypec,departmenttypecmenu))
        departmenttypemenu.grid(row=6,column=1,sticky=W,padx=8,pady=3)
    
    elif departmentnameselected=="Audit":

        departmenttypelist=["Tax Aduit","Company Audit","GST Audit","General Audit","Other Statutary Audit","Other Report"]
        departmenttypemenu=tkinter.OptionMenu(contentframe,departmenttype,*departmenttypelist,command=lambda event=0:getDepartmentTypeCList(contentframe,departmenttypemenu,departmentnameselected,departmenttype.get(),departmenttypeclabel,departmenttypec,departmenttypecmenu))
        departmenttypemenu.grid(row=6,column=1,sticky=W,padx=8,pady=3)
    
    elif departmentnameselected=="Project":

        departmenttypelist=["New Project","Renewal"]
        departmenttypemenu=tkinter.OptionMenu(contentframe,departmenttype,*departmenttypelist,command=lambda event=0:getDepartmentTypeCList(contentframe,departmenttypemenu,departmentnameselected,departmenttype.get(),departmenttypeclabel,departmenttypec,departmenttypecmenu))
        departmenttypemenu.grid(row=6,column=1,sticky=W,padx=8,pady=3)

    elif departmentnameselected=="Other":

        departmenttypelist=["-"]
        departmenttypemenu=tkinter.OptionMenu(contentframe,departmenttype,*departmenttypelist,command=lambda event=0:getDepartmentTypeCList(contentframe,departmenttypemenu,departmentnameselected,departmenttype.get(),departmenttypeclabel,departmenttypec,departmenttypecmenu))
        departmenttypemenu.grid(row=6,column=1,sticky=W,padx=8,pady=3)

    elif departmentnameselected=="TDS":

        departmenttypelist=["Return","Notice"]
        departmenttypemenu=tkinter.OptionMenu(contentframe,departmenttype,*departmenttypelist,command=lambda event=0:getDepartmentTypeCList(contentframe,departmenttypemenu,departmentnameselected,departmenttype.get(),departmenttypeclabel,departmenttypec,departmenttypecmenu))
        departmenttypemenu.grid(row=6,column=1,sticky=W,padx=8,pady=3)

    elif departmentnameselected=="TCS":

        departmenttypelist=["Return","Notice"]
        departmenttypemenu=tkinter.OptionMenu(contentframe,departmenttype,*departmenttypelist,command=lambda event=0:getDepartmentTypeCList(contentframe,departmenttypemenu,departmentnameselected,departmenttype.get(),departmenttypeclabel,departmenttypec,departmenttypecmenu))
        departmenttypemenu.grid(row=6,column=1,sticky=W,padx=8,pady=3)
    
    
    return







def enterWorkIn(root):

    contentframe=tkinter.Frame(root)
    contentframe.grid(row=0,column=1,ipadx=globalvalues.HEIGHT,ipady=globalvalues.WIDTH-100)

    
    tkinter.Label(contentframe,text="ADD WORK-",font="Time 14").grid(row=0,column=0,sticky=W,pady=7)


    tkinter.Label(contentframe,text="Party Name:").grid(row=2,column=0,sticky=W,pady=5)
    partynameselected=tkinter.StringVar(contentframe)
    partynamelist = ["-"]
    partynameselected.set("None")
    partynamemenu=tkinter.OptionMenu(contentframe,partynameselected,*partynamelist)
    partynamemenu.grid(row=2,column=1,sticky=W,padx=8,pady=3)



    groupnameselected=tkinter.StringVar(contentframe)
    groupnamelist=[]
    try:
        for i in DBMSGetData.getData("GROUPANDPARTYDETAILS","GROUPNAME"):
            groupnamelist.append(i[0])
       
    except:
        pass 
    groupnameselected.set("None")
    if not groupnamelist:
        groupnamelist.append("None")
    tkinter.Label(contentframe,text="Group Name:").grid(row=1,column=0,sticky=W,pady=5)
    tkinter.OptionMenu(contentframe,groupnameselected,*groupnamelist,command=lambda event=0: getPartyNameMenu(partynamemenu,partynameselected,groupnameselected.get(),contentframe,panlabel,addresslabel)).grid(row=1,column=1,sticky=W,padx=8,pady=3)

    
    
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
    departmentnamemenu=tkinter.OptionMenu(contentframe,departmentnameselected,*departmentnamelist,command=lambda event=0:getDepartmentTypeList(contentframe,departmentnamemenu,departmenttypelabel,departmenttypeclabel,departmentnameselected.get(),departmenttype,departmenttypec,departmenttypemenu,departmenttypecmenu))
    departmentnamemenu.grid(row=5,column=1,sticky=W,padx=8,pady=3)


    departmenttypelabel= tkinter.Label(contentframe,text="-")
    departmenttypelabel.grid(row=6,column=0,sticky=W,pady=5)
    departmenttype=tkinter.StringVar(contentframe)
    departmenttypelist = ["-"]
    departmenttype.set("None")
    departmenttypemenu=tkinter.OptionMenu(contentframe,departmenttype,*departmenttypelist)
    departmenttypemenu.grid(row=6,column=1,sticky=W,padx=8,pady=3)


    departmenttypeclabel = tkinter.Label(contentframe,text="-")
    departmenttypeclabel.grid(row=7,column=0,sticky=W,pady=5)
    departmenttypec=tkinter.StringVar(contentframe)
    departmenttypeclist = ["-"]
    departmenttypec.set("None")
    departmenttypecmenu=tkinter.OptionMenu(contentframe,departmenttypec,*departmenttypeclist)
    

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

    tkinter.Button(contentframe,text="Save",command=lambda:saveWorkEntry(buttonframe,contentframe,root,departmenttype.get(),departmenttypec.get(),panlabel["text"],departmentnameselected.get(),recievedate.get(),financialyear.get(),assessmentyear.get())).grid(row=11,columnspan=2,pady=20)

    buttonframe=tkinter.Frame(root)
    tkinter.Frame(buttonframe,relief=RIDGE,borderwidth=2,bg="red").grid(row=0,column=0,rowspan=40,ipady=globalvalues.HEIGHT,ipadx=100)
    buttonframe.grid(row=0,column=0,rowspan=40,sticky=N)

    AdminButtons.buttonCreate(buttonframe,contentframe,root)

    return