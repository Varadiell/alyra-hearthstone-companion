import streamlit as st

# Page Setup

home_page = st.Page(
    page="views/Home.py",
    title="Home",
    icon="🏡",
    default=True
)
machine_learning_page = st.Page(
    page="views/0_Machine_Learning.py",
    title="Machine Learning",
    icon="🤖",
)
deep_learning_page = st.Page(
    page="views/1_Deep_Learning.py",
    title="Deep Learning",
    icon="🌌",
)

pg = st.navigation({
    "Home": [
        home_page,
    ],
    "Predictions": [
        machine_learning_page,
        deep_learning_page,
    ],
})

st.set_page_config(
    layout="wide",
)

st.sidebar.text("Made with ❤️")

pg.run()
