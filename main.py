import pandas as pd
import numpy as np
from tkinter import *
from tkinter.ttk import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt

emissionsDataSet = pd.read_csv('emissionsData.csv')

select_country = emissionsDataSet.loc[emissionsDataSet['Country'] == 'United States']


def plot():
    countryA = combo1.get()
    countryB = combo2.get()

    countryAEmissions = emissionsDataSet.loc[emissionsDataSet['Country'] == countryA, emissionsDataSet.columns != 'Country'].values.tolist()[0]
    countryBEmissions = emissionsDataSet.loc[emissionsDataSet['Country'] == countryB, emissionsDataSet.columns != 'Country'].values.tolist()[0]

    years = emissionsDataSet.columns.values.tolist()
    years.remove('Country')

    #plt.xticks(countryBEmissions, years)
    plt.scatter(years, countryAEmissions, label=countryA)
    plt.scatter(years, countryBEmissions, label=countryB)
    plt.xlabel('years')
    plt.ylabel('Tonnes of Green House Gasses (Note the scale in the top left)')
    plt.title('Emissions of '+countryA+" vs "+countryB)
    plt.legend()

    zA = np.polyfit(years, countryAEmissions, 1)
    pA = np.poly1d(zA)
    plt.plot(years,pA(years),"r--")

    zB = np.polyfit(years, countryBEmissions, 1)
    pB = np.poly1d(zB)
    plt.plot(years,pB(years),"r--")

    plt.show()


window = Tk()

window.title("Emissions Calculator")
window.geometry('300x125')

lb1 = Label(window, text="Country A")
lb1.pack()

combo1 = Combobox(window)
combo1['values']=emissionsDataSet['Country'].tolist()
combo1.current(2)
combo1.pack()

lb2 = Label(window, text="Country B")
lb2.pack()

combo2 = Combobox(window)
combo2['values']=emissionsDataSet['Country'].tolist()
combo2.current(3)
combo2.pack()

plot_button = Button(master = window, command = plot, text = "Plot")
plot_button.pack()

window.mainloop()
