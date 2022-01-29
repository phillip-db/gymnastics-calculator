from email import message
import tkinter
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

buttonCount = 0


def msg_box(text):
    messagebox.showinfo(message=text)


def event_button(eventName, cmd):
    global buttonCount

    eventButton = Button(mainframe, text=eventName, padx=15, pady=15, command=(lambda: cmd("Clicked {}".format(eventName))))
    eventButton.grid(row=1, column=buttonCount)
    buttonCount += 1


os.environ["DISPLAY"] = ":0.0"
root = Tk()

width = 1000
height = 500

root.title("Gymnastics Calculator")
root.minsize(width, height)
root.geometry("{}x{}".format(width, height))

mainframe = Frame(root)
mainframe.grid(row=1, column=0)

titleframe = Frame(root, bg="yellow")
titleframe.grid(row=0, column=0)

eventLabel = Label(titleframe, text="Select Event")
eventLabel.grid(column=0, row=0)

titleframe.update()
xbias = int(width) / 2 - titleframe.winfo_width() / 2
titleframe.grid(column=0, row=0, padx=xbias, pady=10)

event_button("Vault", msg_box)
event_button("Bars", msg_box)
event_button("Floor", msg_box)
event_button("Beam", msg_box)

root.mainloop()
