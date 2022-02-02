import os
import json_decoder as json
from tkinter import *
from tkinter import messagebox

buttonCount = 0


def msg_box(text="Hello World!"):
    messagebox.showinfo(message=text)


def clear_skillframe():
    global skillframe

    skillframe.grid_forget()
    skillframe = Frame(mainframe)
    skillframe.grid(row=1, column=0)


def event_button(eventName, cmd, *args):
    global buttonCount

    eventButton = Button(
        buttonframe,
        text=eventName,
        padx=15,
        pady=15,
        command=lambda: cmd(*args),
    )
    eventButton.grid(row=1, column=buttonCount)
    buttonCount += 1


def entries_dropdown(vaultData):
    global entriesframe

    clear_skillframe()
    entriesframe = Frame(skillframe)
    entriesframe.grid(column=0, row=0)

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
    entryDropdown.grid(column=0, row=0)


def exits_dropdown(vaultData, entries, entryName):
    global exitsframe

    exitsframe.grid_forget()
    exitsframe = Frame(skillframe)
    exitsframe.grid(column=0, row=1)

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
    exitDropdown.grid(column=0, row=1)


def create_test_dropdown(data):
    global testframe

    clear_skillframe()

    testframe = Frame(skillframe)
    testframe.grid(column=0, row=0)

    selectedSkills = Text(skillframe)
    selectedSkills.grid(column=0, row=1)

    submitButton = Button(
        skillframe,
        text="Calculate Score",
        command=lambda: msg_box(
            "Total Value: {}".format(
                test_calculate_score(data, selectedSkills.get("1.0", "end-2c"))
            )
        ),
    )
    submitButton.grid(column=0, row=2)

    test_dropdown(data, selectedSkills)


def select_test_skill(dropdown, data, index, output):
    output.insert(END, "{}\n".format(data["skills"][index]["skillname"]))
    dropdown.destroy()
    test_dropdown(data, output)


def test_dropdown(data, outputText):
    skillVar = StringVar(testframe)
    skillVar.set("Select Skill")

    skillNames = [skill["skillname"] for skill in data["skills"]]

    testDropdown = OptionMenu(
        testframe,
        skillVar,
        *skillNames,
        command=lambda x: select_test_skill(
            testDropdown, data, skillNames.index(skillVar.get()), outputText
        )
    )
    testDropdown.grid(column=0, row=0)


def test_calculate_score(data, skillText):
    skills = skillText.split("\n")
    skillNames = [skill["skillname"] for skill in data["skills"]]
    total = 0
    for skill in skills:
        try:
            index = skillNames.index(skill)
            total = round(total + data["skills"][index]["value"], 1)
        except ValueError:
            pass
    return total


os.environ["DISPLAY"] = ":0.0"
root = Tk()

width = 1000
height = 500

root.title("Gymnastics Calculator")
root.minsize(width, height)
root.geometry("{}x{}".format(width, height))

mainframe = Frame(root)
mainframe.grid(row=1, column=0)

buttonframe = Frame(mainframe)
buttonframe.grid(row=0, column=0)

titleframe = Frame(root, bg="yellow")
titleframe.grid(row=0, column=0)

skillframe = Frame(mainframe)
skillframe.grid(row=1, column=0)

eventLabel = Label(titleframe, text="Select Event")
eventLabel.grid(column=0, row=0)

titleframe.update()
xbias = int(width) / 2 - titleframe.winfo_width() / 2
titleframe.grid(column=0, row=0, padx=xbias, pady=10)

# Load JSONs
vaultData = json.load_json(json.vault_path)
skillData = json.load_json(json.skills_path)

entriesframe = Frame(skillframe)
exitsframe = Frame(skillframe)
testframe = Frame(skillframe)

event_button("Vault", entries_dropdown, vaultData)
event_button("Bars", create_test_dropdown, skillData)
event_button("Floor", msg_box)
event_button("Beam", msg_box)

# entries_dropdown(vaultData)

root.mainloop()
