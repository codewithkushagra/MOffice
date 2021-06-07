import tkinter as tk

HEIGHT,WIDTH=600,800

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        global HEIGHT
        global WIDTH
        WIDTH=self.winfo_screenwidth()
        HEIGHT=self.winfo_screenheight()
        self.title("OFFICE MANAGEMENT")
        self.geometry('%dx%d+0+0'%(self.winfo_screenwidth(),self.winfo_screenheight()))
        self.resizable(0,0)