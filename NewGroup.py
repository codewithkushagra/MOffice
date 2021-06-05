import tkinter
from tkinter.constants import *
from tkinter import messagebox

import AdminButtons
import DBMSSaveData



def saveNewGroup(groupname,partyname,pannumber,address,groupnamevar,partynamevar,pannumbervar,addressvar):
    if groupname=="" or partyname=="" or pannumber=="" or address=="":
        messagebox.showerror("Error","Invalid Entry")
    else:
        DBMSSaveData.saveGroupParty(groupname,partyname,pannumber,address)
        groupnamevar.set("")
        partynamevar.set("")
        pannumbervar.set("")
        addressvar.set("")
        messagebox.showinfo("Saved","New Group added")
    return


def newGroup(root):
    
    contentframe=tkinter.Frame(root)
    contentframe.grid(row=0,column=1)


    groupname=tkinter.StringVar(root)
    partyname=tkinter.StringVar(root)
    pannumber=tkinter.StringVar(root)
    address=tkinter.StringVar(root)

    tkinter.Label(contentframe,text="ADD NEW GROUP-").grid(row=0,column=0,sticky=W,pady=7)

    tkinter.Label(contentframe,text="Group Name:").grid(row=1,column=0,sticky=W,pady=7)
    tkinter.Entry(contentframe, bd=1 ,width=20,textvariable=groupname).grid(row=1,column=1,sticky=W,padx=8,pady=5)

    tkinter.Label(contentframe,text="Party Name:").grid(row=2,column=0,sticky=W,pady=7)
    tkinter.Entry(contentframe, bd=1 ,width=20,textvariable=partyname).grid(row=2,column=1,sticky=W,padx=8,pady=5)
    
    tkinter.Label(contentframe,text="PAN No:").grid(row=3,column=0,sticky=W,pady=7)
    tkinter.Entry(contentframe, bd=1 ,width=20,textvariable=pannumber).grid(row=3,column=1,sticky=W,padx=8,pady=5)
    
    tkinter.Label(contentframe,text="Address:").grid(row=4,column=0,sticky=W,pady=7)
    tkinter.Entry(contentframe, bd=1 ,width=20,textvariable=address).grid(row=4,column=1,sticky=W,padx=8,pady=5)
    
    tkinter.Button(contentframe,text="Save",command=lambda:saveNewGroup(groupname.get(),partyname.get(),pannumber.get(),address.get(),groupname,partyname,pannumber,address ) ).grid(row=5,columnspan=2,pady=20)

    buttonframe=tkinter.Frame(root)
    tkinter.Frame(buttonframe,relief=RIDGE,borderwidth=2).grid(row=0,column=0,rowspan=8,ipady=300,ipadx=100)

    buttonframe.grid(row=0,column=0,rowspan=7,sticky=N)


    AdminButtons.buttonCreate(buttonframe,contentframe,root)

    return