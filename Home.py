import streamlit as st
from datetime import datetime

today = datetime.today().strftime("%H:%M:%S")

st.title(today)

model = st.selectbox("Choose your model", ["gpt-4o", "gpt-3.5-turbo"])

st.write(model)

name = st.text_input("Enter your name")

st.write(name)

value = st.slider("temperature", min_value=0.1, max_value=1.0),

st.write(value),