import streamlit as st
import time

import sys
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

import plotly.express as px
from datetime import datetime as dt

from streamlit_metrics import metric, metric_row


sys.setrecursionlimit(100000)
#print("Installed Dependencies")


def app():
    st.title("COVID-19 BEFORE-DURING ANALYSIS IN FRANCE")
    
    st.header("LOCKDOWN PHASES")
    
    st.subheader("Loading the COVID-19 Data....")
    
    file = st.file_uploader("Upload file")
    show_file = st.empty()
    
    if not file:
        show_file.info("Please upload a file of type: " + ", ".join([".csv", ".xls", ".xlsx"]))
        return
    
    label = st.empty()
    bar = st.progress(0)
    
    for i in range(100):
        # Update progress bar with iterations
        label.text(f'Loaded {i+1} %')
        bar.progress(i+1)
        time.sleep(0.01)
    
    path = file #'new_master_data.csv'
    data = pd.read_csv(path)
    #print("Data Shape: ", data.shape)
    data.head()
    #print("Data Shape: ", data.shape)
    #data.head()
    
    ".... and now we're done!!!"
    
    ###########################################################################
    
    def plot(city):
      fig = go.Figure()
      fig.add_trace(go.Scatter(x = max[max.City == city].date, y = max[max.City == city].Concentration, name = "max conc.", mode = "lines", line=dict(color='blue')))
      fig.add_trace(go.Scatter(x = min[min.City == city].date, y = min[min.City == city].Concentration, name = "min conc.", line=dict(color='red')))
      fig.add_trace(go.Scatter(x = ['2020-03-01', '2020-04-15', '2020-07-20', '2020-11-15', '2021-01-20', '2021-03-27', '2021-06-15'], y = [800, 800, 800, 800, 800, 800, 800], 
                               mode="text", name="Labels", text=["No Lockdown", "1st Lockdown", "No Lockdown", "2nd Lockdown", "No Lockdown", "3rd Lockdown", "No Lockdown"], textposition="top center"))
      fig.update_xaxes(title_text = "Date", rangeslider_visible=True, showline=True, linewidth=2, linecolor='black', mirror=True)
      fig.update_yaxes(title_text = "Average Concentration", showline=True, linewidth=2, linecolor='black', mirror=True)
      fig.update_layout(height=700, width=1500, title_text="Average Concentration (Unit - µg/m³) of Air Pollutants in France from 2020-21 :: " + city,
                          shapes = [dict(type = "rect", y0 = -50, y1 = 1000, x0="2020-02-05", x1="2020-03-17", name = "No Lockdown", fillcolor = "green", opacity = 0.5),
                                    dict(type = "rect", y0 = -50, y1 = 1000, x0="2020-03-17", x1="2020-05-10", name = "1st Lockdown", fillcolor = "red", opacity = 0.5),
                                    dict(type = "rect", y0 = -50, y1 = 1000, x0="2020-05-10", x1="2020-10-17", name = "No Lockdown", fillcolor = "green", opacity = 0.5), 
                                    dict(type = "rect", y0 = -50, y1 = 1000, x0="2020-10-17", x1="2020-12-14", name = "2nd Lockdown", fillcolor = "red", opacity = 0.5),
                                    dict(type = "rect", y0 = -50, y1 = 1000, x0="2020-12-14", x1="2021-02-26", name = "No Lockdown", fillcolor = "green", opacity = 0.5),
                                    dict(type = "rect", y0 = -50, y1 = 1000, x0="2021-02-26", x1="2021-05-02", name = "3rd Lockdown", fillcolor = "red", opacity = 0.5),
                                    dict(type = "rect", y0 = -50, y1 = 1000, x0="2021-05-02", x1="2021-07-27", name = "No Lockdown", fillcolor = "green", opacity = 0.5)]) 
      #fig.show()
      st.plotly_chart(fig)  
      
    
    max = data[["date", "City", "('max', 'co')", "('max', 'dew')", "('max', 'humidity')",
           "('max', 'no2')", "('max', 'o3')", "('max', 'pm10')",
           "('max', 'pm25')", "('max', 'pressure')", "('max', 'so2')",
           "('max', 'temperature')", "('max', 'wind gust')",
           "('max', 'wind speed')"]]
    
    max = max[["date", "City", "('max', 'co')", "('max', 'dew')", "('max', 'no2')", "('max', 'o3')", "('max', 'pm10')", "('max', 'pm25')", "('max', 'so2')"]]
    max = max.melt(id_vars=["date", "City"], var_name = "Pollutants", value_name = "Concentration")
    max.sort_values(["date", "Pollutants"], inplace = True)
    
    min = data[["date", "City", "('min', 'co')", "('min', 'dew')", "('min', 'humidity')", 
           "('min', 'no2')", "('min', 'o3')", "('min', 'pm10')",
           "('min', 'pm25')", "('min', 'pressure')", "('min', 'so2')",
           "('min', 'temperature')", "('min', 'wind gust')",
           "('min', 'wind speed')"]]
    
    min = min[["date", "City", "('min', 'co')", "('min', 'dew')", "('min', 'no2')", "('min', 'o3')", "('min', 'pm10')", "('min', 'pm25')", "('min', 'so2')"]]
    min = min.melt(id_vars=["date", "City"], var_name = "Pollutants", value_name = "Concentration")
    min.sort_values(["date", "Pollutants"], inplace = True)
    
    
    st.subheader("Visualize All Lockdown Phases")
    
    
    if st.checkbox("Plot Bordeaux"): 
            plot("Bordeaux")
    
    if st.checkbox("Plot Grenoble"): 
            plot("Grenoble")
    
    if st.checkbox("Plot Lille"): 
            plot("Lille")
    
    if st.checkbox("Plot Lyon"): 
            plot("Lyon")
    
    if st.checkbox("Plot Marseille"): 
            plot("Marseille")
    
    if st.checkbox("Plot Montepellier"): 
            plot("Montpellier")
    
    if st.checkbox("Plot Nantes"): 
            plot("Nantes")
    
    if st.checkbox("Plot Nice"): 
            plot("Nice")
    
    if st.checkbox("Plot Paris"): 
            plot("Paris")
    
    if st.checkbox("Plot Rouen"): 
            plot("Rouen")
    
    if st.checkbox("Plot Strasbourg"): 
            plot("Strasbourg")
    
    if st.checkbox("Plot Toulouse"): 
            plot("Toulouse")
            
            
            
    ########################################################################### 