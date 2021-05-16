from matplotlib import pyplot as plt
import requests
import pandas as pd
import numpy as np
 
def Plot(plot1, x_y, color='blue', ylab=''):
    plot1.cla()
    x, y = x_y
    x = x[-30:] 
    
    y = y[-30:]

    plot1.set_title(ylab)
    
    plot1.plot(x, y, color=color)
    plot1.scatter(x, y, color=color)

    plot1.set_xlabel('Date')
    plot1.set_ylabel(ylab)
    
    plot1.set_xticks(np.arange(0,29,2))

    plot1.tick_params('x',labelrotation=45, pad=0.5, labelsize=8, )

def PlotPie(plot1, active, recovered, dead):
     
    plot1.pie([active, recovered, dead], labels=[f'Active({active})', f'Recovered({recovered})', f'Deceased({dead})'])
  
 
