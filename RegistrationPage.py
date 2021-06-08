import tkinter
from tkinter.constants import *
from tkinter import messagebox

import AdminButtonGlobal
import globalvalues
import DBMSSaveData


def saveTeam(usernamevar,namevar,passwordvar,staffdeginationvar,emailvar,phonevar,username,name,password,staffdegination,email,phone):

    if username=="" or name=="" or password=="" or staffdegination=="None" or email=="" or phone=="":
        messagebox.showerror("Error","Empty Feild")
    else:
        DBMSSaveData.insertTeam(username,name,password,staffdegination,email,phone)
        usernamevar.set("")
        namevar.set("")
        passwordvar.set("")
        staffdeginationvar.set("None")
        emailvar.set("")
        phonevar.set("")
        messagebox.showinfo("Saved","New Team member added")
        
    return




def registeruser(root):

    contentframe=tkinter.Frame(root)
    contentframe.grid(row=0,column=1,ipadx=globalvalues.HEIGHT,ipady=globalvalues.WIDTH-100)
    
    tkinter.Label(contentframe,text="ADD NEW USER-",font="Time 14").grid(row=0,column=0,sticky=W,pady=7)
    
    username=tkinter.StringVar(contentframe)
    tkinter.Label(contentframe,text="Username:").grid(row=1,column=0,sticky=W,pady=7)
    tkinter.Entry(contentframe, bd=1 ,width=20,textvariable=username).grid(row=1,column=1,sticky=W,padx=8,pady=5)

    name=tkinter.StringVar(contentframe)
    tkinter.Label(contentframe,text="Name:").grid(row=2,column=0,sticky=W,pady=7)
    tkinter.Entry(contentframe, bd=1 ,width=20,textvariable=name).grid(row=2,column=1,sticky=W,padx=8,pady=5)
    
    password=tkinter.StringVar(contentframe)
    tkinter.Label(contentframe,text="Password:").grid(row=3,column=0,sticky=W,pady=7)
    tkinter.Entry(contentframe, bd=1 ,width=20,show='*',textvariable=password).grid(row=3,column=1,sticky=W,padx=8,pady=5)
    
    staffdegination=tkinter.StringVar(contentframe)
    staffdeginationlist = ["Boss","Dept Head","Executive","Accountant","Article","other staff"]
    staffdegination.set("None")
    tkinter.Label(contentframe,text="Degination:").grid(row=4,column=0,sticky=W)
    tkinter.OptionMenu(contentframe,staffdegination,*staffdeginationlist).grid(row=4,column=1,sticky=W,padx=8)
    
    email=tkinter.StringVar(contentframe)
    tkinter.Label(contentframe,text="Email:").grid(row=5,column=0,sticky=W,pady=7)
    tkinter.Entry(contentframe, bd=1 ,width=20,textvariable=email).grid(row=5,column=1,sticky=W,padx=8,pady=5)

    phone=tkinter.StringVar(contentframe)
    tkinter.Label(contentframe,text="Phone No:").grid(row=6,column=0,sticky=W,pady=7)
    tkinter.Entry(contentframe, bd=1 ,width=20,textvariable=phone).grid(row=6,column=1,sticky=W,padx=8,pady=5)

    tkinter.Button(contentframe,text="Save",command=lambda:saveTeam(username,name,password,staffdegination,email,phone,username.get(),name.get(),password.get(),staffdegination.get(),email.get(),phone.get())).grid(row=7,columnspan=2,pady=20)

    AdminButtonGlobal.CURRENTFRAME=contentframe

    return