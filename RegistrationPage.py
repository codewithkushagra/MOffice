import tkinter
from tkinter.constants import *
from tkinter import messagebox

def registeruser(root):
    
    tkinter.Label(root,text="ADD NEW USER-",bg="white").grid(row=0,column=0,sticky=W,pady=7)
    
    tkinter.Label(root,text="Username:",bg="white").grid(row=1,column=0,sticky=W,pady=7)
    tkinter.Entry(root, bd=1 ,width=20).grid(row=1,column=1,sticky=W,padx=8,pady=5)


    tkinter.Label(root,text="Name:",bg="white").grid(row=2,column=0,sticky=W,pady=7)
    tkinter.Entry(root, bd=1 ,width=20).grid(row=2,column=1,sticky=W,padx=8,pady=5)
    
    
    tkinter.Label(root,text="Password:",bg="white").grid(row=3,column=0,sticky=W,pady=7)
    tkinter.Entry(root, bd=1 ,width=20,show='*').grid(row=3,column=1,sticky=W,padx=8,pady=5)
    
    
    tkinter.Label(root,text="Phone No:",bg="white").grid(row=4,column=0,sticky=W,pady=7)
    tkinter.Entry(root, bd=1 ,width=20).grid(row=4,column=1,sticky=W,padx=8,pady=5)
    

    tkinter.Button(root,text="Save").grid(row=5,columnspan=2,pady=20)

    return