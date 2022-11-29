import streamlit as st
import plotly.express as px
import backend as bk

st.set_page_config(layout='centered', page_title='Weather Forecast')
st.title('Weather Forecast for the Next Day')

place = st.text_input(label='Place:', key='place', placeholder='City', autocomplete='Press enter to apply')

days = st.select_slider(label='Forecast Days', options=range(1, 6))
if days == 1:
    str_day = 'day'
else:
    str_day = 'days'
topic = st.selectbox(label='Select Data to view', options=('Temperature', 'Sky'))


try:
    if place != '':
        dt, data = bk.get_data(place, days, topic)
        head_label = f'{topic} for next {days} {str_day} in {place}'
        st.subheader(head_label)
        if topic == 'Temperature':
            figure = px.line(x=dt, y=data, labels={'x': 'Date', 'y': 'Temperature (C)'})
            st.plotly_chart(figure)
        else:
            image = {'Clear': 'images/clear.png','Clouds': 'images/cloud.png', 'Rain': 'images/rain.png',
                     'Snow': 'images/snow.png'}
            image = [image[i] for i in data]
            st.image(image, width=115 )
    else:
        st.info('Please enter city name')
except KeyError:
    st.info('This place does not exists')
