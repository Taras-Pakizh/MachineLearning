from tkinter import *
import tkinter.ttk as ttk
from tkinter.colorchooser import *

comboBoxStyles = ("Solid line",
                 "Dashes line",
                 "Dotted line",
                 "Dashed-Dotted line",)

comboBoxMarkers = ("None",
                   "Point",
                   "Circle",
                   "Triangle",
                   "Rectancle",
                   "Star")

#Window
root = Tk()
root.title("Lab 3")
root.geometry("800x150")

# count of points, color, style, thickness, markers

#Labels
Label(root, text="Point count").grid(row=0, column=0)
Label(root, text="Choose style").grid(row=0, column=2)
Label(root, text="Choose thickness").grid(row=0, column=3)
Label(root, text="Choose marker type").grid(row=0, column=4)

#Parameters
pointsScale = Scale(root, from_=5, to = 100, orient=HORIZONTAL)
btnColor = Button(root, text='Choose color')
cbStyle = ttk.Combobox(root, state='readonly', values=comboBoxStyles)
thicknessScale = Scale(root, from_=0.5, to = 5, orient=HORIZONTAL, resolution=0.1)
cbMarker = ttk.Combobox(root, state='readonly', values=comboBoxMarkers)

#Button
btnMain = Button(root, text = 'Create and Save Plot')
btnBar = Button(root, text = ' Create and Save Bar')

#Grid
pointsScale.grid(row=1, column=0, ipadx=10, ipady=6, padx=10, pady=10)
btnColor.grid(row=1, column=1, ipadx=10, ipady=6, padx=10, pady=10)
cbStyle.grid(row=1, column=2, ipadx=10, ipady=6, padx=10, pady=10)
thicknessScale.grid(row=1, column=3, ipadx=10, ipady=6, padx=10, pady=10)
cbMarker.grid(row=1, column=4, ipadx=10, ipady=6, padx=10, pady=10)
btnMain.grid(row=2, column=4, ipadx=10, ipady=6, padx=10, pady=10)
btnBar.grid(row=2, column=3, ipadx=10, ipady=6, padx=10, pady=10)

#Default
cbStyle.set(comboBoxStyles[0])
cbMarker.set(comboBoxMarkers[0])
pointsScale.set(10)
thicknessScale.set(2)
