#! /usr/bin/env python3


import tkinter as tk
import time

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        timedisplay = time.strftime("%H:%M:%S")
        timelist = timedisplay.split(':')
        H = int(timelist[0])
        M = int(timelist[1])
        S = int(timelist[2])
        timeismoney = ((H-9)*60*60 + M*60 + S)*0.022446689113356
        self.label.configure(text=timeismoney)
        self.root.after(1000, self.update_clock)

app=App()
