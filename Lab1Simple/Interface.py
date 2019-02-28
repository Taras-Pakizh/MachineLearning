from tkinter import *
import tkinter.ttk as ttk

comboBoxItems = ("Real 0 to 1",
                 "Real -10 to 10",
                 "Integer -10 to 10",
                 "Integer 0 to 20",
                 "Integer 0 to 50")

#Window
root = Tk()
root.title = "Fuck Tkinter"
root.geometry("800x500")

#Frames
LeftPanel = Frame(root, height = 500, width = 200, padx=5, pady=5)
RightPanel = Frame(root, height = 400, width = 600, padx=5, pady=5)
SubBottonPanel = Frame(RightPanel, height = 100, width = 600, padx=5, pady=5)

LeftPanel.pack(side=LEFT)
RightPanel.pack(side=RIGHT)
SubBottonPanel.pack(side=BOTTOM)

#SubBottonPanel -----------------------------------

#Create Vector
btnCreateVector = Button(SubBottonPanel, text="Create vector")
btnCreateVector.grid(row=0, column=0, ipadx=10, ipady=6, padx=10, pady=10)

#Create Matrix
btnCreateMatrix = Button(SubBottonPanel, text="Create matrix")
btnCreateMatrix.grid(row=0, column=1, ipadx=10, ipady=6, padx=10, pady=10)

#ComboBox
cb = ttk.Combobox(SubBottonPanel, state='readonly', values=comboBoxItems)
cb.set(comboBoxItems[0])
cb.grid(row=0, column=2, ipadx=10, ipady=6, padx=10, pady=10)

#Clear
btnClear = Button(SubBottonPanel, text="Clear")
btnClear.grid(row=0, column=3, ipadx=10, ipady=6, padx=10, pady=10)

#LeftPanel ------------------------------- rows = 7 cols = 2

#Labels
Label(LeftPanel, text="Inputs for Task 1").grid(row=0, column=0, columnspan=2)
Label(LeftPanel, text="X").grid(row=1, column=0)
Label(LeftPanel, text="Y").grid(row=2, column=0)
Label(LeftPanel, text="Vector size").grid(row=3, column=0)
Label(LeftPanel, text="Inputs for Task 2").grid(row=4, column=0, columnspan=2)
Label(LeftPanel, text="Rows").grid(row=5, column=0)
Label(LeftPanel, text="Columns").grid(row=6, column=0)

#Entries
entryX = Entry(LeftPanel)
entryX.grid(row=1, column=1, ipadx=10, ipady=6, padx=10, pady=10)

entryY = Entry(LeftPanel)
entryY.grid(row=2, column=1, ipadx=10, ipady=6, padx=10, pady=10)

entrySize = Entry(LeftPanel)
entrySize.grid(row=3, column=1, ipadx=10, ipady=6, padx=10, pady=10)

entryRows = Entry(LeftPanel)
entryRows.grid(row=5, column=1, ipadx=10, ipady=6, padx=10, pady=10)

entryCols = Entry(LeftPanel)
entryCols.grid(row=6, column=1, ipadx=10, ipady=6, padx=10, pady=10)

#RightPanel -------------------------------

textbox = Text(RightPanel, font='Arial 14', wrap='word')
textbox.pack(expand=True)

