import tkinter
from tkinter.constants import *
import FrameSwitcher

def buttonCreate(buttonframe,workentry,list,reports,allotwork,todayswork,workdairy,register):
    workentrybutton=tkinter.Button(buttonframe,text="Work Entry",command=lambda :FrameSwitcher.switchAdminFrame(workentry))
    workentrybutton.grid(row=0,column=0,padx=5,pady=5)
    listbutton=tkinter.Button(buttonframe,text="List")
    listbutton.grid(row=1,column=0,padx=5,pady=5)
    reportbutton=tkinter.Button(buttonframe,text="Reports")
    reportbutton.grid(row=2,column=0,padx=5,pady=5)
    allotworkbutton=tkinter.Button(buttonframe,text="Allot Work")
    allotworkbutton.grid(row=3,column=0,padx=5,pady=5)
    todaystargetbutton=tkinter.Button(buttonframe,text="Todays Target")
    todaystargetbutton.grid(row=4,column=0,padx=5,pady=5)
    workdairybutton=tkinter.Button(buttonframe,text="Work Dairy")
    workdairybutton.grid(row=5,column=0,padx=5,pady=5)
    registerbutton=tkinter.Button(buttonframe,text="Register",command=lambda :FrameSwitcher.switchAdminFrame(register))
    registerbutton.grid(row=6,column=0,padx=5,pady=5)
    articlebutton=tkinter.Button(buttonframe,text="Articles")
    articlebutton.grid(row=7,column=0,padx=5,pady=5)