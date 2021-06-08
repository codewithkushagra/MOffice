import tkinter
from tkinter.constants import *
import FrameSwitcher

import AdminButtonGlobal



def buttonCreate(buttonframe,root):
    workentrybutton=tkinter.Button(buttonframe,text="Work Entry",width=10,bg="white",border=0,command=lambda :FrameSwitcher.recreateWorkEntry(AdminButtonGlobal.CURRENTFRAME,root))
    workentrybutton.grid(row=0,column=0,padx=5,pady=10,sticky=NSEW)
    listbutton=tkinter.Button(buttonframe,text="Work List",width=10,bg="white",border=0,command=lambda :FrameSwitcher.recreateListPage(AdminButtonGlobal.CURRENTFRAME,root))
    listbutton.grid(row=1,column=0,padx=5,pady=10,sticky=NSEW)
    reportbutton=tkinter.Button(buttonframe,text="Reports",width=10,bg="white",border=0,command=lambda :FrameSwitcher.recreateReportsPage(AdminButtonGlobal.CURRENTFRAME,root))
    reportbutton.grid(row=2,column=0,padx=5,pady=10,sticky=NSEW)
    allotworkbutton=tkinter.Button(buttonframe,text="Allot Work",width=10,bg="white",border=0,command=lambda :FrameSwitcher.recreateAllotWorkPage(AdminButtonGlobal.CURRENTFRAME,root))
    allotworkbutton.grid(row=3,column=0,padx=5,pady=10,sticky=NSEW)
    todaystargetbutton=tkinter.Button(buttonframe,text="Today's Work",width=10,bg="white",border=0,command=lambda :FrameSwitcher.recreateTodaysWorkPage(AdminButtonGlobal.CURRENTFRAME,root))
    todaystargetbutton.grid(row=4,column=0,padx=5,pady=10,sticky=NSEW)
    workdiarybutton=tkinter.Button(buttonframe,text="Work Dairy",width=10,bg="white",border=0,command=lambda :FrameSwitcher.recreateWorkDiaryPage(AdminButtonGlobal.CURRENTFRAME,root))
    workdiarybutton.grid(row=5,column=0,padx=5,pady=10,sticky=NSEW)
    registerbutton=tkinter.Button(buttonframe,text="Register Team",width=10,bg="white",border=0,command=lambda :FrameSwitcher.recreateRegistrationPage(AdminButtonGlobal.CURRENTFRAME,root))
    registerbutton.grid(row=6,column=0,padx=5,pady=10,sticky=NSEW)
    articlebutton=tkinter.Button(buttonframe,text="Team",width=10,bg="white",border=0)
    articlebutton.grid(row=7,column=0,padx=5,pady=10,sticky=NSEW)