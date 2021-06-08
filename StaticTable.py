import tkinter
from tkinter import *
from tkinter.constants import *

import FrameSwitcher
import globalvalues
import DBMSGetData

def drawTable(root,table,allotnow=False):
    def data():
         
         Label(frame,text="Group Name",borderwidth=1,bg="white",font="Time 14",relief=RAISED).grid(row=0,ipadx=10,ipady=10,column=0,sticky=NSEW)
         Label(frame,text="Party Name",borderwidth=1,bg="white",font="Time 14",relief=RAISED).grid(row=0,ipadx=10,ipady=10,column=1,sticky=NSEW)
         Label(frame,text="PAN No",borderwidth=1,bg="white",font="Time 14",relief=RAISED).grid(row=0,ipadx=10,ipady=10,column=2,sticky=NSEW)
         Label(frame,text="Department",borderwidth=1,bg="white",font="Time 14",relief=RAISED).grid(row=0,ipadx=10,ipady=10,column=3,sticky=NSEW)
         Label(frame,text="Type",borderwidth=1,bg="white",font="Time 14",relief=RAISED).grid(row=0,ipadx=10,ipady=10,column=4,sticky=NSEW)
         Label(frame,text="Description",borderwidth=1,bg="white",font="Time 14",relief=RAISED).grid(row=0,ipadx=10,ipady=10,column=5,sticky=NSEW)
         Label(frame,text="Assessment Year",borderwidth=1,bg="white",font="Time 14",relief=RAISED).grid(row=0,ipadx=10,ipady=10,column=6,sticky=NSEW)
         Label(frame,text="Recieve Date",borderwidth=1,bg="white",font="Time 14",relief=RAISED).grid(row=0,ipadx=10,ipady=10,column=7,sticky=NSEW)
         Label(frame,text="Work Status",borderwidth=1,bg="white",font="Time 14",relief=RAISED).grid(row=0,ipadx=10,ipady=10,column=8,sticky=NSEW)
         Label(frame,text="Alloted To",borderwidth=1,bg="white",font="Time 14",relief=RAISED).grid(row=0,ipadx=10,ipady=10,column=9,sticky=NSEW)
         button=[]
         buttonindex=0
         row=1
         for i in table:
            partyandgroup=DBMSGetData.getParty(i[1],"GROUPANDPARTYDETAILS")
          
            Label(frame,text=partyandgroup[1],font="Time 12",borderwidth=1).grid(row=row,padx=10,ipady=10,column=0,sticky=W)
            Label(frame,text=partyandgroup[0],font="Time 12",borderwidth=1).grid(row=row,padx=10,ipady=10,column=1,sticky=W)
            Label(frame,text=i[1],borderwidth=1,font="Time 12").grid(row=row,padx=10,ipady=10,column=2,sticky=W)
            Label(frame,text=i[2],borderwidth=1,font="Time 12").grid(row=row,padx=10,ipady=10,column=3,sticky=W)
            Label(frame,text=i[3],borderwidth=1,font="Time 12").grid(row=row,padx=10,ipady=10,column=4,sticky=W)
            Label(frame,text=i[4],borderwidth=1,font="Time 12").grid(row=row,padx=10,ipady=10,column=5,sticky=W)
            Label(frame,text=i[5],borderwidth=1,font="Time 12").grid(row=row,padx=10,ipady=10,column=6,sticky=W)
            Label(frame,text=i[6],borderwidth=1,font="Time 12").grid(row=row,padx=10,ipady=10,column=7,sticky=W)
            Label(frame,text=i[11],borderwidth=1,font="Time 12").grid(row=row,padx=10,ipady=10,column=8,sticky=W)
            if not allotnow:
                Label(frame,text=i[12],borderwidth=1,font="Time 12").grid(row=row,padx=10,ipady=10,column=9,sticky=W)
            else:
                if i[12]=='None':
                    button.append(Button(frame,text="Allot",borderwidth=1,font="Time 12",command=lambda:FrameSwitcher))
                    button[buttonindex].grid(row=row,padx=10,ipady=10,column=9,sticky=EW)
                    buttonindex+=1
                else:
                    button.append(Button(frame,text="Update",borderwidth=1,font="Time 12"))
                    button[buttonindex].grid(row=row,padx=10,ipady=10,column=9,sticky=EW)
                    buttonindex+=1
            
            row+=1
    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"),width=globalvalues.WIDTH-300,height=globalvalues.HEIGHT-300)
    
    myframe=tkinter.Frame(root,relief=GROOVE,width=globalvalues.WIDTH-200,height=globalvalues.HEIGHT-300,bd=1)
    myframe.place(x=0,y=15)
    canvas=tkinter.Canvas(myframe)
    frame=tkinter.Frame(canvas)
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