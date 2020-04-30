import pandas as pd
from bokeh.plotting import figure, output_file, show, output_notebook
import csv
output_notebook()

def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)


GDP = pd.read_csv('clean_gdp.csv')

Unemployement = pd.read_csv('clean_unemployment.csv')

print(GDP.head())

print(Unemployement.head())

print(Unemployement[Unemployement['unemployment'] > 8.5])

x = GDP['date']

gdp_change = GDP["change-current"]

unemployment = Unemployement["unemployment"]

title = "Impact of GDP on unemployment"

file_name = "index.html"

make_dashboard(x, gdp_change, unemployment, title, file_name)