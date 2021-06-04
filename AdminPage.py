import tkinter
from tkinter.constants import *


import AdminButtons
import RegistrationPage
import WorkEntry
import NewParty
import ListPage
import NewGroup
import WorkEntrySection
import ReportsPage
import AllotWorkPage
import TodaysWorkPage
import WorkDiaryPage


def admin(root):


    contentframe=tkinter.Frame(root)
    contentframe.grid(row=0,column=1)

    tkinter.Frame(contentframe,bg="white").grid(row=0,column=0,ipady=300,ipadx=350)



    workentry=tkinter.Frame(contentframe,bg="white")
    workentry.grid(row=0,column=0,sticky=NSEW)

    list=tkinter.Frame(contentframe,bg="white")
    list.grid(row=0,column=0,sticky=NSEW)
    ListPage.workList(list)

    reports=tkinter.Frame(contentframe,bg="white")
    reports.grid(row=0,column=0,sticky=NSEW)
    ReportsPage.reportList(reports)

    allotwork=tkinter.Frame(contentframe,bg="white")
    allotwork.grid(row=0,column=0,sticky=NSEW)
    AllotWorkPage.allotWorkList(allotwork)

    todayswork=tkinter.Frame(contentframe,bg="white")
    todayswork.grid(row=0,column=0,sticky=NSEW)
    TodaysWorkPage.todaysWorkList(todayswork)

    workdiary=tkinter.Frame(contentframe,bg="white")
    workdiary.grid(row=0,column=0,sticky=NSEW)
    WorkDiaryPage.workDiaryList(workdiary)

    register=tkinter.Frame(contentframe,bg="white")
    register.grid(row=0,column=0,sticky=NSEW)
    RegistrationPage.registeruser(register)    

    

    workentrysection=tkinter.Frame(contentframe,bg="white")
    workentrysection.grid(row=0,column=0,sticky=NSEW)
    WorkEntrySection.enterWorkIn(workentrysection)

    newparty=tkinter.Frame(contentframe,bg="white")
    newparty.grid(row=0,column=0,sticky=NSEW)
    NewParty.newParty(newparty)

    newgroup=tkinter.Frame(contentframe,bg="white")
    newgroup.grid(row=0,column=0,sticky=NSEW)
    NewGroup.newGroup(newgroup)
    
    workentry=tkinter.Frame(contentframe,bg="white")
    workentry.grid(row=0,column=0,sticky=NSEW)
    WorkEntry.enterWork(workentry,newgroup,newparty,workentrysection)

    buttonframe=tkinter.Frame(root)
    tkinter.Frame(buttonframe,bg="black").grid(row=0,column=0,rowspan=8,ipady=300,ipadx=100)
    buttonframe.grid(row=0,column=0,rowspan=7,sticky=N)

    AdminButtons.buttonCreate(buttonframe,workentry,list,reports,allotwork,todayswork,workdiary,register)
    return