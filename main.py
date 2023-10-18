from langchain_helper import generateDescription
import streamlit as st


# st.title(Pet Name Generator)
# animal = st.text_input("Animal", "")
# color = st.text_input("Color", "")
# clicked = st.button("Generate")

name = st.sidebar.text_input(
    "What is your name?")
sample1 = st.sidebar.text_area("Enter Sample 1:")
sample2 = st.sidebar.text_area("Enter Sample 2:")
sample3 = st.sidebar.text_area("Enter Sample 3:")
sample4 = st.sidebar.text_area("Enter Sample 4:")


if st.sidebar.button("Generate"):
    st.write(generateDescription(name, sample1, sample2, sample3, sample4))
