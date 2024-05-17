# pylint disable=unused-import

from tkinter import Tk
from tkinter import Label
import time
import sys

master = Tk()
master.title("Kimathi's Digital Clock")


def get_time():
    timeVar = time.strftime("%H:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200, get_time)     

Label(master, font=("Arial", 10), text="Kimathi's Digital Clock", bg="black", fg="white").pack()
clock = Label(master, font=("Calibri", 60), bg="black", fg="white")
clock.pack()

get_time()

master.mainloop()
