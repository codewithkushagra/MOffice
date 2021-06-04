import tkinter
from tkinter.constants import *
from tkinter import messagebox

def enterWorkIn(root):
    tkinter.Label(root,text="ADD WORK-",bg="white").grid(row=0,column=0,sticky=W,pady=7)
    
    groupnameselected=tkinter.StringVar(root)
    groupnamelist = ["sample1","sample1"]
    groupnameselected.set("None")
    tkinter.Label(root,text="Group Name:",bg="white").grid(row=1,column=0,sticky=W,pady=7)
    tkinter.OptionMenu(root,groupnameselected,*groupnamelist).grid(row=1,column=1,sticky=W,padx=8,pady=5)


    partynameselected=tkinter.StringVar(root)
    partynamelist = ["sample1","sample1"]
    partynameselected.set("None")
    tkinter.Label(root,text="Party Name:",bg="white").grid(row=1,column=2,sticky=W,pady=7)
    tkinter.OptionMenu(root,partynameselected,*partynamelist).grid(row=1,column=3,sticky=W,padx=8,pady=5)
    
    
    tkinter.Label(root,text="PAN No:",bg="white").grid(row=2,column=0,sticky=W,pady=7)
    tkinter.Label(root,text="-",bg="white").grid(row=2,column=1,sticky=W,padx=8,pady=5)
    
    
    tkinter.Label(root,text="Address:",bg="white").grid(row=2,column=2,sticky=W,pady=7)
    tkinter.Label(root,text="-",bg="white").grid(row=2,column=3,sticky=W,padx=8,pady=5)
        

    # tkinter.Button(root,text="Save").grid(row=4,columnspan=2,pady=20)

    return