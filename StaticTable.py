import tkinter
from tkinter import *
from tkinter.constants import *



def drawTable(root):
    def data():
         
         Label(frame,text="Group Name",bg="white",borderwidth=1,relief="solid").grid(row=0,ipadx=2,column=0)
         Label(frame,text="Party Name",bg="white",borderwidth=1,relief="solid").grid(row=0,ipadx=2,column=1)
         Label(frame,text="PEN No.",bg="white",borderwidth=1,relief="solid").grid(row=0,ipadx=2,column=2)
         Label(frame,text="Department",bg="white",borderwidth=1,relief="solid").grid(row=0,ipadx=2,column=3)
         Label(frame,text="Type",bg="white",borderwidth=1,relief="solid").grid(row=0,ipadx=2,column=4)
         Label(frame,text="Description",bg="white",borderwidth=1,relief="solid").grid(row=0,ipadx=2,column=5)
         Label(frame,text="Assessment Year",bg="white",borderwidth=1,relief="solid").grid(row=0,ipadx=2,column=6)
         Label(frame,text="Recieve Date",bg="white",borderwidth=1,relief="solid").grid(row=0,ipadx=2,column=7)
         Label(frame,text="Work Status",bg="white",borderwidth=1,relief="solid").grid(row=0,ipadx=2,column=8)
         Label(frame,text="Alloted To",bg="white",borderwidth=1,relief="solid").grid(row=0,ipadx=2,column=9)

     
    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"),width=580,height=450)
    
    myframe=tkinter.Frame(root,relief=GROOVE,width=600,height=450,bd=1,bg="white")
    myframe.place(x=0,y=15)
    canvas=tkinter.Canvas(myframe)
    frame=tkinter.Frame(canvas,bg="white")
    myscrollbar=tkinter.Scrollbar(myframe,orient="vertical",command=canvas.yview)
    myscrollbar1=tkinter.Scrollbar(myframe,orient="horizontal",command=canvas.xview)
    canvas.configure(yscrollcommand=myscrollbar.set)
    canvas.configure(xscrollcommand=myscrollbar1.set)
    myscrollbar1.pack(side="bottom",fill="x")
    myscrollbar.pack(side="right",fill="y")
    
    canvas.pack(side="left")
    canvas.create_window((0,0),window=frame,anchor='nw')
    frame.bind("<Configure>",myfunction)
    data()
    return