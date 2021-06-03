import tkinter as tk

HEIGHT,WIDTH=600,800

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("OFFICE MANAGEMENT")
        self.geometry('800x600')
        self.resizable(0,0)