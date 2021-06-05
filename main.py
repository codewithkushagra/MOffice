from tkinter import *
from tkinter.constants import *
import tkinter
from tkinter import messagebox
import NewPartyVariables

import DBMSGetData
import appwindow
import LoginPage



def ControlFrame(root):

    loginframe=tkinter.Frame(root)
    loginframe.grid(row=0,column=0,sticky=NSEW)
    #loginframe call
    LoginPage.login(loginframe,root)

    return





if __name__ == "__main__":

    NewPartyVariables.CURRENTPARTYLIST=DBMSGetData.getData("GROUPANDPARTYDETAILS","PARTYNAME")[0]
    print(NewPartyVariables.CURRENTPARTYLIST)
    app = appwindow.App()
    ControlFrame(app)
    app.mainloop()