import streamlit as st
st.title("Hello")
a = st.number_input('Pick a number', 0,10)
b = st.number_input('Pick another number', 0,10)
d = st.number_input('what is the sum of this two numbers', 0,20)
c = a + b
if d == c :
    st.title("You are correct")
else:
    st.title("wrong!! Try again")