import numpy as np
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox

from MainTask import MainTask
from Generator import Generator
from Validator import Validator
import Interface as ui

# Global ---------------------

gen = Generator()
valid = Validator()
dictionary = {}
id = 0
for item in ui.comboBoxItems:
    dictionary[item] = id
    id += 1

#Events -----------------

def Clear(e):
    ui.textbox.delete('1.0', END)

def CreateVector(e):
    result = valid.ValidVector(ui.entrySize.get(), ui.entryX.get(), ui.entryY.get())
    if isinstance(result, str):
        messagebox.showinfo("Input Error", "Check your inputs on left panel\n" + str(result))
        return 0
    array = gen.GetVector(result[0], dictionary[ui.cb.get()])
    ui.textbox.insert(INSERT, array.__str__() + "\n")
    try:
        task = MainTask(array)
        count = task.TaskVector(result[1], result[2])
        ui.textbox.insert(INSERT, "Кількість елементів перед першим відємним елементом = " + str(count) + "\n")
    except Exception as ex:
        messagebox.showinfo("Input Error", ex)

def CreateMatrix(e):
    result = valid.ValidMatrix(ui.entryRows.get(), ui.entryCols.get())
    if isinstance(result, str):
        messagebox.showinfo("Input Error", "Check your inputs on left panel\n" + str(result))
        return 0
    array = gen.GetMatrix(result[0], result[1], dictionary[ui.cb.get()])
    ui.textbox.insert(INSERT, array.__str__() + "\n")
    try:
        task = MainTask(array)
        newArray, column = task.TaskMatrix()
        if column == -1:
            ui.textbox.insert(INSERT, "Найменший, додатній елемент матриці знаходиться у останьому стовпці\n")
        else:
            ui.textbox.insert(INSERT, "Найменший, додатній елемент матриці знаходився у стовпці № " + str(column) + "\n")
            ui.textbox.insert(INSERT, newArray.__str__() + "\n")
    except Exception as ex:
        messagebox.showinfo("Input Error", ex)

#Main ---------------
def main():
    ui.btnCreateVector.bind("<Button-1>", CreateVector)
    ui.btnClear.bind("<Button-1>", Clear)
    ui.btnCreateMatrix.bind("<Button-1>", CreateMatrix)
    ui.root.mainloop()

if __name__ == "__main__":
    main()