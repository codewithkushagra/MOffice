import tkinter
from tkinter import *
from tkinter.constants import *
from tkinter import messagebox



def switchFrame(emptyframe,root):
    emptyframe.tkraise()
    root.tkraise()    
    return



# def currentFrameCheck(CHECKVALUE):
#     if CHECKVALUE=="admin":
#         switchFrame(main.emptyframe,main.adminframe)
#     elif CHECKVALUE=="login":
#         switchFrame(main.emptyframe,main.loginframe)
#     elif CHECKVALUE=="article":
#         switchFrame(main.emptyframe,main.articleframe)
#     else:
#         messagebox.showerror("Error","Please check the password or the username you entered")