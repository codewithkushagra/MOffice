import tkinter
from tkinter.constants import *
import FrameSwitcher

def buttonCreate(buttonframe,workentry,list,reports,allotwork,todayswork,workdiary,register):
    workentrybutton=tkinter.Button(buttonframe,text="Work Entry",width=10,bg="white",border=0,command=lambda :FrameSwitcher.switchAdminFrame(workentry))
    workentrybutton.grid(row=0,column=0,padx=5,pady=5)
    listbutton=tkinter.Button(buttonframe,text="List",width=10,bg="white",border=0,command=lambda :FrameSwitcher.switchAdminFrame(list))
    listbutton.grid(row=1,column=0,padx=5,pady=5)
    reportbutton=tkinter.Button(buttonframe,text="Reports",width=10,bg="white",border=0,command=lambda :FrameSwitcher.switchAdminFrame(reports))
    reportbutton.grid(row=2,column=0,padx=5,pady=5)
    allotworkbutton=tkinter.Button(buttonframe,text="Allot Work",width=10,bg="white",border=0,command=lambda :FrameSwitcher.switchAdminFrame(allotwork))
    allotworkbutton.grid(row=3,column=0,padx=5,pady=5)
    todaystargetbutton=tkinter.Button(buttonframe,text="Todays Target",width=10,bg="white",border=0,command=lambda :FrameSwitcher.switchAdminFrame(todayswork))
    todaystargetbutton.grid(row=4,column=0,padx=5,pady=5)
    workdiarybutton=tkinter.Button(buttonframe,text="Work Dairy",width=10,bg="white",border=0,command=lambda :FrameSwitcher.switchAdminFrame(workdiary))
    workdiarybutton.grid(row=5,column=0,padx=5,pady=5)
    registerbutton=tkinter.Button(buttonframe,text="Register",width=10,bg="white",border=0,command=lambda :FrameSwitcher.switchAdminFrame(register))
    registerbutton.grid(row=6,column=0,padx=5,pady=5)
    articlebutton=tkinter.Button(buttonframe,text="Articles",width=10,bg="white",border=0)
    articlebutton.grid(row=7,column=0,padx=5,pady=5)