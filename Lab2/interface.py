from tkinter import *
import tkinter.ttk as ttk

#Window
root = Tk()
root.title("Lab 2")
root.geometry("450x150")

# count - neighbors, photos, persentOfSize

#Labels
Label(root, text="Neighbors (K)").grid(row=0, column=0)
Label(root, text="Photos to shows").grid(row=0, column=1)
Label(root, text="Percentage of test set").grid(row=0, column=2)

#Scales
ScaleNeighbors = Scale(root, from_ = 1, to = 10, orient=HORIZONTAL)
ScalePhotos = Scale(root, from_=1, to = 10, orient=HORIZONTAL)
ScaleTestSize = Scale(root, from_=0, to = 1, orient=HORIZONTAL, resolution=0.01)

#Button
btn = Button(root, text = "Run")


#Grid
ScaleNeighbors.grid(row=1, column=0, ipadx=10, ipady=6, padx=10, pady=10)
ScalePhotos.grid(row=1, column=1, ipadx=10, ipady=6, padx=10, pady=10)
ScaleTestSize.grid(row=1, column=2, ipadx=10, ipady=6, padx=10, pady=10)
btn.grid(row=2, column=2, ipadx=10, ipady=6, padx=10, pady=10)

#Default
ScaleNeighbors.set(2)
ScalePhotos.set(5)
ScaleTestSize.set(0.25)


