import tkinter
from tkinter.constants import *
from tkinter import messagebox

def buttonCreate(buttonframe):
    reportbutton=tkinter.Button(buttonframe,text="Work Entry")
    reportbutton.grid(row=0,column=0,padx=5,pady=10)
    reportbutton=tkinter.Button(buttonframe,text="List")
    reportbutton.grid(row=1,column=0,padx=5,pady=10)
    reportbutton=tkinter.Button(buttonframe,text="Reports")
    reportbutton.grid(row=2,column=0,padx=5,pady=10)
    reportbutton=tkinter.Button(buttonframe,text="Allot Work")
    reportbutton.grid(row=3,column=0,padx=5,pady=10)
    reportbutton=tkinter.Button(buttonframe,text="Todays Target")
    reportbutton.grid(row=4,column=0,padx=5,pady=10)
    reportbutton=tkinter.Button(buttonframe,text="Work Dairy")
    reportbutton.grid(row=5,column=0,padx=5,pady=10)
    reportbutton=tkinter.Button(buttonframe,text="Register")
    reportbutton.grid(row=6,column=0,padx=5,pady=10)
    reportbutton=tkinter.Button(buttonframe,text="Articles")
    reportbutton.grid(row=7,column=0,padx=5,pady=10)