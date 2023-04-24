import pandas as pd
#import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import datetime
import numpy as np
import time
import plotly.graph_objects as go
from PIL import Image
#import altair as alt

# Use the full page instead of a narrow central column
st.set_page_config(page_title="XYZ Company", layout="wide")

st.title("Sales Dashboard of XYZ Company")
st.markdown("For fiscal year 2020/2021")

#loading the dataset
revenue_data = pd.read_excel(r"Revenue1.xlsx")

#computing total sales amount
total_sales = revenue_data['sales_amount'].sum()
st.write("Total Sales: NPR ",int(total_sales/1000000),"Millions")

#computing best performing salesperson


#creating newdataframe
data = revenue_data[['sales_amount']].copy()

#generating the current time stamp
#localtime = [datetime.datetime.now() + datetime.timedelta(hours=i) for i in range(1462)]

#creating new dataframe to store timestamp and sales ampunt
mean_sales = pd.DataFrame()
#mean_sales['time']= localtime

#computing the average of each 100 data in dataframe
mean_sales = data.groupby(np.arange(len(data))//100).mean()
new_data = np.array(mean_sales)

def view_revenue():
    st.subheader('Revenue Table')
    st.table(revenue_data.head(5))

my_expander = st.expander("View Dataset", expanded=False)

with my_expander:
    view_revenue()

#unit_cost = product_data['Unit Cost']* revenue_data['quantity_items']
#profit = total_sales - unit_cost.sum()
#st.write("Total profit for the year: NPR", profit)

col1, col2= st.columns(2)
#revenue_data['OrderValue']= range(1, 1+len(revenue_data))

#left hand side column begins
with col1:
    #drawing line chart
    st.subheader("Order Date Vs Sales Amount")
    linechart = px.line(revenue_data, x='time_stamp', y='sales_amount', color='team')
    st.plotly_chart(linechart)

    #plotting real time continuous dataset
    if st.checkbox("See the live chart"):
        chart = st.line_chart()
        for i in range(0, len(mean_sales)):
            new_rows = new_data[i]
            chart.add_rows(new_rows)
            time.sleep(0.05)

        st.button("Re-run")

    # drawing 3d chart
    st.subheader("Salesperson Vs Quantity")
    barchart = px.histogram(revenue_data, x='salesperson',y='quantity_items')
    st.plotly_chart(barchart)


# right hand side column begins
with col2:
#drawing the piechart
    st.subheader("Vendors Vs Sales")
    piechart = px.pie(revenue_data, values='sales_amount', names='team')
    st.plotly_chart(piechart)

    st.subheader("Salesperson Vs Sales")
    piechart = px.pie(revenue_data, values='sales_amount', names='salesperson')
    #piechart = px.funnel(revenue_data, x='sales_amount', y='salesperson')
    st.plotly_chart(piechart)

st.markdown("<h3 style='text-align: center;'>-----Dashboard by-----</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'> Ashish KC Khatri </h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'> Data Analyst </h4>", unsafe_allow_html=True)
#st.write("Website: [Portfolio](https://ashishkhatri.com.np)")
st.markdown("<h4 style='text-align: center;'> Website:www.ashishkhatri.com.np </h4>", unsafe_allow_html=True)

#image = Image.open('D:/Ashish Drive/Document/Company/karyathalologo/logo-karyathalo.png')
#st.image(image,use_column_width=True)
