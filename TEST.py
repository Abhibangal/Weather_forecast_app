import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(layout='centered', page_title='Happiness Index')

st.title('In Search for Happiness')

x_axis = st.selectbox('Select data for X axis', ['GDP', 'Happiness', 'Generosity'])
y_axis = st.selectbox('Select data for y axis', ['GDP', 'Happiness', 'Generosity'])

st.subheader(f"{x_axis} and  {y_axis}")


def get_x_y_data(x, y):
    x = x.casefold()
    y = y.casefold()
    ggh_df = pd.read_csv('happy.csv')
    x_data = ggh_df[x]
    y_data = ggh_df[y]
    return x_data, y_data


x, y = get_x_y_data(x_axis, y_axis )
figure = px.scatter(x=x, y=y, labels={'x': x_axis, 'y': y_axis})
st.plotly_chart(figure)
print(x_axis , y_axis )



