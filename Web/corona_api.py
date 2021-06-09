from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from corona_gui import *
from corona_pre import *
import mpld3
from tk_Dash import onlyPlot

from flask import Flask, render_template, request
 

# from sklearn import
# from flask_sqlalchemy import SQLAlchemy
# text='hhhhhhh'
app = Flask(__name__)
countries=[]

@app.route("/")
def index(text="Wormld"):
    global countries
    countries = getCountries()
    return render_template("base.html", value=countries, sel=countries[0])

@app.route("/", methods=["POST"])
def my_form_post():
    country = request.form["text"]

    data = Process(country.strip())
    
    fig = onlyPlot(*data)[0]

    html_str = mpld3.fig_to_html(fig)
    Html_file= open("./templates/index.html","w")
    Html_file.write(html_str)
    Html_file.close()

    return render_template("index2.html", value=countries, sel=country)


@app.route("/plot")
def api():
    country = request.args.get('country')
    
    data = Process(country.strip())
    
    fig = onlyPlot(*data)[0]

    html_str = mpld3.fig_to_html(fig)
    Html_file= open("./templates/index.html","w")
    Html_file.write(html_str)
    Html_file.close()

    return render_template("index.html") 

  
if __name__ == "__main__":
    app.run(debug=True)
 