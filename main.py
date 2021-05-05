import pandas as pd
import numpy as np
from tkinter import *
from tkinter.ttk import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt

emissionsDataSet = pd.read_csv('emissionsData.csv')

select_country = emissionsDataSet.loc[emissionsDataSet['Country'] == 'United States']

#print(select_country.values.tolist()[0])

def plot():
    countryA = combo1.get()
    countryB = combo2.get()
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5), dpi = 100)
  
    # list of squaress
    countryAEmissions = emissionsDataSet.loc[emissionsDataSet['Country'] == countryA, emissionsDataSet.columns != 'Country']
    countryBEmissions = emissionsDataSet.loc[emissionsDataSet['Country'] == countryB, emissionsDataSet.columns != 'Country']

    # adding the subplot
    plot1 = fig.add_subplot(111)
  
    # plotting the graph
    plot1.plot(countryAEmissions.values[0].tolist())
    plot1.plot(countryBEmissions.values[0].tolist())
    
    title="Emissions: "+countryA+" vs "+countryB

    fig.suptitle(title, fontsize=16)
    #plot1.set_ylable("Green House Gases (in tonnes)", fontsize=14)
    #plot1.set_xlable("year", fontsize=14)


    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master = window)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

window = Tk()

window.title("Emissions Calculator")
#window.geometry('900x900')

lb1 = Label(window, text="Country A")
lb1.pack()

combo1 = Combobox(window)
combo1['values']=emissionsDataSet['Country'].tolist()
combo1.current(1)
combo1.pack()

lb2 = Label(window, text="Country B")
lb2.pack()

combo2 = Combobox(window)
combo2['values']=emissionsDataSet['Country'].tolist()
combo2.current(2)
combo2.pack()

plot_button = Button(master = window, command = plot, text = "Plot")
plot_button.pack()

window.mainloop()
