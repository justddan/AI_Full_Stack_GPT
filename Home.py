import streamlit as st
from langchain.prompts import PromptTemplate

st.write("hello")

st.write([1,2,3,4])

st.write({"a": 1, "b": 2})

st.write(PromptTemplate)

p = PromptTemplate.from_template("xxxx")

st.write(p)

a = [1,2,3,4,5]

d = {"a": 1, "b": 2}

a

d

p

st.selectbox("Choose your model", ["gpt-4o", "gpt-3.5-turbo"])