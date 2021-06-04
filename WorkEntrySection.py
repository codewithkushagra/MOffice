import tkinter
from tkinter.constants import *
from tkinter import messagebox

def enterWorkIn(root):
    tkinter.Label(root,text="ADD WORK-",bg="white").grid(row=0,column=0,sticky=W,pady=7)
    
    groupnameselected=tkinter.StringVar(root)
    groupnamelist = ["sample1","sample1"]
    groupnameselected.set("None")
    tkinter.Label(root,text="Group Name:",bg="white").grid(row=1,column=0,sticky=W,pady=5)
    tkinter.OptionMenu(root,groupnameselected,*groupnamelist).grid(row=1,column=1,sticky=W,padx=8,pady=3)


    partynameselected=tkinter.StringVar(root)
    partynamelist = ["sample1","sample1"]
    partynameselected.set("None")
    tkinter.Label(root,text="Party Name:",bg="white").grid(row=2,column=0,sticky=W,pady=5)
    tkinter.OptionMenu(root,partynameselected,*partynamelist).grid(row=2,column=1,sticky=W,padx=8,pady=3)
    
    
    tkinter.Label(root,text="PAN No:",bg="white").grid(row=3,column=0,sticky=W,pady=5)
    tkinter.Label(root,text="-",bg="white").grid(row=3,column=1,sticky=W,padx=8,pady=5)
    
    
    tkinter.Label(root,text="Address:",bg="white").grid(row=4,column=0,sticky=W,pady=5)
    tkinter.Label(root,text="-",bg="white").grid(row=4,column=1,sticky=W,padx=8,pady=5)
    
    departmentnameselected=tkinter.StringVar(root)
    departmentnamelist = ["sample1","sample1"]
    departmentnameselected.set("None")
    tkinter.Label(root,text="Department:",bg="white").grid(row=5,column=0,sticky=W,pady=5)
    tkinter.OptionMenu(root,departmentnameselected,*departmentnamelist).grid(row=5,column=1,sticky=W,padx=8,pady=3)

    tkinter.Label(root,text="Recieve Date:",bg="white").grid(row=6,column=0,sticky=W,pady=5)
    tkinter.Entry(root, bd=1 ,width=20).grid(row=6,column=1,sticky=W,padx=8,pady=3)

    tkinter.Label(root,text="Financial Year:",bg="white").grid(row=7,column=0,sticky=W,pady=5)
    tkinter.Entry(root, bd=1 ,width=20).grid(row=7,column=1,sticky=W,padx=8,pady=3)

    tkinter.Label(root,text="Assessment Year:",bg="white").grid(row=8,column=0,sticky=W,pady=5)
    tkinter.Entry(root, bd=1 ,width=20).grid(row=8,column=1,sticky=W,padx=8,pady=3)

    tkinter.Button(root,text="Save").grid(row=9,columnspan=2,pady=20)

    return