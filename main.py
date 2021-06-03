from tkinter import *
from tkinter.constants import *
import tkinter
from tkinter import messagebox


import AdminPage
import ArticlePage
import appwindow
import LoginPage



def ControlFrame(root):

    
    
    #adminframe initialization
    adminframe=tkinter.Frame(root)
    adminframe.place(x=0,y=0)
    #adminframe call
    AdminPage.admin(adminframe)


    #articleframe initialization
    articleframe=tkinter.Frame(root)
    articleframe.place(x=0,y=0)
    #articleframe call
    ArticlePage.article(articleframe)



    #emptyframe initialization
    emptyframe=tkinter.Frame(root)
    emptyframe.pack(expand=True,fill="both")

    #loginframe initialization
    loginframe=tkinter.Frame(app)
    loginframe.place(x=appwindow.WIDTH/10,y=appwindow.HEIGHT/10)
    #loginframe call
    LoginPage.login(loginframe,adminframe,articleframe,emptyframe)



    return





if __name__ == "__main__":
    app = appwindow.App()
    ControlFrame(app)
    app.mainloop()