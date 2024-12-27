import streamlit as st

# Page Config
st.title("Home")

st.info("Select a page to start.")

st.page_link("views/0_Machine_Learning.py", label="Machine Learning", icon="➡️")
st.page_link("views/1_Deep_Learning.py", label="Deep Learning", icon="➡️")
