import tkinter
from tkinter.constants import *
from tkinter import messagebox

def registeruser(root):
    tkinter.Label(root,text="USERNAME:",bg="white").grid(row=0,column=0,sticky=W,pady=7)
    tkinter.Entry(root, bd=1 ,width=20).grid(row=0,column=1,sticky=W,padx=8,pady=5)

    tkinter.Label(root,text="NAME:",bg="white").grid(row=1,column=0,sticky=W,pady=7)
    tkinter.Entry(root, bd=1 ,width=20).grid(row=1,column=1,sticky=W,padx=8,pady=5)
    
    tkinter.Label(root,text="PASSWORD:",bg="white").grid(row=2,column=0,sticky=W,pady=7)
    tkinter.Entry(root, bd=1 ,width=20,show='*').grid(row=2,column=1,sticky=W,padx=8,pady=5)
    
    tkinter.Label(root,text="PHONE NO:",bg="white").grid(row=3,column=0,sticky=W,pady=7)
    tkinter.Entry(root, bd=1 ,width=20).grid(row=3,column=1,sticky=W,padx=8,pady=5)
    
    tkinter.Button(root,text="Save").grid(row=4,columnspan=2,pady=20)