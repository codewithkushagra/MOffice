import tkinter
from tkinter.constants import *
from tkinter import messagebox

import FrameSwitcher


def check():
    return "admin"

def onPress(root,adminframe,articleframe,emptyframe):
    if check()=="admin":
        FrameSwitcher.switchFrame(emptyframe,adminframe)
    elif check()=="article":
        FrameSwitcher.switchFrame(emptyframe,articleframe)
    else:
        messagebox.showerror("Error","Please check the password or the username you entered")
    return





def login(root,adminframe,articleframe,emptyframe):


    loginlabel=tkinter.Label(root,text="LOGIN -")
    loginlabel.grid(row=0,column=0,columnspan=2,sticky=W,pady=10,padx=10)


    username=tkinter.Label(root,text="Username:")
    password=tkinter.Label(root,text="Password:")

    username.grid(row=1,column=0,sticky=W,pady=10,padx=10)
    password.grid(row=2,column=0,sticky=W,pady=10,padx=10)

    usernameentry=tkinter.Entry(root)
    passwordentry=tkinter.Entry(root,show='*')

    usernameentry.grid(row=1,column=1,sticky=W,pady=10,padx=10)
    passwordentry.grid(row=2,column=1,sticky=W,pady=10,padx=10)

    loginbutton=tkinter.Button(root,text="Login",command=lambda :onPress(root,adminframe,articleframe,emptyframe))
    loginbutton.grid(row=3,column=0,columnspan=2,pady=10,padx=10)
    
    return