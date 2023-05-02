#To read csv
import pandas as pd

#Import Bokeh libs
from bokeh.layouts import gridplot
from bokeh.models import CDSView, ColumnDataSource, IndexFilter
from bokeh.plotting import figure, save

#Import data
data = pd.read_csv("Great-Metal-Songs.csv")

#Print the data
print(data)

# Convert the data from pandas
source = ColumnDataSource(data)

#First figure
p = figure(height=500, width=500)
p.circle(x="avg. ENERGY", y="Rating", size=10, hover_color="red", source=source)
''''''
#Second Figure
p = figure(height=500, width=500)
p.vbar(x="avg. ENERGY", top="Rating", width=0.5, bottom=0, color="red", source=source)

#Third Fiure
p = figure(height=500, width=500)
p.line(x="avg. ENERGY", y="Rating", line_color="blue", line_width=2,source=source)

#We average the data and translate to bokeh
grouped=data.groupby('Rating', as_index=False).mean()
grouped = ColumnDataSource(grouped)

p = figure(height=500, width=500)
p.line(y="avg. ENERGY", x="Rating", line_color="blue", line_width=2, source=grouped)

#We average the data and translate to bokeh
grouped=data.groupby('Rating', as_index=False).mean()
grouped = ColumnDataSource(grouped)

p = figure(height=500, width=500)
p.line(y="avg. ENERGY", x="Rating", line_color="blue", line_width=2, source=grouped)
p.line(y="Total Seconds", x="Rating", line_color="red", line_width=2, source=grouped)

#We average the data and translate to bokeh (log)
grouped=data.groupby('Rating', as_index=False).mean()
grouped = ColumnDataSource(grouped)

p = figure(height=500, width=500,y_axis_type="log")
p.line(y="avg. ENERGY", x="Rating", line_color="blue", line_width=2, source=grouped)
p.line(y="Total Seconds", x="Rating", line_color="red", line_width=2, source=grouped)

#To generate the html, you can also use show to open the explorer
save(p)