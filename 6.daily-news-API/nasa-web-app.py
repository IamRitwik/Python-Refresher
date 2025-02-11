import streamlit as st
import requests

url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
response = requests.get(url)
content = response.json()

st.header(content["title"])
st.image(content["url"])
st.write(content["explanation"])
