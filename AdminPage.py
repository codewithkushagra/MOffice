import tkinter
from tkinter.constants import *
import AdminButtons
import RegistrationPage



def admin(root):




    contentframe=tkinter.Frame(root)
    contentframe.grid(row=0,column=1)

    tkinter.Frame(contentframe,bg="white").grid(row=0,column=0,ipady=300,ipadx=350)


    workentry=tkinter.Frame(contentframe,bg="white")
    workentry.grid(row=0,column=0,sticky=NSEW)

    workentry=tkinter.Frame(contentframe,bg="white")
    workentry.grid(row=0,column=0,sticky=NSEW)

    list=tkinter.Frame(contentframe,bg="white")
    list.grid(row=0,column=0,sticky=NSEW)

    reports=tkinter.Frame(contentframe,bg="white")
    reports.grid(row=0,column=0,sticky=NSEW)

    allotwork=tkinter.Frame(contentframe,bg="white")
    allotwork.grid(row=0,column=0,sticky=NSEW)

    todayswork=tkinter.Frame(contentframe,bg="white")
    todayswork.grid(row=0,column=0,sticky=NSEW)


    workdairy=tkinter.Frame(contentframe,bg="white")
    workdairy.grid(row=0,column=0,sticky=NSEW)


    register=tkinter.Frame(contentframe,bg="white")
    register.grid(row=0,column=0,sticky=NSEW)
    RegistrationPage.registeruser(register)    
    
    tkinter.Frame(root).grid(row=0,column=0,rowspan=7,ipady=300)

    buttonframe=tkinter.Frame(root)
    buttonframe.grid(row=0,column=0,rowspan=7,sticky=N)

    AdminButtons.buttonCreate(buttonframe,workentry,list,reports,allotwork,todayswork,workdairy,register)
    return