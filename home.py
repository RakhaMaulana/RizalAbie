import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie

st.set_page_config(
        page_title="Malaria Blood Detection",
        page_icon="drop_of_blood"
    )

st.sidebar.success("")

url = "https://lottie.host/49a2e68c-3ad6-4786-a147-4d3fe335fc08/YlDE6LYVXO.json"

st.title("Malaria Detection")

_left, mid, _right = st.columns([0.2, 0.5, 0.2])
with mid:
    st_lottie(url,key='Medic')

with st.expander("What website is this?"):
    st.write("This website designed to detect Malaria using Deep Learning approach with more than 20 thousand images")

st.text("How to detect?")

st.write("With your blood smear retrieved from laboratory")
