import tkinter
from tkinter.constants import *
from tkinter import messagebox


def newParty(root):

    tkinter.Label(root,text="ADD NEW PARTY-",bg="white").grid(row=0,column=0,sticky=W,pady=7)

    groupnameselected=tkinter.StringVar(root)
    groupnamelist = ["sample1","sample1"]
    groupnameselected.set("None")
    tkinter.Label(root,text="Group Name:",bg="white").grid(row=1,column=0,sticky=W,pady=7)
    tkinter.OptionMenu(root,groupnameselected,*groupnamelist).grid(row=1,column=1,sticky=W,padx=8,pady=5)

    

    tkinter.Label(root,text="Party Name:",bg="white").grid(row=2,column=0,sticky=W,pady=7)
    tkinter.Entry(root, bd=1 ,width=20).grid(row=2,column=1,sticky=W,padx=8,pady=5)



    tkinter.Label(root,text="PAN No:",bg="white").grid(row=3,column=0,sticky=W,pady=7)
    tkinter.Entry(root, bd=1 ,width=20).grid(row=3,column=1,sticky=W,padx=8,pady=5)



    tkinter.Label(root,text="Address:",bg="white").grid(row=4,column=0,sticky=W,pady=7)
    tkinter.Entry(root, bd=1 ,width=20).grid(row=4,column=1,sticky=W,padx=8,pady=5)



    tkinter.Button(root,text="Save").grid(row=5,columnspan=2,pady=20)
    return