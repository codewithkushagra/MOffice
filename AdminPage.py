import tkinter
from tkinter.constants import *

import WorkEntry
import AdminButtons
import globalvalues


def admin(root):

    adminpageframe=tkinter.Frame(root)
    adminpageframe.grid(row=0, column=0, sticky=NSEW,ipadx=globalvalues.WIDTH,ipady=globalvalues.HEIGHT)

    
    
    
    WorkEntry.enterWork(adminpageframe)

    return




































    # tkinter.Frame(contentframe).grid(row=0,column=0,ipady=300,ipadx=350)



    
    # list=tkinter.Frame(contentframe)
    # list.grid(row=0,column=0,sticky=NSEW)
    # ListPage.workList(list)

    # reports=tkinter.Frame(contentframe)
    # reports.grid(row=0,column=0,sticky=NSEW)
    # ReportsPage.reportList(reports)

    # allotwork=tkinter.Frame(contentframe)
    # allotwork.grid(row=0,column=0,sticky=NSEW)
    # AllotWorkPage.allotWorkList(allotwork)

    # todayswork=tkinter.Frame(contentframe)
    # todayswork.grid(row=0,column=0,sticky=NSEW)
    # TodaysWorkPage.todaysWorkList(todayswork)

    # workdiary=tkinter.Frame(contentframe)
    # workdiary.grid(row=0,column=0,sticky=NSEW)
    # WorkDiaryPage.workDiaryList(workdiary)

    # register=tkinter.Frame(contentframe)
    # register.grid(row=0,column=0,sticky=NSEW)
    # RegistrationPage.registeruser(register)    

    

    # workentrysection=tkinter.Frame(contentframe)
    # workentrysection.grid(row=0,column=0,sticky=NSEW)
    # WorkEntrySection.enterWorkIn(workentrysection)

    # newparty=tkinter.Frame(contentframe)
    # newparty.grid(row=0,column=0,sticky=NSEW)
    # NewParty.newParty(newparty)

    # newgroup=tkinter.Frame(contentframe)
    # newgroup.grid(row=0,column=0,sticky=NSEW)
    # NewGroup.newGroup(newgroup)