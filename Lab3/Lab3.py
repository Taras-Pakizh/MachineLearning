from numpy import *
import matplotlib.pyplot as plt
from tkinter import *
from tkinter.colorchooser import *
from sklearn.datasets import fetch_lfw_pairs
import matplotlib

import Interface as ui

#global
_styles = ("-", '--', '-.', ':')
_markers = (None, '.', 'o', '^', 's', '*')

_color = '#555555'
_points = 10
_style = _styles[0]
_thickness = 2
_marker = _markers[0]

#Events ----------------------
def ColorChoose(e):
    global _color
    result = askcolor()
    _color = result[1]

def Main(e):

    _points = ui.pointsScale.get()
    _style = _styles[ui.comboBoxStyles.index(ui.cbStyle.get())]
    _thickness = ui.thicknessScale.get()
    _marker = _markers[ui.comboBoxMarkers.index(ui.cbMarker.get())]

    valuesX = linspace(0, 5, _points)
    valuesY = Func(valuesX)
    plt.plot(valuesX, valuesY, marker=_marker, color=_color, linestyle=_style, linewidth=_thickness, label='5*cos(10*x)*sin(3*x)/(x^(1/2))')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.savefig('figure.png')
    plt.show()

def Train(e):
    bunch = fetch_lfw_pairs()
    xdata = [0, 1]
    same = sum(bunch.target)
    ydata = [len(bunch.target) - same, same]
    plt.bar(xdata[0], ydata[0], color='brown')
    plt.bar(xdata[1], ydata[1], color='red')
    plt.xlabel('Target names')
    plt.ylabel('Frequency')
    plt.legend(['Different persons', 'Same persons'])
    plt.title('Bars')
    plt.savefig('bar.png')
    plt.show()
   
def Run(d):
    valx = linspace(0, 5, 50)
    valy1 = Fun1(valx)
    valy2 = Fun2(valx)
    plt.plot(valx, valy1, marker='h', color='y')
    plt.plot(valx, valy2, marker='+', color='b')
    plt.show()

def Fun1(x):
    return 5*sin(x)

def Fun2(x):
    return 0.5*(exp**(-x))
    
#--------------------------------

#Task
def Func(arg):
    return 5*cos(10*arg)*sin(3*arg)/(arg**(0.5))

def main():
    ui.btnMain.bind("<Button-1>", Main)
    ui.btnColor.bind("<Button-1>", ColorChoose)
    ui.btnBar.bind("<Button-1>", Train)
    mainloop()

if __name__ == "__main__":
    main()
    valx = linspace(0, 5, 50)
    valy1 = Fun1(valx)
    #valy2 = Fun2(valx)
    plt.plot(valx, valy1, marker='h', color='y')
    #plt.plot(valx, valy2, marker='+', color='b')
    plt.show()
