import tkinter
from tkinter.constants import *
import AdminButtons
from tkinter import messagebox

def enterWorkIn(root):

    contentframe=tkinter.Frame(root)
    contentframe.grid(row=0,column=1)
    
    tkinter.Label(contentframe,text="ADD WORK-").grid(row=0,column=0,sticky=W,pady=7)
    
    groupnameselected=tkinter.StringVar(contentframe)
    groupnamelist = ["sample1","sample1"]
    groupnameselected.set("None")
    tkinter.Label(contentframe,text="Group Name:").grid(row=1,column=0,sticky=W,pady=5)
    tkinter.OptionMenu(contentframe,groupnameselected,*groupnamelist).grid(row=1,column=1,sticky=W,padx=8,pady=3)


    partynameselected=tkinter.StringVar(contentframe)
    partynamelist = ["sample1","sample1"]
    partynameselected.set("None")
    tkinter.Label(contentframe,text="Party Name:").grid(row=2,column=0,sticky=W,pady=5)
    tkinter.OptionMenu(contentframe,partynameselected,*partynamelist).grid(row=2,column=1,sticky=W,padx=8,pady=3)
    
    
    tkinter.Label(contentframe,text="PAN No:").grid(row=3,column=0,sticky=W,pady=5)
    tkinter.Label(contentframe,text="-").grid(row=3,column=1,sticky=W,padx=8,pady=5)
    
    
    tkinter.Label(contentframe,text="Address:").grid(row=4,column=0,sticky=W,pady=5)
    tkinter.Label(contentframe,text="-").grid(row=4,column=1,sticky=W,padx=8,pady=5)
    
    departmentnameselected=tkinter.StringVar(contentframe)
    departmentnamelist = ["sample1","sample1"]
    departmentnameselected.set("None")
    tkinter.Label(contentframe,text="Department:").grid(row=5,column=0,sticky=W,pady=5)
    tkinter.OptionMenu(contentframe,departmentnameselected,*departmentnamelist).grid(row=5,column=1,sticky=W,padx=8,pady=3)

    tkinter.Label(contentframe,text="Recieve Date:").grid(row=6,column=0,sticky=W,pady=5)
    tkinter.Entry(contentframe, bd=1 ,width=20).grid(row=6,column=1,sticky=W,padx=8,pady=3)

    tkinter.Label(contentframe,text="Financial Year:").grid(row=7,column=0,sticky=W,pady=5)
    tkinter.Entry(contentframe, bd=1 ,width=20).grid(row=7,column=1,sticky=W,padx=8,pady=3)

    tkinter.Label(contentframe,text="Assessment Year:").grid(row=8,column=0,sticky=W,pady=5)
    tkinter.Entry(contentframe, bd=1 ,width=20).grid(row=8,column=1,sticky=W,padx=8,pady=3)

    tkinter.Button(contentframe,text="Save").grid(row=9,columnspan=2,pady=20)

    buttonframe=tkinter.Frame(root)
    tkinter.Frame(buttonframe,relief=RIDGE,borderwidth=2).grid(row=0,column=0,rowspan=8,ipady=300,ipadx=100)
    buttonframe.grid(row=0,column=0,rowspan=7,sticky=N)

    AdminButtons.buttonCreate(buttonframe,contentframe,root)

    return