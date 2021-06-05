import tkinter
from tkinter import *
from tkinter.constants import *

import LoginPageVaribles


def article(root):

    contentframe=tkinter.Frame(root)
    contentframe.grid(row=0,column=0)

    loginlabel=tkinter.Label(contentframe,text=f"Hello {LoginPageVaribles.CURRENTUSER} !!!")
    loginlabel.grid(row=0,column=0,columnspan=2,sticky=W)

    

    return


