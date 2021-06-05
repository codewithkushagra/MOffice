import tkinter
from tkinter.constants import *
from tkinter import messagebox

import LoginPageVaribles
import FrameSwitcher



def check(password,username):
    try:
        usernameindex=LoginPageVaribles.USERNAME.index(username)
    except:
        usernameindex=-1
    if username=="b" and password=="b":
        return "admin"
    elif usernameindex+1 and password==LoginPageVaribles.PASSWORD[usernameindex]:  #check if the username and the corresponding password is present in the list or not
        LoginPageVaribles.CURRENTUSER=username
        return "article"
    else:
        return "error"

def onPress(root,prime,password,username):
    if check(password,username)=="admin":
        FrameSwitcher.recreateAdminPage(root,prime)
        pass
    elif check(password,username)=="article":
        FrameSwitcher.recreateArticlePage(root,prime)
    else:
        messagebox.showerror("Error","Please check the password or the username you entered")
    return





def login(root,prime):


    username=tkinter.StringVar(root)
    password=tkinter.StringVar(root)

    loginlabel=tkinter.Label(root,text="LOGIN -")
    loginlabel.grid(row=0,column=0,columnspan=2,sticky=W,pady=10,padx=10)


    usernamelabel=tkinter.Label(root,text="Username:")
    passwordlabel=tkinter.Label(root,text="Password:")

    usernamelabel.grid(row=1,column=0,sticky=W,pady=10,padx=10)
    passwordlabel.grid(row=2,column=0,sticky=W,pady=10,padx=10)

    usernameentry=tkinter.Entry(root,textvariable=username)
    passwordentry=tkinter.Entry(root,show='*',textvariable=password)

    usernameentry.grid(row=1,column=1,sticky=W,pady=10,padx=10)
    passwordentry.grid(row=2,column=1,sticky=W,pady=10,padx=10)

    loginbutton=tkinter.Button(root,text="Login",command=lambda :onPress(root,prime,password.get(),username.get()))
    loginbutton.grid(row=3,column=0,columnspan=2,pady=10,padx=10)
    
    return