from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from corona_gui import *
from corona_pre import *

canvas=[]
toolbar=[]
k=''
def embed_plot(dates, conf_series, rec_series, active_series, ded_series, new_series):
    global canvas, toolbar
    try: 
        canvas.get_tk_widget().pack_forget()
    except AttributeError: 
        pass
    
    # the figure that will contains the plot
    fig = Figure(figsize=(16/1.4, 9/1.4), dpi=100)

    
    # adding the subplot
    plot1 = fig.add_subplot(221)
    plot2 = fig.add_subplot(222)      
    plot3 = fig.add_subplot(223)
    plot4 = fig.add_subplot(224)

    

    # plotting the graph
    #plot1.plot(y)

    Plot(plot1, [dates, active_series], color='orange', ylab='Active')
    Plot(plot2, [dates, new_series], color='purple', ylab='New Cases')
    Plot(plot3, [dates, rec_series], color='green', ylab='Recovered')
    Plot(plot4, [dates, ded_series], color='red', ylab='New Deaths')
 
    
 
     

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
    fig.tight_layout(pad=1.5)
    

def main():
    global k
    country = n.get()
 
    k.set(country)
 
    data = Process(country.strip())
    
    embed_plot(*data)
       
 
# the main Tkinter window
window=Tk()

# setting the title and dimensions of the main window
window.title('COVID Dashboard')
window.geometry('1000x800')

from tkinter import ttk

n = StringVar() 
countrychoosen = ttk.Combobox(window, width = 27, textvariable = n) 

c=tuple(getCountries())  
# Adding combobox drop down list 
countrychoosen['values'] = c 
  
countrychoosen.grid(column = 1, row = 5) 
#countrychoosen.current()
countrychoosen.pack()
 
# button that displays the plot
plot_button = Button(master=window, command=main, height=2, width=10, text="Plot")
plot_button.pack()

k = StringVar()
heqading = Label(window, width=50, height=2, anchor='center', textvariable=k)
heqading.config(font=("Courier", 30))
heqading.pack()
 
#print(n.get())
window.mainloop()
