import streamlit as st
import pandas as pd
import plotly_express as px
# reading the data file

df = pd.read_csv('vehicles_us.csv')
# setting a header for the app
st.header("Used Cars Dealership")
# setting a minimun and maximum price for viewing
lower = df['price'].quantile(0.5)
upper = df['price'].quantile(0.97)
#checkbox for exluding outliers
disregard_outliers = st.checkbox('No outliers in price Distribution')

if disregard_outliers:
    filtered_df = df[(df['price'] >= lower) & (df['price'] <= upper)]
else:
    filtered_df = df

#creating a histogram
hist = px.histogram(filtered_df, x='price',title='Price Distribution', color_discrete_sequence=['blue'],nbins=50)
if st.checkbox("View Data through a histogram"):
    st.plotly_chart(hist)

# creating a scatter plot
scatter = px.scatter(filtered_df, x='price', y='odometer',title='Price Vs Mileage', color_discrete_sequence=['red'],labels={
    'price':'Price in Dollar$$', 'odometer':'Mileage in Miles'
})
#displaying the graph
if st.checkbox("Relationship Visual via a scatter graph"):
    st.plotly_chart(scatter)
# display raw data
if st.checkbox("Prefer raw data"):
    st.write(filtered_df)

# loading data by running streamlit run app.py on the terminal


