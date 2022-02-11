import streamlit as st

st.title('''CELSIUS TO FAHRENHEIT CONVETER''')



C=st.slider('slide your celsius value')

F=(9/5*C)+32

st.write('celsius     ', C,'°c is equal to fareheit ', F,'°f',)
