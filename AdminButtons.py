import tkinter
from tkinter.constants import *
import FrameSwitcher

def buttonCreate(buttonframe,workentry,list,reports,allotwork,todayswork,workdairy,register):
    workentrybutton=tkinter.Button(buttonframe,text="Work Entry",width=10,command=lambda :FrameSwitcher.switchAdminFrame(workentry))
    workentrybutton.grid(row=0,column=0,padx=5,pady=5)
    listbutton=tkinter.Button(buttonframe,text="List",width=10)
    listbutton.grid(row=1,column=0,padx=5,pady=5)
    reportbutton=tkinter.Button(buttonframe,text="Reports",width=10)
    reportbutton.grid(row=2,column=0,padx=5,pady=5)
    allotworkbutton=tkinter.Button(buttonframe,text="Allot Work",width=10)
    allotworkbutton.grid(row=3,column=0,padx=5,pady=5)
    todaystargetbutton=tkinter.Button(buttonframe,text="Todays Target",width=10)
    todaystargetbutton.grid(row=4,column=0,padx=5,pady=5)
    workdairybutton=tkinter.Button(buttonframe,text="Work Dairy",width=10)
    workdairybutton.grid(row=5,column=0,padx=5,pady=5)
    registerbutton=tkinter.Button(buttonframe,text="Register",width=10,command=lambda :FrameSwitcher.switchAdminFrame(register))
    registerbutton.grid(row=6,column=0,padx=5,pady=5)
    articlebutton=tkinter.Button(buttonframe,text="Articles",width=10)
    articlebutton.grid(row=7,column=0,padx=5,pady=5)