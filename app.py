import streamlit as st

'''
###Our super important survey!
Help us out by filling in the following questions
'''

with st.beta_form(submit_label="I'm done!", key="my_form"):
  name = st.text_input("What is your name?")  
  color = st.selectbox(
      'What is your favorite color?',
      ('Blue','Green','Red','Rainbow','Other')
  swallow = st.slide('What is the airspeed velocity of an unladen swallow?,0,100)
  
