from tkinter import *
from tkinter.constants import *
import tkinter

import globalvalues

import appwindow
import LoginPage



def ControlFrame(root):

    loginframe=tkinter.Frame(root)
    loginframe.grid(row=0,column=0,sticky=NSEW)
    #loginframe call
    LoginPage.login(loginframe,root)

    return


if __name__ == "__main__":

    app = appwindow.App()
    ControlFrame(app)
    globalvalues.HEIGHT =appwindow.HEIGHT
    globalvalues.WIDTH =appwindow.WIDTH
    app.mainloop()