import tkinter
from tkinter.constants import *
from tkinter import messagebox

import AdminButtons

def registeruser(root):

    contentframe=tkinter.Frame(root)
    contentframe.grid(row=0,column=1)
    
    tkinter.Label(contentframe,text="ADD NEW USER-").grid(row=0,column=0,sticky=W,pady=7)
    
    tkinter.Label(contentframe,text="Username:").grid(row=1,column=0,sticky=W,pady=7)
    tkinter.Entry(contentframe, bd=1 ,width=20).grid(row=1,column=1,sticky=W,padx=8,pady=5)


    tkinter.Label(contentframe,text="Name:").grid(row=2,column=0,sticky=W,pady=7)
    tkinter.Entry(contentframe, bd=1 ,width=20).grid(row=2,column=1,sticky=W,padx=8,pady=5)
    
    
    tkinter.Label(contentframe,text="Password:").grid(row=3,column=0,sticky=W,pady=7)
    tkinter.Entry(contentframe, bd=1 ,width=20,show='*').grid(row=3,column=1,sticky=W,padx=8,pady=5)
    
    staffdegination=tkinter.StringVar(contentframe)
    staffdeginationlist = ["CA","Accountant","Article"]
    staffdegination.set("None")
    tkinter.Label(contentframe,text="Degination:").grid(row=4,column=0,sticky=W)
    tkinter.OptionMenu(contentframe,staffdegination,*staffdeginationlist).grid(row=4,column=1,sticky=W,padx=8)
    
    tkinter.Label(contentframe,text="Email:").grid(row=5,column=0,sticky=W,pady=7)
    tkinter.Entry(contentframe, bd=1 ,width=20).grid(row=5,column=1,sticky=W,padx=8,pady=5)

    tkinter.Label(contentframe,text="Phone No:").grid(row=6,column=0,sticky=W,pady=7)
    tkinter.Entry(contentframe, bd=1 ,width=20).grid(row=6,column=1,sticky=W,padx=8,pady=5)

    tkinter.Button(contentframe,text="Save").grid(row=7,columnspan=2,pady=20)

    buttonframe=tkinter.Frame(root)
    tkinter.Frame(buttonframe,relief=RIDGE,borderwidth=2).grid(row=0,column=0,rowspan=8,ipady=300,ipadx=100)
    buttonframe.grid(row=0,column=0,rowspan=7,sticky=N)


    AdminButtons.buttonCreate(buttonframe,contentframe,root)

    return