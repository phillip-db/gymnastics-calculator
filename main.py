import os
import json_decoder as json
from tkinter import *
from tkinter import messagebox

buttonCount = 0


def msg_box(text="Hello World!"):
    messagebox.showinfo(message=text)


def event_button(eventName, cmd, *args):
    global buttonCount

    eventButton = Button(
        mainframe,
        text=eventName,
        padx=15,
        pady=15,
        command=lambda: cmd(*args),
    )
    eventButton.grid(row=1, column=buttonCount)
    buttonCount += 1


def entries_dropdown(vaultData):
    list = entriesframe.grid_slaves() + exitsframe.grid_slaves()
    for l in list:
        l.destroy()

    entries = json.get_entries(vaultData)

    entryVar = StringVar(entriesframe)
    entryVar.set("Select Entry")

    entryDropdown = OptionMenu(
        entriesframe,
        entryVar,
        *entries,
        command=lambda x: exits_dropdown(vaultData, entries, entryVar.get())
    )
    entryDropdown.config(width=20)
    entryDropdown.grid(column=0, row=2)


def exits_dropdown(vaultData, entries, entryName):
    list = exitsframe.grid_slaves()
    for l in list:
        l.destroy()

    exitVar = StringVar(exitsframe)
    exitVar.set("Select Exit")

    exits = json.get_exits(vaultData, entries.index(entryName))
    exitNames = [exit["exitName"] for exit in exits]

    exitDropdown = OptionMenu(
        exitsframe,
        exitVar,
        *exitNames,
        command=lambda x: msg_box(
            "{} into {} worth {} points in difficulty".format(
                entryName, exitVar.get(), exits[exitNames.index(exitVar.get())]["value"]
            )
        )
    )
    exitDropdown.grid(column=1, row=2)


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

# Load Vault JSON
vaultData = json.load_vaults(json.vault_path)

entriesframe = Frame(mainframe)
entriesframe.grid(column=0, row=2)
exitsframe = Frame(mainframe)
exitsframe.grid(column=1, row=2)

event_button("Vault", entries_dropdown, vaultData)
event_button("Bars", msg_box)
event_button("Floor", msg_box)
event_button("Beam", msg_box)

# entries_dropdown(vaultData)

root.mainloop()
